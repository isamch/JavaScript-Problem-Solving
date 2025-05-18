// Exercise 11: Merge Arrays

/*
  Description: Merge two arrays while removing duplicates
  Write a function that: Merge two arrays while removing duplicates and return new array
  Expected Output: Merge [1,2] and [2,3] → [1,2,3]
*/

function merge_arrays(arr1, arr2) {
  // Your code here
  arr2.map( e => arr1.push(e))

  return arr1.filter((e,i,arr)=>arr.indexOf(e) === i);
}

let first_Arr = [1,2];
let second_Arr = [2,3];

// Test the function
console.log(merge_arrays(first_Arr, second_Arr)); // Should return Merge [1,2] and [2,3] → [1,2,3]
