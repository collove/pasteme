console.log("interactive.js");

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
