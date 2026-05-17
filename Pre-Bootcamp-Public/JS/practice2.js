// ==========================================
// Practice I: Variables and Basic Operations
// ==========================================

// 1. Declare a variable favoriteAnimal and assign it your favorite animal. Print the value.
let favoriteAnimal = "Lion"; 
console.log(`Favorite Animal: ${favoriteAnimal}`);

// 2. Declare two variables a and b, assign them numbers, and print their sum.
let a = 10;
let b = 20;
console.log(`Sum of a and b: ${a + b}`);

// 3. Create a variable age and assign your age. Print a message like: "I am 25 years old."
let age = 22; 
console.log(`Age Message: I am ${age} years old.`);

// 4. Declare a variable country with a value of your favorite country. Change its value to another country and print it.
let country = "Palestine";
country = "Egypt"; 
console.log(`Updated Country: ${country}`);

// 5. Use const to declare a variable for the value of pi (3.14) and print it.
const pi = 3.14;
console.log(`Value of PI: ${pi}`);

// 6. Create a variable named favoriteColor and assign your favorite color to it. Print the value.
let favoriteColor = "Blue";
console.log(`Favorite Color: ${favoriteColor}`);

// 7. Create a variable named x with the value 5 and another variable y with the value 10. Print their sum.
let x = 5;
let y = 10;
console.log(`Sum of x and y: ${x + y}`);

// 8. Declare a variable isSunny and set it to true. Print a message like: "It is sunny today."
let isSunny = true;
if (isSunny) {
    console.log("Weather Status: It is sunny today.");
}


// ==========================================
// Practice II: Conditional Statements (if-else)
// ==========================================

// 1. Write a program that checks if a number is positive or negative.
let number = 5; 
if (number > 0) {
    console.log(`The number ${number} is positive.`);
} else if (number < 0) {
    console.log(`The number ${number} is negative.`);
} else {
    console.log("The number is zero.");
}

// 2. Write a program that prints "Good morning" if the time is less than 12 and "Good afternoon" otherwise.
let time = 10; 
if (time < 12) {
    console.log("Time-based greeting: Good morning");
} else {
    console.log("Time-based greeting: Good afternoon");
}

// 3. Write a program that assigns grades based on scores.
let score = 85; 
if (score >= 90) {
    console.log("Grade: A");
} else if (score >= 80) { // تبسيط الشرط تلقائياً لأن ما فوق 90 تم تجميعه بالفعل أعلاه
    console.log("Grade: B");
} else if (score >= 70) {
    console.log("Grade: C");
} else {
    console.log("Grade: F");
}

// 4. Write a program that takes a day of the week and prints whether it's a weekday or weekend.
let day = "Friday"; 
let normalizedDay = day.toLowerCase(); 

if (normalizedDay === "friday" || normalizedDay === "saturday") {
    console.log(`${day} is a weekend.`);
} else {
    console.log(`${day} is a weekday.`);
}