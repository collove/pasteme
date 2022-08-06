// Initialize the AOS library
AOS.init();

$(".darkmode-switch").on("click", function () {
    $("html").toggleClass("dark");
    dark_mode = !dark_mode;
    localStorage.theme = dark_mode ? "dark" : "light";
});

// Menu toggle functionality
$("#menu-toggle").on("click", function () {
    if ($("#menu").hasClass("z-10")) {
        $("#menu").removeClass("z-10");
        setTimeout(function () {
            $("#menu").toggleClass("top-[100%_!important]");
        }, 100);
    } else {
        $("#menu").toggleClass("top-[100%_!important]");
        setTimeout(function () {
            $("#menu").toggleClass("z-[10_!important]");
        }, 200);
    }
});
