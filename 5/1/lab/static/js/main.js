document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener("scroll", function () {
        var scrollTop = window.scrollY || document.documentElement.scrollTop;
        var windowHeight = window.innerHeight;
        var scrollTrigger = windowHeight * 0.15;
        var duration = 1.5;
        if (scrollTop > scrollTrigger) {
            gsap.to("#image1", { opacity: 0, duration: duration });
            gsap.to("#image2", { opacity: 0, duration: duration });
        } else {
            gsap.to("#image1", { opacity: 1, duration: duration });
            gsap.to("#image2", { opacity: 1, duration: duration });
        }
    });
});

const cards = document.querySelectorAll(".paralax");

cards.forEach(
    card_w => {

        const card = card_w.querySelector(".partner-icon");

        card_w.addEventListener('mousemove', event => {
            const [x, y] = [event.offsetX, event.offsetY];
            const rect = card_w.getBoundingClientRect();
            const [width, height] = [rect.width, rect.height];
            const middleX = width / 2;
            const middleY = height / 2;
            const offsetX = ((x - middleX) / middleX) * 25;
            const offsetY = ((y - middleY) / middleY) * 25;
            const offX = 50 + ((x - middleX) / middleX) * 25;
            const offY = 50 - ((y - middleY) / middleY) * 20;
            card.style.setProperty("--rotateX", 2 * offsetX + "deg");
            card.style.setProperty("--rotateY", -2 * offsetY + "deg");
            card.style.setProperty("--posx", offX + "%");
            card.style.setProperty("--posy", offY + "%");
        });
        card_w.addEventListener('mouseleave', eve => {

            card.style.animation = 'reset-card 0.5s ease';
            card.addEventListener("animationend", e => {
                card.style.animation = 'unset';
                card.style.setProperty("--rotateX", "0deg");
                card.style.setProperty("--rotateY", "0deg");
                card.style.setProperty("--posx", "50%");
                card.style.setProperty("--posy", "50%");
            }, {
                once: true
            });
        });
    });

document.addEventListener("DOMContentLoaded", function () {
    var startTime = localStorage.getItem("countdownStartTime");
    if (startTime === null) {
        startTime = new Date().getTime();
        localStorage.setItem("countdownStartTime", startTime);
    }
    var countdownHours = 1;
    var countdownElement = document.getElementById("countdown");
    function updateCountdown() {
        var currentTime = new Date().getTime();
        var elapsedTime = currentTime - startTime;
        var remainingTime = countdownHours * 60 * 60 * 1000 - elapsedTime;
        if (remainingTime <= 0) {
            countdownElement.innerHTML = "Отсчет завершен!";
            localStorage.removeItem("countdownStartTime");
        } else {
            var hours = Math.floor(remainingTime / 3600000);
            var minutes = Math.floor((remainingTime % 3600000) / 60000);
            var seconds = Math.floor((remainingTime % 60000) / 1000);
            countdownElement.innerHTML = `Осталось времени: ${hours} часов, ${minutes} минут, ${seconds} секунд`;
        }
    }
    updateCountdown();
    setInterval(updateCountdown, 1000);
});

document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("birthday-form");
    var ageMessage = document.getElementById("age-message");
    var dayOfWeek = document.getElementById("day-of-week");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        var birthdate = new Date(document.getElementById("birthdate").value);
        var now = new Date();
        var age = now.getFullYear() - birthdate.getFullYear();
        if (now.getMonth() < birthdate.getMonth() ||
            (now.getMonth() === birthdate.getMonth() && now.getDate() < birthdate.getDate())) {
            age--;
        }
        if (age >= 18) {
            alert(`Вы совершеннолетний.\nДень недели вашего дня рождения: ${getDayOfWeek(birthdate)}`);
        } else {
            confirm(`Вы несовершеннолетний. Требуется разрешение родителей.\nДень недели вашего дня рождения: ${getDayOfWeek(birthdate)}`);
        }
    });
    function getDayOfWeek(date) {
        var daysOfWeek = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
        return daysOfWeek[date.getDay()];
    }
});

class Exhibit {
    constructor(name, description) {
        this.name = name;
        this.description = description;
    }

    displayInfo() {
        return `${this.name}: ${this.description}`;
    }
}

class Painting extends Exhibit {
    constructor(name, description, artist, style) {
        super(name, description);
        this.artist = artist;
        this.style = style;
    }

    get paintingStyle() {
        return this.style;
    }

    set paintingStyle(newStyle) {
        this.style = newStyle;
    }
}

function rateDecorator(painting, rating) {
    painting.rating = rating;
    const displayInfo = painting.displayInfo.bind(painting);
    painting.displayInfo = function () {
        return `${displayInfo()} (Rating: ${this.rating})`;
    };
}

const starryNight = new Painting('Starry Night', 'Impressionist masterpiece', 'Vincent van Gogh', 'Post-Impressionism');
rateDecorator(starryNight, 4);

console.log(starryNight.displayInfo());

function Exhibit(name, description) {
    this.name = name;
    this.description = description;
}

Exhibit.prototype.displayInfo = function () {
    return `${this.name}: ${this.description}`;
};

function Painting(name, description, artist, style) {
    Exhibit.call(this, name, description);
    this.artist = artist;
    this.style = style;
}

Painting.prototype = Object.create(Exhibit.prototype);

Object.defineProperty(Painting.prototype, 'paintingStyle', {
    get: function () {
        return this.style;
    },
    set: function (newStyle) {
        this.style = newStyle;
    }
});

function rateDecorator(painting, rating) {
    painting.rating = rating;
    painting.displayInfo = function () {
        return `${Exhibit.prototype.displayInfo.call(this)} (Rating: ${this.rating})`;
    };
}

const monaLisa = new Painting('Mona Lisa', 'Famous portrait', 'Leonardo da Vinci', 'Renaissance');
rateDecorator(monaLisa, 5);

console.log(monaLisa.displayInfo());
