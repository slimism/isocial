from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib import messages
from django.contrib.auth.models import User
from main.models import Product

def not_shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:

        orders = Order.objects.filter(shipped=False)
        return render(request, "payment/not_shipped_dash.html", {"orders": orders})
    else:
        messages.error(request,"Access Denied")
        return redirect('home') 

def shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=True)
        return render(request, "payment/shipped_dash.html", {"orders": orders})
    else:
        messages.error(request,"Access Denied")
        return redirect('home')

def process_order(request):
    if request.POST:
         #Get cart
        cart = Cart(request)
        cart_products = cart.get_prods
        totals = cart.cart_total()
        #Get Billing info from last page 
        payment_form = PaymentForm(request.POST or None)
        #Get Shipping Session Data
        my_shipping = request.session.get('my_shipping')

        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        #Create Shipping address from session info 
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}\n"
        amount_paid = totals

        #create an order
        if request.user.is_authenticated:
            user = request.user
            #Create Order 
            create_order = Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()

            #Add Order Items 
            #Get Order ID 
            order_id =  create_order.pk
            #Get Product Info 
            for product in cart_products():
                #Get Product ID 
                product_id = product.id
                #Get Product price
                price = product.price

                create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, price=price)
                create_order_item.save()

            #Delete our cart 
            for key in list(request.session.keys()):
                if key == "session_key":
                    #Delete Key 
                    del request.session[key]
                


            messages.success(request,"Orders Placed")
            return redirect('home')
        else: 
            create_order = Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()

            
            #Add Order Items 
            #Get Order ID 
            order_id =  create_order.pk
            #Get Product Info 
            for product in cart_products():
                #Get Product ID 
                product_id = product.id
                #Get Product price
                price = product.price

                create_order_item = OrderItem(order_id=order_id, product_id=product_id, price=price)
                create_order_item.save()
                
            #Delete our cart 
            for key in list(request.session.keys()):
                if key == "session_key":
                    #Delete Key 
                    del request.session[key]
                    
            messages.success(request,"Orders Placed")
            return redirect('home')
    else:
        messages.error(request,"You must be logged in")
        return redirect('home')
        

def billing_info(request):
    if request.POST:

        #Get cart
        cart = Cart(request)
        cart_products = cart.get_prods
        totals = cart.cart_total()

        #Create a session with Shipping Info 
        my_shipping = request.POST 
        request.session['my_shipping'] = my_shipping

        #Check to see if logged in 
        if request.user.is_authenticated:
            #Get billing form 
            billing_form = PaymentForm()
            return render(request, "payment/billing_info.html", {"cart_products": cart_products, "totals": totals, "shipping_info":request.POST, "billing_form":billing_form })
        else:
            billing_form = PaymentForm()
            return render(request, "payment/billing_info.html", {"cart_products": cart_products, "totals": totals, "shipping_info":request.POST, "billing_form":billing_form })
        shipping_form = request.POST
        return render(request, "payment/billing_info.html", {"cart_products": cart_products, "totals": totals, "shipping_form":shipping_form })
    else:
        messages.error(request,"You must be logged in")
        return redirect('home')

def payment_success(request):
    return render (request, "payment/payment_success.html", {})

def checkout(request):
    #Get cart
    cart = Cart(request)
    cart_products = cart.get_prods
    totals = cart.cart_total()

    if request.user.is_authenticated:
        #Checkout as Authenticated User
        #Get Shipping User
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        #Get Shipping Form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "payment/checkout.html", {"cart_products": cart_products, "totals": totals, "shipping_form":shipping_form })
    else:
        #Checkout as Guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request, "payment/checkout.html", {"cart_products": cart_products, "totals": totals, "shipping_form":shipping_form })
    
