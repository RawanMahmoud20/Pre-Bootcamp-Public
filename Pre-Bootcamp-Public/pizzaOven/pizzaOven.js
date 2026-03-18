// pizzaOven 
function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

// Creating your first two pizzas
var p1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
var p2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);


console.log("Pizza 1:", p1);
console.log("Pizza 2:", p2);


// randomPizza

var crusts = ["deep dish", "hand tossed", "thin and crispy", "cauliflower"];
var sauces = ["traditional", "marinara", "white sauce", "pesto"];
var cheeseOptions = ["mozzarella", "feta", "cheddar", "no cheese"];
var toppingOptions = ["pepperoni", "sausage", "mushrooms", "olives", "onions", "pineapple"];

function randomPizza() {
    // Helper function to get a random element from an array
    function getRandom(arr) {
        var index = Math.floor(Math.random() * arr.length);
        return arr[index];
    }

    // "Bake" the random pizza using our existing pizzaOven function
    return pizzaOven(
        getRandom(crusts),
        getRandom(sauces),
        [getRandom(cheeseOptions)], // Wrapped in array as per requirements
        [getRandom(toppingOptions), getRandom(toppingOptions)] // Picks two toppings
    );
}

console.log( "Random Pizza:", randomPizza());