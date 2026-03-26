

// choose elements from page
const likeButton = document.querySelector("#like-btn");
const likeCountElement = document.querySelector("#like-count");

// initialize the number of likes
let likeCount = 0;
likeCountElement.innerText = likeCount;

likeButton.onclick = function() {
    // extract the current number and convert it to an integer
    let currentLikes = parseInt(likeCountElement.innerText);

    // increment the number by 1
    currentLikes++;

    // update the text inside the element with the new number
    likeCountElement.innerText = currentLikes;
};