// Theme 
const moonIcon = document.getElementById('theme-icon-moon');
const sunIcon = document.getElementById('theme-icon-sun');
moonIcon.addEventListener('click', toggleTheme);
sunIcon.addEventListener('click', toggleTheme);
document.addEventListener("DOMContentLoaded", () => {
    local = localStorage.getItem("theme");
    if (local == "dark") {
        document.body.classList.add("darkMode");
    } else {
        document.body.classList.remove("darkMode");
    }
})
function toggleTheme() {
    document.body.classList.toggle('darkMode');
    if (document.body.classList == 'darkMode') {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
}
// finish Theme part 
