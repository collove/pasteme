let dark_mode = true;

// Disable dark mode if the user's device is not set to dark mode
if (
    localStorage.theme === "dark" ||
    (!("theme" in localStorage) &&
        window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
    $("html").addClass("dark");
} else {
    $("html").removeClass("dark");
    dark_mode = false;
}

localStorage.theme = dark_mode ? "dark" : "light";
