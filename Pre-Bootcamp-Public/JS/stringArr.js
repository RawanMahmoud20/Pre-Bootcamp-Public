// =================================================================
// STRINGS TO DO 2: String Basic Functions
// =================================================================

// 1. Reverse String
// Task: Reverse a string without using the built-in .reverse() method.
function reverseString(str) {
    let reversed = "";
    // Loop backwards from the last character to the first
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    return reversed;
}

// Testing Task 1
console.log("Reversed 'creature':", reverseString("creature")); // Output: "erutaerc"


// 2. Remove Even-Length Strings
// Task: Remove even-length strings from an array in-place.
function removeEvenLengthStrings(arr) {
    // Loop backwards to safely remove elements without messing up the array indices
    for (let i = arr.length - 1; i >= 0; i--) {
        if (arr[i].length % 2 === 0) {
            arr.splice(i, 1); // Removes 1 element at index i
        }
    }
    return arr;
}

// Testing Task 2
let stringArr = ["Nope!", "Its", "Kris", "starting", "with", "K!", "(instead", "of", "Chris", "with", "C)", "."];
removeEvenLengthStrings(stringArr);
console.log("Filtered Array:", stringArr); // Output: ["Nope!", "Its", "Chris", "."]


// 3. Integer to Roman Numerals
// Task: Convert a positive integer (less than 4000) into its Roman numeral representation.
function intToRoman(num) {
    // Lookup table matching decimal values to Roman symbols sorted from highest to lowest
    const romanMatrix = [
        [1000, 'M'],  [900, 'CM'],  [500, 'D'],  [400, 'CD'],
        [100, 'C'],   [90, 'XC'],   [50, 'L'],   [40, 'XL'],
        [10, 'X'],    [9, 'IX'],    [5, 'V'],    [4, 'IV'],
        [1, 'I']
    ];
    
    let result = "";
    
    for (let i = 0; i < romanMatrix.length; i++) {
        let value = romanMatrix[i][0];
        let symbol = romanMatrix[i][1];
        
        // Append the symbol while num is greater than or equal to its value
        while (num >= value) {
            result += symbol;
            num -= value;
        }
    }
    return result;
}

// Testing Task 3
console.log("349 to Roman:", intToRoman(349)); // Output: "CCCIL" (or "CCCXLIX" depending on strict standard variant)
console.log("444 to Roman:", intToRoman(444)); // Output: "CDXLIV"


// 4. Roman Numerals to Integer
// Task: Convert a Roman numeral string into its corresponding integer value.
function romanToInt(roman) {
    const romanSymbols = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    };
    
    
    let total = 0;
    
    for (let i = 0; i < roman.length; i++) {
        let currentVal = romanSymbols[roman[i]];
        let nextVal = romanSymbols[roman[i + 1]];
        
        // If current value is less than the next one, subtract it (e.g., IV = 5 - 1 = 4)
        if (nextVal > currentVal) {
            total -= currentVal;
        } else {
            total += currentVal;
        }
    }
    return total;
}

// Testing Task 4
console.log("III to Int:", romanToInt("III"));     // Output: 3
console.log("DCIX to Int:", romanToInt("DCIX"));   // Output: 609
console.log("MXDII to Int:", romanToInt("MXDII")); // Output: 1492


// =================================================================
// PRACTICE I: Variables and Basic Operations
// =================================================================

let favoriteAnimal = "Lion"; 
console.log("Favorite Animal:", favoriteAnimal);

let a = 10;
let b = 20;
console.log("Sum of a and b:", a + b);

let age = 22; 
console.log("Age Message: I am " + age + " years old.");

let country = "Palestine";
country = "Egypt"; 
console.log("Updated Country:", country);

const pi = 3.14;
console.log("Value of PI:", pi);

let favoriteColor = "Blue";
console.log("Favorite Color:", favoriteColor);

let x = 5;
let y = 10;
console.log("Sum of x and y:", x + y);

let isSunny = true;
if (isSunny) {
    console.log("Weather Status: It is sunny today.");
}


// =================================================================
// PRACTICE II: Conditional Statements (if-else)
// =================================================================

let number = 5; 
if (number > 0) {
    console.log("The number " + number + " is positive.");
} else if (number < 0) {
    console.log("The number " + number + " is negative.");
} else {
    console.log("The number is zero.");
}

let time = 10; 
if (time < 12) {
    console.log("Time-based greeting: Good morning");
} else {
    console.log("Time-based greeting: Good afternoon");
}

let score = 85; 
if (score >= 90) {
    console.log("Grade: A");
} else if (score >= 80 && score <= 89) {
    console.log("Grade: B");
} else if (score >= 70 && score <= 79) {
    console.log("Grade: C");
} else {
    console.log("Grade: F");
}

let day = "Friday"; 
day = day.toLowerCase(); 
if (day === "friday" || day === "saturday") {
    console.log(day + " is a weekend.");
} else {
    console.log(day + " is a weekday.");
}