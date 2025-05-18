// Exercise 10: Find Element

/*
  Description: Find an element in an array and return its index
  Write a function that: Find the element in the array and return its index or -1 if not found
  Expected Output: Find 3 in [1,2,3] → 2
*/

function find_element(array, element) {
  // Your code here
  const index = array.indexOf(element);
  if (index === -1) {
    return "Element not found";
  }
  return index;
}

let array = [1,2,3];
// Test the function
console.log(find_element(array, 2)); // Should return Find 3 in [1,2,3] → 2
