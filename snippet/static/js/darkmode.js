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

localStorage.theme = dark_mode ? "dark" : "light";
