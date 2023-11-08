document.addEventListener("DOMContentLoaded", function () {
    const bannerContainer = document.getElementById("banner-container");
    const intervalInput = document.getElementById("interval");
    let currentIndex = 0;
    let intervalId;

    function changeBanner() {
        const banners = bannerContainer.getElementsByClassName("ads");
        banners[currentIndex].style.display = "none";
        currentIndex = (currentIndex + 1) % banners.length;
        banners[currentIndex].style.display = "block";
    }

    function startRotation() {
        const interval = (intervalInput != null ? parseInt(intervalInput.value) : 2) * 1000;
        if (isNaN(interval) || interval <= 0) {
            alert("Пожалуйста, введите корректный интервал (в секундах).");
            return;
        }

        if (intervalId) {
            clearInterval(intervalId);
        }

        intervalId = setInterval(changeBanner, interval);
    }

    function stopRotation() {
        if (intervalId) {
            clearInterval(intervalId);
            intervalId = null;
        }
    }

    if (intervalInput != null) {
        intervalInput.addEventListener("change", function () {
            if (intervalId) {
                stopRotation();
                startRotation();
            }
        });
    }

    window.addEventListener("focus", startRotation);
    window.addEventListener("blur", stopRotation);

    startRotation();
});
