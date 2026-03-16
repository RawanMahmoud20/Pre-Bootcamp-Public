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