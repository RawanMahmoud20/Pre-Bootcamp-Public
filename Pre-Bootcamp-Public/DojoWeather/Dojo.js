// alert the user when they click on a city name
function loading() {
    alert("Loading weather report...");
}

// delete the cookie message when the user clicks "I Accept"
function acceptCookies() {
    var element = document.querySelector("#cookie-box");
    element.remove();
}

// convert temperature from Celsius to Fahrenheit and vice versa
function convertTemp(element) {
    var temps = document.querySelectorAll(".high, .low");
    
    for (var i = 0; i < temps.length; i++) {
        var tempVal = parseInt(temps[i].innerText);
        if (element.value == "f") {
          // convert C to F using the formula F = (C * 9/5) + 32
            temps[i].innerText = Math.round((tempVal * 9/5) + 32);
        } else {
           // convert F to C using the formula C = (F - 32) * 5/9
            temps[i].innerText = Math.round((tempVal - 32) * 5/9);
        }
    }
}