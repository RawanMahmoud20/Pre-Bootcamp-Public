// 1. Remove Blanks
// Removes all spaces from the string
function removeBlanks(str) {
    let result = "";
    // If the character is NOT a space, add it to result
    for (let i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            result += str[i];
        }
    }
    return  console.log(result);
}
removeBlanks("  Play Games  ");

// 2. Get Digits
// Extracts all digits from the string and returns them as a number
function getDigits(str) {
    let digitStr = "";
    for (let i = 0; i < str.length; i++) {
        // Check if character is a digit
        if (str[i] !== " " &&  str[i] >= "0" && str[i] <= "9") {
        // if (str[i] !== " " && !isNaN(Number(str[i])  )) {
            digitStr += str[i];
        }
    }
    return  console.log(Number(digitStr));
}

getDigits("a18c03d15n6d0j!8");

// 3. Acronyms
// short version to get the first letter of each word and convert to uppercase
function acronym(str) {
    let words = str.split(" ");
    let result = "";
    for (let i = 0; i < words.length; i++) {
        // Ignore empty strings (caused by extra spaces)
        if (words[i].length > 0) {
            result += words[i][0].toUpperCase();
        }
    }
    return  console.log(result);
}
acronym(" there's no free lunch - gotta pay yer way. ");

 // 4. Count Non-Spaces
 // Counts all characters except spaces

function countNonSpaces(str) {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        // Increase count if it's not a space
        if (str[i] !== " ") {
            count++;
        }
    }
    return  console.log(count);
}
countNonSpaces("Hello world !");

// 5. Remove Shorter Strings
// Keeps only strings with length >= minLength
function removeShorterStrings(arr, minLength) {
    let newArr = [];
    for (let i = 0; i < arr.length; i++) {
        // Add only valid strings to new array

        if (arr[i].length >= minLength) {
            newArr[newArr.length] = arr[i];
        }
    }
    return  console.log(newArr);
}
removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3);