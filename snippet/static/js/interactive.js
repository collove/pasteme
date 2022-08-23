// Dark-mode switch functionality
$(".darkmode-switch").on("click", function () {
    $("html").toggleClass("dark");
    dark_mode = !dark_mode;
    localStorage.theme = dark_mode ? "dark" : "light";
});

// Menu toggle functionality
$("#menu-toggle").on("click", function () {
    $("#menu").toggleClass("menu-open");
});

window.onscroll = function () {
    fixNavbar();
};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function fixNavbar() {
    if (window.pageYOffset > sticky) {
        // duration class makes the color switch to be smooth and
        // look glitchy when scrolling down so I disable it temporarily
        navbar.classList.remove("transition-colors", "duration-300");
        navbar.classList.add("sticky");

        // transition is used for dark mode switching smoothness so
        // we need it back
        setTimeout(function () {
            navbar.classList.add("transition-colors", "duration-300");
        }, 100);
    } else {
        navbar.classList.remove("sticky");
    }
}

// Initialize the AOS library
AOS.init();
