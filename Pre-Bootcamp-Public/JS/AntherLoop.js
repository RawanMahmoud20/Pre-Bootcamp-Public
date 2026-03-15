//print numbers from 0 to 10
for(let i= 1 ; i<=10 ; i++){
    console.log(i);
}
// from 10 to 0
for(let i= 10 ; i>=1 ; i--){
    console.log(i);
}
// for loop odd nubmers 1 to 20
for(let i =1 ; i<=20;i+=2){
    console.log(i);
}

// for loop even nubmers 1 to 20
for(let i =2 ; i<=20;i+=2){
    console.log(i);
}
//  foor to sum of numbers from 1 to 10
let sum =0;
for(let i=1 ; i<=10; i++){
    sum+=i;
}
console.log("Sum of numbers from 1 to 10:", sum)
// for loop to print number from 1 to 30 
for(let i=1 ; i<=30 ; i++){
    if(i%3 ===0 && i%5 ===0){
        console.log("FizzBuzz");
    }else if(i%5 ===0){
        console.log("Buzz");
    }else if(i%3 ===0 ){
        console.log("Fizz");
    }else{
        console.log(i);
    }
}

