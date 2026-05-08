document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const button = document.querySelector("button");

    if (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();
            alert("Form submitted successfully!");
        });
    }

    if (button) {
        button.addEventListener("click", function () {
            console.log("Button clicked!");
        });
    }
});
