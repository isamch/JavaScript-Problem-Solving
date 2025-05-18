// Exercise 7: Sum Even Numbers

/*
  Description: Sum all even numbers in an array
  Write a function that: Sum all even numbers in the array and return the total
  Expected Output: [1,2,3,4] → 6
*/

function sum_even_numbers(numbers) {
  // Your code here
  let sum = 0;
  for(let number of numbers){
    if(number%2 == 0) {
      sum += number;
    } 
  }
  
  return sum;
}

// Test the function
const numbers = [1,2,3,4];
console.log(sum_even_numbers(numbers)); // Should return [1,2,3,4] → 6
