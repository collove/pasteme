$(function () {
  if (sessionStorage.getItem("show-modal") === "true") {
    $("body").addClass("overflow-hidden");
  }

  let copy_btn = $("#copy-btn");
  copy_btn.on("click", function () {
    navigator.clipboard.writeText($("#command").text());
    $("#copy-msg").html("Copied to clipboard!");
    setTimeout(function () {
      $("#copy-msg").html("");
    }, 3000);
  });

  function play_page_animations() {
    // Initialize the Asciinema player
    try {
      AsciinemaPlayer.create(
        "/static/file/demo.cast",
        document.getElementById("demo"),
        {
          rows: 18,
          preload: true,
          autoplay: true,
          idleTimeLimit: 1,
          theme: "asciinema",
        }
      );
    } catch (error) {}

    // Confetti animation
    let skew = 1;
    let duration = 10 * 1000;
    let animationEnd = Date.now() + duration;

    let canvas = document.getElementById("banner");

    if (canvas) {
      canvas.confetti =
        canvas.confetti || confetti.create(canvas, { resize: true });

      function randomInRange(min, max) {
        return Math.random() * (max - min) + min;
      }

      (function frame() {
        let timeLeft = animationEnd - Date.now();
        let ticks = Math.max(200, 500 * (timeLeft / duration));
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
          shapes: ["triangle"],
          gravity: randomInRange(0.3, 0.4),
          scalar: randomInRange(0.4, 1),
          drift: randomInRange(-0.4, 0.4),
        });

        if (timeLeft > 0) {
          requestAnimationFrame(frame);
        }
      })();
    }
  }

  $("#modal-close").on("click", function () {
    console.log("close");
    $("#modal").hide();
    $("body").removeClass("overflow-hidden");
    sessionStorage.setItem("show-modal", "false");
    play_page_animations();
  });

  if (sessionStorage.getItem("show-modal") === "false") {
    $("#modal").hide();
    play_page_animations();
  }
});
