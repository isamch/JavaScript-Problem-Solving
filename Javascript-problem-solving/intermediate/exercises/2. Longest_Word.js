// Exercise 2: Longest Word

/*
  Description: Find the longest word in a sentence
  Write a function that: Find and return the longest word in the sentence
  Expected Output: For 'The quick brown fox' → 'quick'
*/

function longest_word(txt) {
  const words = txt.split(' ');
  let longest = '';

  for (const word of words) {
    if (word.length > longest.length) {
      longest = word;
    }
  }

  return longest;
}

// Test the function
const text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry';
console.log(longest_word(text)); // Should return For 'The quick brown fox' → 'quick'
