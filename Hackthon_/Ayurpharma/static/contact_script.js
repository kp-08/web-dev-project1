document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById("contactForm");

    contactForm.addEventListener("submit", function (event) {
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;

        if (name === "" || email === "" || message === "") {
            alert("Please fill in all fields.");
            event.preventDefault();
        } else if (!isValidEmail(email)) {
            alert("Please enter a valid email address.");
            event.preventDefault();
        }
    });

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
});
 