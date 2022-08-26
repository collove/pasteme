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

let navbar = document.getElementById("navbar");
let hero = document.getElementById("hero");
let sticky = navbar.offsetTop;

function fixNavbar() {
    if (window.pageYOffset > sticky) {
        // duration class makes the color switch to be smooth and
        // look glitchy when scrolling down so I disable it temporarily
        navbar.classList.remove("transition-colors", "duration-300");
        hero.classList.add("pt-[120px]");
        navbar.classList.add("sticky");

        // transition is used for dark mode switching smoothness so
        // we need it back
        setTimeout(function () {
            navbar.classList.add("transition-colors", "duration-300");
        }, 100);
    } else {
        hero.classList.remove("pt-[120px]");
        navbar.classList.remove("sticky");
    }
}

// Initialize the AOS library
AOS.init();
