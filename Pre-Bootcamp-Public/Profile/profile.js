// ===============================
// Edit Profile Function
// ===============================
const editBtn = document.querySelector(".editProfile");
const nameElement = document.querySelector(".name");

editBtn.addEventListener("click", function() {
    // Requirements say: change the user's name to any other name
    if (nameElement.innerText === "Rawan Mahmoud") {
        nameElement.innerText = "Jane Doe";
        editBtn.innerText = "Reset Name"; // Optional flair
    } else {
        nameElement.innerText = "Rawan Mahmoud";
        editBtn.innerText = "Edit Profile";
    }
});

// ===============================
// Handle Connection Requests
// ===============================
function handleRequest(element, isAccepted) {
// 1. Remove the user from the requests list
    const requestItem = element.closest('.connection-item');
    requestItem.remove();

    // 2. Decrease the "Connection Requests" number
    const requestCount = document.querySelector("#request-count");
    let currentRequests = parseInt(requestCount.innerText);
    requestCount.innerText = currentRequests - 1;

    // 3. Bonus: if accepted, increase "Your Connections" number
    if (isAccepted) {
        const totalConn = document.querySelector("#total-connections");
        // We parse the text. If it says "50+", we treat it as 50.
        let currentTotal = parseInt(totalConn.innerText);
        totalConn.innerText = currentTotal + 1;
    }
}
// Attach listeners to ALL request buttons (Accept and Decline)
document.querySelectorAll('.action-yes').forEach(btn => {
    btn.addEventListener('click', function() {
        handleRequest(this, true);
    });
});

document.querySelectorAll('.action-no').forEach(btn => {
    btn.addEventListener('click', function() {
        handleRequest(this, false);
    });
});