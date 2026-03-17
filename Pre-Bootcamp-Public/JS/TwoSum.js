
// first solution by 2 for loops 
function twoSumBruteForce(numbers, target) {
  // loop 1 iterates through each number
    for (let i = 0; i < numbers.length; i++) {
        // loop 2 starts from the next number (i + 1)
        for (let j = i + 1  ; j < numbers.length; j++) {
            // check if the sum of the two numbers equals the target
            if (numbers[i] + numbers[j] === target) {
                return [i, j]; // return the indices of the two numbers
            }
        }
    }
    return null; // no solution found
}

const numss = [ 11, 2, 8 ,15 ];
const targett = 10;
console.log(twoSumBruteForce(numss, targett)); // Output: [1, 2]



// Two Sum Problem
function twoSum(numbers, target) {
    const numMap = new Map();
    for (let i = 0; i < numbers.length; i++) {
       // Calculate the complement
        const complement = target - numbers[i];
       // Check if the complement exists in the map
        if (numMap[complement] !== undefined) {
          // Found the complement, return indices
            return [numMap[complement], i];
        }
        // Store the current number and its index in the map
        numMap[numbers[i]] = i;
    }
    // If no solution is found, return null or an empty array
    return null;
}
// Example usage
const nums = [2, 8, 11, 15];
const target = 10;
const result = twoSum(nums, target);
console.log(result); // Output: [0, 1]


