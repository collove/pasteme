$(function () {
  // Body has this property by default, this is used to block user from
  // scrolling the page while the loading screen is active.
  $("body").removeClass("overflow-hidden");

  // This class moves the element out of the viewport by "slide-out"
  // animation defined in the CSS file. @extra.css
  $("#loading-msg").addClass("loaded");

  // removes the loading screen after 1 second, if we omit this step
  // the loading screen will be visible while taking screenshots
  // because the "loaded" class will only add the "slide-out"
  // animation to the element which translates it's Y-position and not
  // hiding the element completely.
  setTimeout(function () {
    $("#loading-msg").hide();
  }, 1000); // I wait for 1 second to make sure the loading screen is fully out of view
});
