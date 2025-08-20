// script.js

// Run code after DOM loads
document.addEventListener("DOMContentLoaded", () => {
    console.log("JS Loaded Successfully ✅");

    // Select the second h1 (insert_data)
    const dataHeading = document.querySelectorAll("h1")[1];

    // Change its color every 2 seconds
    const colors = ["#22d3ee", "#a78bfa", "#f59e0b", "#ef4444"];
    let i = 0;

    setInterval(() => {
        dataHeading.style.color = colors[i % colors.length];
        i++;
    }, 2000);

    // Add a small click interaction
    dataHeading.addEventListener("click", () => {
        alert("You clicked on: " + dataHeading.innerText);
    });
});
