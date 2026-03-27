
// let likesArray = [9, 12, 9];

// function addLike(index) {

//     likesArray[index]+=1;

// let allCounters = document.querySelectorAll(".likes-counter");
// allCounters[index].innerText = likesArray[index];
// }

function addLike(elem){
    // get the post card element that contains the like button that was clicked
    let postCard = elem.closest(".post-card");
  // get the counter element within that post card
    let counter = postCard.querySelector(".likes-counter");
   // get the current number of likes from the counter, increment it, and update the counter's text
    let currentLikes = Number(counter.innerText);
    // increment the likes count
    currentLikes++;
    // update the counter's text with the new likes count
    counter.innerText = currentLikes;
}