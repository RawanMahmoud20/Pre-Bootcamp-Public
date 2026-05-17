function coinChange(cents) {
    // result object with all coin types initialized to zero
    let coins = {
        quarters: 0,
        dimes: 0,
        nickels: 0,
        pennies: 0
    };

    // how many quarters fit, then update the remaining amount
    coins.quarters = Math.floor(cents / 25);
    cents %= 25;

    // how many dimes fit in what's left
    coins.dimes = Math.floor(cents / 10);
    cents %= 10;

    // how many nickels fit in what's left
    coins.nickels = Math.floor(cents / 5);
    cents %= 5;

    // everything remaining is pennies
    coins.pennies = cents;

    return coins;
}

console.log(coinChange(94));
// expected: { quarters: 3, dimes: 1, nickels: 0, pennies: 4 }

console.log(coinChange(41));
// expected: { quarters: 1, dimes: 1, nickels: 1, pennies: 1 }


function maxMinAvg(arr) {
    // guard against empty array to avoid division by zero and bad comparisons
    if (arr.length === 0) {
        return { max: 0, min: 0, avg: 0 };
    }

    // assume the first element is both the largest and smallest to start
    let max = arr[0];
    let min = arr[0];
    let sum = 0;

    for (let i = 0; i < arr.length; i++) {
        // update max if a larger value is found
        if (arr[i] > max) {
            max = arr[i];
        }
        // update min if a smaller value is found
        if (arr[i] < min) {
            min = arr[i];
        }
        // accumulate sum for the average calculation
        sum += arr[i];
    }

    // average = total sum divided by number of elements
    let avg = sum / arr.length;

    // return all three stats as an object
    return {
        max: max,
        min: min,
        avg: avg
    };
}

console.log(maxMinAvg([1, 2, 3, 4, 5]));
// expected: { max: 5, min: 1, avg: 3 }

console.log(maxMinAvg([10, -2, 4, 8]));
// expected: { max: 10, min: -2, avg: 5 }