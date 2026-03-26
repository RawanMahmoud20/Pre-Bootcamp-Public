// Array to store the like counts for each post
let likesArray = [9, 12, 9];

function addLike(index) {
// Increment the value in the array for the clicked post
    likesArray[index]+=1;

let allCounters = document.querySelectorAll(".likes-counter");
// Update the text of the specific counter element with the new value   
allCounters[index].innerText = likesArray[index];
}