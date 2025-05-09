// Exercise 1: Count Vowels

/*
  Description: Count the number of vowels in a given string
  Write a function that: Return the count of vowels (a, e, i, o, u) in the string
  Expected Output: For 'Hello World' → 3
*/

"use strict"; 

const string = 'hello world';
function count_vowels(str) {
  // Your code here
  const vowels = 'aeiou';
  str = str.toLowerCase();
  
  return str.split('').filter(e => vowels.includes(e)).length;
    
}

// Test the function
console.log(count_vowels(string)); // Should return For 'Hello World' → 3
