function example(element) {
    console.log("element clicked", element);
};

function turnOff(element) {
    element.innerText += "can change - Turned Off";
};

function hide(element) {
    element.remove();
}

let taco1 = {
    tortilla: "corn",
    protein: "chicken",
    cheese: "cheddar",
    toppings: ["lettuce", "tomato"],
   tacoInfo: function() {
  console.log("Tortilla: " + this.tortilla);
  console.log("Protein: " + this.protein);
  console.log("Cheese: " + this.cheese);
  console.log("Toppings: " + this.toppings);
}
};
taco1.tacoInfo();
console.log(taco1);

//
function clicked(elem) {
  elem.style.fontSize = "44px";
}

var person = {
  name: "Rawan", //string
  age: 23, // number
  getInfo: function () {
    //function
    return "My name is " + this.name + " I am " + this.age + " years old.";
  },
};

var darkTheme = {
  backgroundColor: "black",
  color: "white",
};

function userInfo(elem) {
  elem.innerText = person.getInfo();
}

function darkMode(elem) {
  elem.style.backgroundColor = darkTheme.backgroundColor;
  elem.style.color = darkTheme.color;
}