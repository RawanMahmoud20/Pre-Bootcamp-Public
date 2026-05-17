// =================================================================
// 1. Always Hungry
// =================================================================
function alwaysHungry(arr) {
    let foundFood = false;
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === "food") {
            console.log("yummy");
            foundFood = true;
        }
    }
    
    if (!foundFood) {
        console.log("I'm hungry");
    }
}

// Testing Challenge 1
alwaysHungry([3.14, "food", "pie", true, "food"]); // Output: "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2]);                   // Output: "I'm hungry"


// =================================================================
// 2. High Pass Filter
// =================================================================
function highPass(arr, cutoff) {
    var filteredArr = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]); // Adds value to the new array if it's greater than cutoff
        }
    }
    
    return filteredArr;
}

// Testing Challenge 2
var result2 = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result2); // Output: [6, 8, 10, 9]


// =================================================================
// 3. Better than average
// =================================================================
function betterThanAverage(arr) {
    var sum = 0;
    // Step 1: Calculate the sum of all numbers
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    
    // Step 2: Calculate the average
    var average = sum / arr.length;
    
    var count = 0;
    // Step 3: Count how many values are greater than the average
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > average) {
            count++;
        }
    }
    
    return count;
}

// Testing Challenge 3
var result3 = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result3); // Output: 4


// =================================================================
// 4. Array Reverse
// =================================================================
function reverse(arr) {
    let left = 0;
    let right = arr.length - 1;
    
    // Swap elements from outside moving inward
    while (left < right) {
        let temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        
        left++;
        right--;
    }
    
    return arr;
}

// Testing Challenge 4
var result4 = reverse(["a", "b", "c", "d", "e"]);
console.log(result4); // Output: ["e", "d", "c", "b", "a"]


// =================================================================
// 5. Fibonacci Array
// =================================================================
function fibonacciArray(n) {
    // The [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    
    // Loop starts from index 2 up to the desired length 'n'
    while (fibArr.length < n) {
        let nextFib = fibArr[fibArr.length - 1] + fibArr[fibArr.length - 2];
        fibArr.push(nextFib); // Add the sum of the last two elements
    }
    
    return fibArr;
}

// Testing Challenge 5
var result5 = fibonacciArray(10);
console.log(result5); // Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]