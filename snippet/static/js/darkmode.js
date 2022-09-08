// This is the very first file (scripts) that is executed when the page
// is loading. It is used to determine if the user prefers dark mode or
// not. If yes, it will add the "dark" class to the html element.
(function () {
  let dark_mode = true;
  let html_element = document.getElementsByTagName("html")[0];

  // Disable dark mode if the user's device is not set to dark mode
  if (
    localStorage.theme === "dark" ||
    (!("theme" in localStorage) &&
      window.matchMedia("(prefers-color-scheme: dark)").matches)
  ) {
    html_element.classList.add("dark");
  } else {
    html_element.classList.remove("dark");
    dark_mode = false;
  }

  // the value will be saved for future visits
  localStorage.theme = dark_mode ? "dark" : "light";
})();
