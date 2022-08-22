$(function () {
    // Initialize the AOS library
    AOS.init();

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

    let copy_btn = $("#copy-btn");
    copy_btn.on("click", function () {
        navigator.clipboard.writeText($("#command").text());
        $("#copy-msg").html("Copied to clipboard!");
        setTimeout(function () {
            $("#copy-msg").html("");
        }, 3000);
    });

    $("#loading-msg").addClass("loaded");
    setTimeout(function () {
        $("#loading-msg").hide();
    }, 1000);

    // Confetti animation
    var skew = 1;
    var duration = 10 * 1000;
    var animationEnd = Date.now() + duration;

    var canvas = document.getElementById("banner");
    canvas.confetti =
        canvas.confetti || confetti.create(canvas, { resize: true });

    function randomInRange(min, max) {
        return Math.random() * (max - min) + min;
    }

    (function frame() {
        var timeLeft = animationEnd - Date.now();
        var ticks = Math.max(200, 500 * (timeLeft / duration));
        skew = Math.max(0.8, skew - 0.001);

        canvas.confetti({
            particleCount: 1,
            startVelocity: 0,
            ticks: ticks,
            origin: {
                x: Math.random(),
                // since particles fall down, skew start toward the top
                y: Math.random() * skew - 0.2,
            },
            colors: ["#ff005d"],
            shapes: ["circle"],
            gravity: randomInRange(0.2, 0.4),
            scalar: randomInRange(0.4, 1),
            drift: randomInRange(-0.4, 0.4),
        });

        if (timeLeft > 0) {
            requestAnimationFrame(frame);
        }
    })();

    // Initialize the Asciinema player
    AsciinemaPlayer.create(
        "/static/file/demo.cast",
        document.getElementById("demo"),
        {
            rows: 18,
            preload: true,
            autoplay: true,
            theme: "asciinema",
        }
    );
});
