// Two Sum Problem
function twoSum(numbers, target) {
    const numMap = new Map();
    for (let i = 0; i < numbers.length; i++) {
        const complement = target - numbers[i];
        if (numMap[complement] !== undefined) {
            return [numMap[complement], i];
        }
        numMap[numbers[i]] = i;
    }
    return null;
}
// Example usage
const nums = [2, 8, 11, 15];
const target = 10;
const result = twoSum(nums, target);
console.log(result); // Output: [0, 1]