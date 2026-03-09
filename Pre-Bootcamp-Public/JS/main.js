// Loop from 1 to 100
for (let index = 1; index < 100; index++) {
    // Check if multiple of both 3 and 5 first
    if (index % 3 === 0 && index % 5 === 0) {
        console.log("FizzBuzz");
    }
    // Check if multiple of 3 
    else if (index % 3 === 0) {
        console.log("Fizz");
    }
    // Check if multiple of 5
    else if (index % 5 === 0) {
        console.log("Buzz");
    }
    // Otherwise, just print the number 
    else {
        console.log(index);
    }
}