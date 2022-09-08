(function () {
  // Dark-mode switch functionality
  $(".darkmode-switch").on("click", function () {
    $("html").toggleClass("dark");
    localStorage.theme = $("html").hasClass("dark") ? "dark" : "light";
  });

  // Menu toggle functionality
  $("#menu-toggle").on("click", function () {
    $("#menu").toggleClass("menu-open");
  });

  // This function needs to calculate the display property of the navbar
  // every time the user scrolls.
  window.onscroll = function () {
    fixNavbar();
  };

  let navbar = document.getElementById("navbar");
  let main = document.getElementById("main");
  let height = navbar.offsetHeight;
  let offset = navbar.offsetTop;

  function fixNavbar() {
    if (window.pageYOffset > offset) {
      // duration class makes the color switch to be smooth and
      // look glitchy when scrolling down so I disable it temporarily
      navbar.classList.remove("transition-colors", "duration-300");
      main.style.paddingTop = height + "px";
      navbar.classList.add("sticky");

      // transition is used for dark mode switching smoothness so
      // we need it back
      setTimeout(function () {
        navbar.classList.add("transition-colors", "duration-300");
      }, 100); // This 100ms delay is needed for the color-change to take effect
    } else {
      main.style.paddingTop = 0;
      navbar.classList.remove("sticky");
    }
  }

  // Initialize the AOS library
  AOS.init();
})();
