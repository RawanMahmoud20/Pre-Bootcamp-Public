
const heroSection = document.querySelector(".hero");
heroSection.addEventListener('mouseover', function () {
    this.style.backgroundColor ='#3b4598';
    this.style.Color ='white';

});
heroSection.addEventListener('mouseout', function () {
    this.style.backgroundColor ='transparent';
    this.style.Color ='black';
});
// 
const mainBtn = document.querySelector(".hero button");
const heroTitle = document.querySelector(".hero h1");
const heroImg = document.querySelector(".hero img");

let isChange = false;

mainBtn.addEventListener('click' , function (){
    if (isChange){
      heroTitle.innerText = "what we do";
      heroImg.src= "./img/alt-features.png";  
      this.innerText = "Change Back";
    }else{
        heroTitle.innerText = "We offer modern solutions for growing your business";
        heroImg.src= "./img/about.jpg";  
        this.innerText = "Get Started";
    }
    isChange =  !isChange ;
});
// 
const addServiceBtn = document.querySelector(".service-header button");
const serviceCardContainer = document.querySelector(".service-card ");

addServiceBtn.addEventListener('click' , function () {
    const newCard = document.createElement ('div');
    newCard.className= 'card';

    newCard.innerHTML = ` 
     <img src="./img/features.png" alt="features">
    <p> This is a new service card added dynamically with img and paragraph  </p>
     `;
    serviceCardContainer.appendChild (newCard);

});


