// Exercise 5: Sort Numbers

/*
  Description: Sort an array of numbers in ascending or descending order
  Write a function that: Sort the array in ascending or descending order based on parameter
  Expected Output: [3,1,2] sorted asc → [1,2,3]
*/

function sort_numbers(numbers) {
  // Your code here
  return numbers.sort((a,b) => a-b );
}

// Test the function
const numbers = [3,1,2];
console.log(sort_numbers(numbers)); // Should return [3,1,2] sorted asc → [1,2,3]
