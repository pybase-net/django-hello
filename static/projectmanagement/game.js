document.addEventListener('DOMContentLoaded', function () {
    console.log("Game page loaded");
    const firstCarouselItem = document.querySelector('#quizCarousel .carousel-item');
    firstCarouselItem.classList.add('active');
    // Your JavaScript code here

    document.querySelectorAll('.next-slide').forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const carousel = document.getElementById('quizCarousel');
            const carouselInstance = bootstrap.Carousel.getInstance(carousel);
            carouselInstance.next();
        });
    });

    document.querySelectorAll('.prev-slide').forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const carousel = document.getElementById('quizCarousel');
            const carouselInstance = bootstrap.Carousel.getInstance(carousel);
            carouselInstance.prev();
        });
    });

    // Countdown Timer
    let countdownElement = document.getElementById('game_remaining_time');
    let remainingTime = parseInt(countdownElement.getAttribute('data-remaining-time'), 10);

    function updateCountdown() {
        remainingTime--;

        // Update the display text
        countdownElement.textContent = `Remaining Time: (${remainingTime}) second${remainingTime !== 1 ? 's' : ''}`;

        // If the remaining time is zero, stop the countdown
        if (remainingTime <= 0) {
            clearInterval(countdownInterval);
            countdownElement.textContent = 'Time is up!';
        }
    }

    let countdownInterval = setInterval(updateCountdown, 1000);
    updateCountdown();
});


