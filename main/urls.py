from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_info', views.update_info, name='update_info'),
    path('contact/', views.contact_view, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('bahrbeirut/', views.bahrbeirut, name='bahrbeirut'),
    path('furndebeirut/', views.furndebeirut, name='furndebeirut'),
    path('breez/', views.breez, name='breez'),
    path('shwarmaji/', views.shwarmaji, name='shwarmaji'),
    path('beitemali/', views.beitemali, name='beitemali'),
    path('wingsondrinks/', views.wingsondrinks, name='wingsondrinks'),
    path('funkywrap/', views.funkywrap, name='funkywrap'),
]
