// create Array
let colors=["red","blue","green","yellow","purple"];
console.log("First:", colors[0], "| Last:", colors[colors.length - 1]);
console.log("Second position:", colors[1]);

// Update array 
colors[2] = "orange"; 
console.log("Updated colors:", colors);


// New Requirment 
let numbers=[10,20,30,40,50];
numbers.forEach(element => {
    console.log(element)
});

for(let i = numbers.length - 1 ; i >= 0 ; i--){
  console.log("Reverse :", numbers[i]);
}

//Search in array 
let searchNums = [5, 10, 15, 20, 25];
let index = searchNums.indexOf(25);

if (index !== -1) {
    console.log("Found at position " + index);
} else {
    console.log("Not Found");
}
// Sort
let scores = [50, 20, 70, 10, 40];
scores.sort((a,b)=> a - b);
console.log("Ascending:", scores);
scores.sort((a, b) => b - a);
console.log("Descending:", scores);
// Sorting strings
let names =["Shatha","Sara","Lina","Sami","Dalia"];
console.log("Names sorted:", names.sort());

//Inserting 

let animals = ["dog","cat","rabbit"];
animals.push("elephant");
animals.unshift("lion");
animals.splice(2,0,"tiger");
console.log("Animals:", animals);


// Deleting 
let fruits = ["apple","banana","cherry","date"];
fruits.shift();
fruits.pop();
let filteredFruits = fruits.filter(f => f !== "banana");
console.log("Fruits:", filteredFruits);  


///Join Arrays
let array1 =[1,2,3];
let array2 =[4,5,6];
let join= array1.concat(array2);
console.log("Joined:", join);


// Splitting 
let items=["a","b","c","d","e"];
let firstPart = items.slice(0, 3);
let secondPart = items.slice(3);
console.log("First Part:", firstPart);
console.log("Second Part:", secondPart);


//  Filtering
let bigNumbers = [1, 5, 10, 15, 20, 25, 30];
let FilterNumbers= bigNumbers.filter(num => num > 15);
console.log("Filtered Numbers:", FilterNumbers);


// Removing Duplicates
let duplicates = [1, 2, 2, 3, 4, 4, 5];
let unique = [];
duplicates.forEach(num =>{
    if(!unique.includes(num)){
        unique.push(num);
    }
})
console.log("Unique:" , unique);
  // Or 
let unique2 = [...new Set(duplicates)];
console.log("Anther Solution Of Unique:", unique2);

// Rotate An Array
function rotateArray(arr,n){
    for(let i=0 ; i < n; i++){
        let lastItem= arr.pop();
        arr.unshift(lastItem);
    }
    return arr ;
}
console.log("Rotated", rotateArray([1,2,3,4,5],2));
// Or 
let arr = [1,2,3,4,5];

let rotated = [...arr.slice(-2) , ...arr.slice(0,3)];

console.log("Anther Solution Of Rotated:", rotated);

///////////// Merge Sorted Arrays
function merge(arr1, arr2){
    let merged = [], i = 0, j = 0;
    while(i < arr1.length && j < arr2.length){
        merged.push(arr1[i] < arr2[j] ? arr1[i++] : arr2[j++]);
    }
    return merged.concat(arr1.slice(i)).concat(arr2.slice(j));
}
console.log(merge([1,3,5],[2,4,6]));
