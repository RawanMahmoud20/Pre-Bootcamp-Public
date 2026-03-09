// Loop from 1 to 20, incrementing by 2
    console.log("first loop ");

for (let i = 1; i <= 20; i += 2) {
    console.log(i);
}

// Loop from 100 down to 0, decrementing by 1 and print the number if it is a multiple of 3
console.log("secound  loop ");
for(let i=100 ; i>=0 ; i--){
    if(i %3 ===0){
        

        console.log(i);
    }
}
// Print the given sequence 
console.log("third loop ");
for (let i = 4; i >= -3.5; i -= 1.5) {
    console.log(i);
}

// sigma of numbers from 1 to 100
console.log("fourth loop ");
let sum = 0; 
for(let i = 1 ; i<=100 ; i++){
    sum+=i;
}
console.log(sum);

// factorial 1 to 12 
console.log("fifth loop");
product = 1;
for(let i = 1 ; i <=12 ; i++){
    product*=i;
}
console.log(product);