// Exercise 6: Remove Duplicates

/*
  Description: Remove duplicate elements from an array
  Write a function that: Remove duplicate elements from the array and return a new array
  Expected Output: [1,2,2,3] → [1,2,3]
*/

function remove_duplicates(numbers) {
  // Your code here
  return numbers.filter((e,i,arr) => arr.indexOf(e) == i)
}

// Test the function
const numbers = [3, 1, 2, 2, 3, 4, 5, 1, 9, 8, 0, 0];
console.log(remove_duplicates(numbers)); // Should return [1,2,2,3] → [1,2,3]
