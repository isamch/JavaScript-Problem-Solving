// Exercise 4: Check Palindrome

/*
  Description: Check if a string reads the same forwards and backwards
  Write a function that: Check if the string is a palindrome (reads the same backwards)
  Expected Output: For 'madam' → true, for 'hello' → false
*/

function check_palindrome(string) {
  // Your code here
  const len = string.length;
  let isPalindrom = true;
  for(let i = 0; i < Math.floor(len / 2) ; i++ ){
    if(string[i] != string[len - 1 - i]){
      isPalindrom = false 
      return;
    } 
  }
  
  return isPalindrom;

  // other solution:
  // return str === str.split('').reverse().join('');

}

// Test the function
const string = 'madam';
console.log(check_palindrome(string)); // Should return For 'madam' → true, for 'hello' → false
