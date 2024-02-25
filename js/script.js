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
