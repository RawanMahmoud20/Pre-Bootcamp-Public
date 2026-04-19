// Hero
const heroBtn = document.getElementById('heroBtn');
const heroImg = document.getElementById('heroImg');
let heroChange = false;

heroBtn.addEventListener('click', function () {
    heroBtn.style.display = 'none';
});

heroImg.addEventListener('click', function () {
    if (!heroChange) {
        heroImg.src = './WebFund/blue-super-car.png';
    } else {
        heroImg.src = './WebFund/bluecar.png';

    }
    heroChange = !heroChange;
});

// Book Now
const bookButton = document.querySelectorAll('.book-btn');
bookButton.forEach(function (btn) {
    btn.addEventListener('click', function () {
        const card = this.closest('.service-card');
        const countElement = card.querySelector('.count');
        let count = parseInt(countElement.innerText);
        if (count > 0) {
            countElement.innerText = count - 1;
        } else {
            alert("No appintment left!");
        }
    });
});
//  Read more 
const readMoreBtn = document.getElementById('readMoreBtn');
const reviewText = document.getElementById('reviewText');
const rewiewImg = document.getElementById('rewiewImg');
let expanded = false;

const review1 = `My Eexperience at the car  Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
anim idest laborum.` ;

const review2 = `I had a great experanice  at the car  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat.`

readMoreBtn.addEventListener('click', function () {
    reviewText.style.opacity = '0';
    setTimeout(() => {
        reviewText.textContent = !expanded ? review2 : review1;
        rewiewImg.src = !expanded ? './WebFund/unstisfied.png' : './WebFund/client.png';
        readMoreBtn.textContent = !expanded ? 'Show less' : 'Read more';
        expanded = !expanded;
        reviewText.style.opacity = '1';
        reviewText.classList.add('fade-in');
        setTimeout(() => reviewText.classList.remove('fade-in'), 600);
    }, 300);
});