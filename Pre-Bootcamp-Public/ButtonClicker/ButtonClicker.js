
// 1. Change text from Login to Logout
function toggleLogin(element) {
    if (element.innerText == "Login") {
        element.innerText = "Logout";
    } else {
        element.innerText = "Login";
    }
}

// 2. Remove the "Add Definition" button
function removeBtn(element) {
    element.remove();
}

// 3. Alert when a like button is clicked
function alertLike() {
    alert("Ninja was liked");
}