// Exercise 3: Reverse String

/*
  Description: Reverse the order of characters in a string
  Write a function that: Reverse the string and return the result
  Expected Output: For 'hello' → 'olleh'
*/

function reverse_string(text) {
  // Your code here
  let textArr = text.split('');
  
  
  let temp;
  for(let i = 0 ; i < Math.floor(textArr.length / 2) ; i++ )
  {
    temp = textArr[i];
    textArr[i]  = textArr[textArr.length - 1 - i];
    textArr[textArr.length - 1 - i] = temp;
    
  }
  
  
  return textArr.join('');
  
}

// Test the function
const text = 'hello world';
console.log(reverse_string(text)); // Should return For 'hello' → 'olleh'
