/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.querySelectorAll('.service-item').forEach(item => {
    item.addEventListener('mouseenter', () => {
      item.classList.add('is-flipped');
    });
  
    item.addEventListener('mouseleave', () => {
      item.classList.remove('is-flipped');
    });
  });


  document.addEventListener('DOMContentLoaded', () => {
    const filters = document.querySelectorAll('.portfolio-filters li'); // Select all filter buttons
    const items = document.querySelectorAll('.portfolio-item'); // Select all portfolio items
  
    filters.forEach(filter => {
      filter.addEventListener('click', () => {
        const filterValue = filter.getAttribute('data-filter'); // Get the filter value
        
        // Remove active class from all filters and set it to the clicked one
        filters.forEach(f => f.classList.remove('filter-active'));
        filter.classList.add('filter-active');
  
        // Show/Hide portfolio items based on the filter
        items.forEach(item => {
          if (filterValue === '*' || item.classList.contains(filterValue.slice(1))) {
            item.style.display = 'block'; // Show item
          } else {
            item.style.display = 'none'; // Hide item
          }
        });
      });
    });
  });
  