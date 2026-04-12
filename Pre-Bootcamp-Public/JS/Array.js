// 1. Always Hungry
function alwaysHungry(arr) {
    var foodFound = false; // Flag to track if "food" exists in the array
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] === "food") {
            console.log("yummy"); // Log "yummy" every time "food" is encountered
            foodFound = true;
        }
    }
    // If no "food" was found after checking the entire array, log "I'm hungry" once
    if (!foodFound) {
        console.log("I'm hungry");
    }
}

// 2. High Pass Filter
function highPass(arr, cutoff) {
    var filteredArr = []; // New array to store values that pass the condition
    for (var i = 0; i < arr.length; i++) {
        // Only push values that are strictly greater than the cutoff value
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}

// 3. Better than average
function betterThanAverage(arr) {
    var sum = 0;
    // First loop: Calculate the sum of all elements in the array
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    var avg = sum / arr.length; // Calculate the average
    
    var count = 0; // Counter for values greater than average
    // Second loop: Check each value against the calculated average
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > avg) {
            count++;
        }
    }
    return count;
}

// 4. Array Reverse
function reverse(arr) {
    var left = 0; // Starting pointer at the beginning of the array
    var right = arr.length - 1; // Ending pointer at the last index
    
    // Swap elements from outside-in until the pointers meet in the middle
    while (left < right) {
        var temp = arr[left]; // Temporary storage for the left value
        arr[left] = arr[right]; // Assign right value to left position
        arr[right] = temp; // Assign temp (old left value) to right position
        
        left++; // Move left pointer forward
        right--; // Move right pointer backward
    }
    return arr;
}

// 5. Fibonacci Array
function fibonacciArray(n) {
    // Initial Fibonacci sequence starting values
    var fibArr = [0, 1];
    
    // Continue calculating values until the array reaches the desired length n
    while (fibArr.length < n) {
        var last = fibArr[fibArr.length - 1]; // Current last element
        var secondToLast = fibArr[fibArr.length - 2]; // Element before the last
        
        // Next Fibonacci number is the sum of the previous two
        fibArr.push(last + secondToLast);
    }
    return fibArr;
}
