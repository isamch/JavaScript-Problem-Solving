// Exercise 9: Calculate Average

/*
  Description: Calculate the average of numbers in an array
  Write a function that: Calculate the average of numbers in the array and return it
  Expected Output: [1,2,3,4] → 2.5
*/

function calculate_average(array) {
  // Your code here
  if (array.length === 0) return 0;
  
  const sum = array.reduce((previous, current) => previous + current, 0)
  return sum/array.length;

}

let array = [1,2,3,4];

// Test the function
console.log(calculate_average(array)); // Should return [1,2,3,4] → 2.5
