// =========================================================================
// 1. Is Word Alphabetical
// Returns true if all letters are in alphabetical order, false otherwise.
// =========================================================================
function isWordAlphabetical(str) {
    // remove non-alphabetic characters and convert to lowercase
    str = str.toLowerCase().replace(/[^a-z]/g, '');
    
    for (let i = 0; i < str.length - 1; i++) {
        // if any letter is greater than the next one, order is broken
        if (str[i] > str[i + 1]) {
            return false;
        }
    }
    return true;
}

console.log(isWordAlphabetical("abcdefg"));     // true
console.log(isWordAlphabetical("hello"));       // false
console.log(isWordAlphabetical("facetiously")); // true
console.log(isWordAlphabetical("arseniously")); // false


// =========================================================================
// 2. D Gets Jiggy
// Removes the first letter, uppercases the rest, then appends
// the first letter at the end in a formatted phrase.
// =========================================================================
function dGetsJiggy(name) {
    if (name.length < 2) return "";
    
    let firstLetter = name[0];
    let newName = name.slice(1).toUpperCase(); // everything after the first letter
    
    return newName + " to the " + firstLetter + "!";
}

console.log(dGetsJiggy("Dylan")); // "YLAN to the D!"


// =========================================================================
// 3. Common Suffix
// Returns the longest suffix shared by all words in the array.
// =========================================================================
function commonSuffix(words) {
    if (words.length === 0) return "";
    
    let suffix = words[0]; // start with the full first word as the candidate suffix
    
    for (let i = 1; i < words.length; i++) {
        // keep trimming the front of the suffix until it matches the end of the current word
        while (words[i].indexOf(suffix) !== words[i].length - suffix.length) {
            suffix = suffix.slice(1);
            if (suffix.length === 0) return ""; // no common suffix exists
        }
    }
    return suffix;
}

console.log(commonSuffix(["deforestation", "citation", "conviction", "incarceration"])); // "tion"
console.log(commonSuffix(["nice", "ice", "baby"])); // ""


// =========================================================================
// 4. Book Index
// Converts a sorted array of page numbers into a string of ranges
// for consecutive pages (e.g. 13, 14, 15 → "13-15").
// =========================================================================
function bookIndex(pages) {
    let index = "";
    
    for (let i = 0; i < pages.length; i++) {
        let start = pages[i];
        
        // advance i as long as the next page is consecutive
        while (i < pages.length - 1 && pages[i] + 1 === pages[i + 1]) {
            i++;
        }
        
        let end = pages[i];
        if (start === end) {
            index += start + ", ";          // single page, no range
        } else {
            index += start + "-" + end + ", "; // range of pages
        }
    }
    return index.slice(0, -2); // trim the trailing ", "
}

console.log(bookIndex([1, 13, 14, 15, 37, 38, 70])); // "1, 13-15, 37-38, 70"


// =========================================================================
// 5. Drop the Mike
// Trims extra spaces and capitalizes the first letter of each word.
// If the word "Mike" appears (any casing), returns "stunned silence" instead.
// =========================================================================
function dropTheMike(str) {
    str = str.trim();
    
    // special case: any mention of "mike" silences everything
    if (str.toLowerCase().includes("mike")) {
        return "stunned silence";
    }
    
    // capitalize the first character of every word
    return str.replace(/\b\w/g, char => char.toUpperCase());
}

console.log(dropTheMike(" hello world ")); // "Hello World"
console.log(dropTheMike(" Hey Mike "));    // "stunned silence"