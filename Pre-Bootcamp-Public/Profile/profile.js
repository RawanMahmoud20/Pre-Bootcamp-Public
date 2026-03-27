// ===============================
// Edit Profile Function
// ===============================
function toggleEditProfile(button) {

    const nameElement = document.querySelector(".name");

    if (button.innerText === "Edit Profile") {
        button.innerText = "Cancel";
        nameElement.innerText = "Any Other Name";
    } else {
        button.innerText = "Edit Profile";
        nameElement.innerText = "Rawan Mahmoud";
    }
}


// ===============================
// Handle Connection Requests
// ===============================
function handleRequest(element, isAccepted) {

    // Remove request card
    const requestItem = element.closest('.connection-item');
    requestItem.remove();

    // Update request counter
    const requestCount = document.querySelector("#request-count");
    let currentRequests = parseInt(requestCount.innerText);
    requestCount.innerText = currentRequests - 1;

    // If accepted → increase total connections
    if (isAccepted) {
        const totalConn = document.querySelector("#total-connections");
        let currentTotal = parseInt(totalConn.innerText);
        totalConn.innerText = currentTotal + 1;
    }
}