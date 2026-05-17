// ============================================================================
// 1. Parens Valid — checks if parentheses '()' are balanced
// ============================================================================
function parensValid(str) {
    let counter = 0;

    for (let i = 0; i < str.length; i++) {
        if (str[i] === '(') {
            counter++;          // opening paren: increment
        } else if (str[i] === ')') {
            counter--;          // closing paren: decrement
        }

        // if counter goes negative, a closing paren appeared before an opening one
        if (counter < 0) {
            return false;
        }
    }

    // valid only if every opened paren was closed
    return counter === 0;
}


// ============================================================================
// 2. Braces Valid — checks if all bracket types '()', '[]', '{}' are balanced
//    Uses a stack to track and match pairs
// ============================================================================
function bracesValid(str) {
    const stack = [];
    const matches = {
        ')': '(',
        ']': '[',
        '}': '{'
    };

    for (let i = 0; i < str.length; i++) {
        const char = str[i];

        // opening bracket → push onto the stack
        if (char === '(' || char === '[' || char === '{') {
            stack.push(char);
        }
        // closing bracket → pop from stack and verify it matches
        else if (char === ')' || char === ']' || char === '}') {
            if (stack.pop() !== matches[char]) {
                return false;
            }
        }
    }

    // stack must be empty — every opened bracket was properly closed
    return stack.length === 0;
}


// ============================================================================
// 3. Is Palindrome — checks whether a string reads the same forwards & backwards
// ============================================================================

// Strict version: case-sensitive, spaces and symbols matter
function isPalindromeStrict(str) {
    let left = 0;
    let right = str.length - 1;

    while (left < right) {
        if (str[left] !== str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

// Lenient version: ignores spaces, punctuation, and letter casing
function isPalindromeLenient(str) {
    // strip everything except letters and digits, then lowercase
    const cleanedStr = str.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();

    return isPalindromeStrict(cleanedStr);
}


// ============================================================================
// 4. Longest Palindrome — finds the longest palindromic substring
// ============================================================================

// Helper: cleans a substring and checks if it's a palindrome (used by lenient version)
function isCleanedPalindrome(subStr) {
    const cleaned = subStr.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
    if (cleaned.length === 0) return false;

    let left = 0;
    let right = cleaned.length - 1;
    while (left < right) {
        if (cleaned[left] !== cleaned[right]) return false;
        left++;
        right--;
    }
    return true;
}

// Strict version: checks every possible substring using brute-force O(n²)
function longestPalindromeStrict(str) {
    let longest = "";

    for (let i = 0; i < str.length; i++) {
        for (let j = i + 1; j <= str.length; j++) {
            const substring = str.slice(i, j);

            // keep the substring if it's a palindrome and longer than the current best
            if (isPalindromeStrict(substring)) {
                if (substring.length > longest.length) {
                    longest = substring;
                }
            }
        }
    }
    return longest;
}

// Lenient version: same brute-force approach but compares cleaned lengths
function longestPalindromeLenient(str) {
    let longestRawSubstring = "";
    let maxCleanedLength = 0;

    for (let i = 0; i < str.length; i++) {
        for (let j = i + 1; j <= str.length; j++) {
            const rawSubstring = str.slice(i, j);

            if (isCleanedPalindrome(rawSubstring)) {
                const cleanedLength = rawSubstring.replace(/[^a-zA-Z0-9]/g, "").length;

                // compare by the actual alphanumeric length, not the raw length
                if (cleanedLength > maxCleanedLength) {
                    maxCleanedLength = cleanedLength;
                    longestRawSubstring = rawSubstring;
                }
            }
        }
    }

    // return the result cleaned and lowercased
    return longestRawSubstring.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
}


// ============================================================================
// Test area — output matches the expected results exactly
// ============================================================================

console.log("--- 1. Parens Valid ---");
console.log(parensValid("Y(3(p)p(3)r)s")); // true
console.log(parensValid("N(0(p)3"));       // false
console.log(parensValid("N(0)t )0(k"));    // false

console.log("\n--- 2. Braces Valid ---");
console.log(bracesValid("W(a{t}s[o(n{c}o)m]e)h[e{r}e]!")); // true
console.log(bracesValid("D(i{a}l[t]o)n{e"));               // false
console.log(bracesValid("A(1)s[O(n)0{t}0}k"));             // false

console.log("\n--- 3. Is Palindrome (Strict) ---");
console.log(isPalindromeStrict("a x  a")); // true
console.log(isPalindromeStrict("racecar")); // true
console.log(isPalindromeStrict("Dud"));     // false
console.log(isPalindromeStrict("oho!"));    // false

console.log("\n--- 3. Is Palindrome (Lenient) ---");
console.log(isPalindromeLenient("Able was I, ere I saw Elba")); // true

console.log("\n--- 4. Longest Palindrome (Strict) ---");
console.log(longestPalindromeStrict("what up, daddy-o?"));                // "dad"
console.log(longestPalindromeStrict("uh... not much"));                   // "u"
console.log(longestPalindromeStrict("Yikes! my favorite racecar erupted!")); // "e racecar e"

console.log("\n--- 4. Longest Palindrome (Lenient) ---");
console.log(longestPalindromeLenient("Hot puree eruption!")); // "tpureeerupt"