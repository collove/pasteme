$(function () {
    // hides the loading screen
    $("body").removeClass("overflow-hidden");
    $("#loading-msg").addClass("loaded");

    // removes the loading screen after 1 second
    setTimeout(function () {
        $("#loading-msg").hide();
    }, 1000);
});
