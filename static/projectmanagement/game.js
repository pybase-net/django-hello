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
});


