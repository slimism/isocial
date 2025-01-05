document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.querySelector(".navbar--icon");
    const closeIcon = document.querySelector(".nav--open .fa-times-circle");
    const navOpen = document.querySelector(".nav--open");
    const navUpdated = document.querySelector(".nav--updated");
  
    menuIcon.addEventListener("click", () => {
      navOpen.style.transform = "translateX(0)";
      navUpdated.style.display = "block"; // Make .nav--updated visible
      navUpdated.style.opacity = "1";
      navUpdated.style.pointerEvents = "auto";
    });
  
    closeIcon.addEventListener("click", () => {
      navOpen.style.transform = "translateX(-100%)";
      navUpdated.style.opacity = "0";
      navUpdated.style.pointerEvents = "none";
      setTimeout(() => {
        navUpdated.style.display = "none"; // Hide .nav--updated after transition
      }, 400); // Match the CSS transition duration
    });
  });


  