// Exercise 8: Swap Case

/*
  Description: Swap uppercase to lowercase and vice versa in a string
  Write a function that: Swap character cases in the string and return the result
  Expected Output: 'Hello World' → 'hELLO wORLD'
*/

function swap_case(text) {
  // Your code here
  return text.split('').map(e=> e == e.toUpperCase() ? e.toLowerCase() : e.toUpperCase() ).join('');


}

// Test the function
console.log(swap_case("Hello World")); // Should return 'Hello World' → 'hELLO wORLD'
