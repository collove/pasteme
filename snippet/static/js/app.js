let dark_mode = true;

function isMobileDevice() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
        navigator.userAgent
    );
}

function initParticles() {
    dark_mode == true
        ? particlesJS.load(
              "particles-js",
              "/static/js/particles-dark-config.json"
          )
        : particlesJS.load(
              "particles-js",
              "/static/js/particles-light-config.json"
          );
}

// Initialize the AOS library
AOS.init();

// Disable dark mode if the user's device is not set to dark mode
if (!window.matchMedia("(prefers-color-scheme: dark)").matches) {
    $("html").removeClass("dark");
    dark_mode = false;
}

if (isMobileDevice()) {
    $(".darkmode-switch").on("click", () => $("html").toggleClass("dark"));
} else {
    initParticles();
    $(".darkmode-switch").on("click", function () {
        $("html").toggleClass("dark");
        dark_mode = !dark_mode;
        initParticles();
    });
}

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
