$(function () {
  if (localStorage.show_modal === "true") {
    console.log("show modal");
    // This property is active on the body element by default, this is
    // used to block user from scrolling the page while the modal is
    // active. It gets removed when the loading screen is removed, so I
    // need to add it back. @loading.js
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
          loop: true,
          speed: 2,
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

  // If a modal is being shown to the user, it has a X button that
  // can be used to close the modal.
  $("#modal-close").on("click", function () {
    $("#modal").hide();

    // Make page scrollable again.
    $("body").removeClass("overflow-hidden");

    // Save this preference to the storage that modal doesn't show
    // again. (if there be a new modal to show, it will be shown because
    // the modal_id is also saved in storage @home.html in the inline scripts)
    localStorage.show_modal = 'false';

    // If a modal is being shown, all other background animations are
    // blocked until the user closes the modal. I need to play them when
    // the modal is closed.
    play_page_animations();
  });

  if (localStorage.show_modal === "false") {
    // Hide the modal element if the user has already closed it.
    $("#modal").hide();
    play_page_animations();
  }
});
