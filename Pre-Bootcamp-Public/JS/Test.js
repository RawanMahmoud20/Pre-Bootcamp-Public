
// Q1
function reverseString(str) {
    let reversed = "";
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    return reversed;
}

console.log(reverseString("hello")); // "olleh"

// Q2
function countVowels(str) {
    let count = 0;
    const vowels = "aeiouAEIOU";
    // if we find a vowel, we increment the count and break out of the inner loop to avoid counting the same character multiple times
    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < vowels.length; j++) {
            if (str[i] === vowels[j]) {
                count++;
                break; 
            }
        }
    }
    return count;
}

console.log(countVowels("hello")); 
//Q3 
function isPalindrome(str) {
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

console.log(isPalindrome("madam")); 
console.log(isPalindrome("hello"));

/////// Q 4
function findLongestWord(sentence) {
    let words = sentence.split(" ");
    
    let longest = words[0];

    for (let i = 1; i < words.length; i++) {
        if (words[i].length > longest.length) {
            longest = words[i]; 
        }
    }

    return longest;
}

console.log(findLongestWord("I love solving algorithms")); 
////
function getFeedback(grade) {
  switch (grade.toUpperCase()) {
    case "A":
      return "Excellent";
    case "B":
      return "Good job";
    case "C":
      return "You passed";
    case "D":
      return "Need improvement";
    case "F":
      return "Failed";
    default:
      return "Invalid grade";
  }
}

console.log(getFeedback("B")); 
console.log(getFeedback("z")); 

///////

const vowels = "aeiouAEIOU";
function countCharacters(str) {
  let counts = {
    vowels: 0,
    digits: 0,
    spaces: 0,
    others: 0
  };

  const vowelsList = "aeiouAEIOU";

  for (let char of str) {
    if (vowelsList.includes(char)) {
      counts.vowels++;
    } 
    else if (char >= "0" && char <= "9") {
      counts.digits++;
    } 
    else if (char === " ") {
      counts.spaces++;
    } 
    else {
      counts.others++;
    }
  }

  return counts;
}

const result = countCharacters("Hi 123!");
console.log(result); 




function countCharacterTypes(str) {
  let counts = {
    vowels: 0,
    digits: 0,
    spaces: 0,
    others: 0
  };

  for (let char of str) {

    switch (true) {
      case  vowels.includes(char):
        counts.vowels++;
        break;

      case char >= "0" && char <= "9":
        counts.digits++;
        break;

      case (char === " "):
        counts.spaces++;
        break;

      default:
        counts.others++;
    }
  }

  return counts;
}

console.log(countCharacterTypes("Hi 123!")); 
