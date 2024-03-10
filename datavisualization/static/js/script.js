// show menu toggle
const showMenu = (toggleId, navId) => {
  const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId);

  toggle.addEventListener("click", () => {
    // add show-menu class to nav menu
    nav.classList.toggle("show-menu");
    // add show-icon class to show and hide drop-arrow
    toggle.classList.toggle("show-icon");
  });
};

showMenu("nav-toggle", "nav-menu");

// scroll reveal animations
document.addEventListener("DOMContentLoaded", function () {
  const scrollReveal = ScrollReveal({
    duration: 1000,
    reset: true,
  });

  // home, viz, and analytics
  scrollReveal.reveal(".main-section", {
    origin: "bottom",
    distance: "20px",
    delay: 200,
  });

  // cards
  scrollReveal.reveal(".cards-section", {
    origin: "bottom",
    distance: "20px",
    delay: 200,
  });
});

// select menu input fields
document.querySelectorAll(".select-menu").forEach((menu) => {
  const selectBtn = menu.querySelector(".select-btn");
  const options = menu.querySelectorAll(".option");
  const optionText = menu.querySelector(".select-text");

  selectBtn.addEventListener("click", () => {
    // Close any already open select menus
    document.querySelectorAll(".select-menu").forEach((otherMenu) => {
      if (otherMenu !== menu) {
        otherMenu.classList.remove("active");
      }
    });

    // Toggle the current menu
    menu.classList.toggle("active");
  });

  options.forEach((option) => {
    option.addEventListener("click", () => {
      let selected = option.querySelector(".option-text").innerText;
      optionText.innerText = selected;
      menu.classList.remove("active"); // Close the select menu after selection
      console.log(selected);
    });
  });
});
