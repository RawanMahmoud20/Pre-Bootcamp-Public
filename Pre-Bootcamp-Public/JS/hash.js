// =========================================================================
// 1. Zip Arrays into Map
// Merges two arrays into an object where the first array's elements
// become the keys and the second array's elements become the values.
// =========================================================================
function zipArraysIntoMap(keysArray, valuesArray) {
    let map = {};
    
    for (let i = 0; i < keysArray.length; i++) {
        map[keysArray[i]] = valuesArray[i]; // pair each key with its matching value by index
    }
    
    return map;
}

let arr1 = ["abc", 3, "yo"];
let arr2 = [42, "wassup", true];
console.log(zipArraysIntoMap(arr1, arr2));
// expected: { "abc": 42, 3: "wassup", "yo": true }


// =========================================================================
// 2. Invert Hash
// Flips an object so that every key becomes a value and every value becomes a key.
// =========================================================================
function invertHash(obj) {
    let inverted = {};
    
    for (let key in obj) {
        inverted[obj[key]] = key; // swap: old value is new key, old key is new value
    }
    
    return inverted;
}

let assocArr = { "name": "Zaphod", "charm": "high", "morals": "dicey" };
console.log(invertHash(assocArr));
// expected: { "Zaphod": "name", "high": "charm", "dicey": "morals" }


// =========================================================================
// 3. Count Values (without .length)
// Manually counts the number of key-value pairs in an object
// without using the .length property.
// =========================================================================
function countValues(obj) {
    let count = 0;
    
    for (let key in obj) {
        count++; // increment once for every key encountered
    }
    
    return count;
}

let bandInfo = {
    band: "Travis Shredd & the Good Ol' Homeboys",
    style: "Country/Metal/Rap",
    album: "668: The Neighbor of the Beast"
};
console.log(countValues(bandInfo));
// expected: 3