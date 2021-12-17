window.addEventListener("DOMContentLoaded", startFlow);

function startFlow() {
    let recordButton = document.getElementById("toggle-record");
    let historyButton = document.getElementById("toggle-history");

    recordButton.addEventListener("click", showRecord);
    historyButton.addEventListener("click", showHistory);
}

function showHistory() {
    document.querySelector(".intro").setAttribute("data-visible", "false");
    document.querySelector(".record").setAttribute("data-visible", "false");
    document.querySelector(".history").setAttribute("data-visible", "true");
}

function showRecord() {
    document.querySelector(".intro").setAttribute("data-visible", "false");
    document.querySelector(".history").setAttribute("data-visible", "false");
    document.querySelector(".record").setAttribute("data-visible", "true");
}

function revert() {
    document.querySelector(".intro").setAttribute("data-visible", "true");
    document.querySelector(".history").setAttribute("data-visible", "false");
    document.querySelector(".record").setAttribute("data-visible", "false"); 
}