/*
Program to translate words into "whale talk".
Rules for whale talk:
  1. There are no consonants. Only vowels excluding 'y'.
  2. Whenever 'U' and 'E' are used, double them into 'UU' and 'EE', respectively.
*/

// Variable for input phrase:
const input = 'turpentine and turtles';

// Array to reference vowels:
const vowels = ['a', 'e', 'i', 'o', 'u'];

// Array to store vowels from loop:
let resultArray = [];

// Comparison Loop:
// First loop through input string:
for (let i = 0; i < input.length; i++) {
  let inputChar = input[i];

  // If vowel match is either 'e' or 'u', add letter:
  if (inputChar.toLowerCase() === 'e' || inputChar.toLowerCase() === 'u') {
        resultArray.push(inputChar.toUpperCase());}

  // Second, loop through vowels array
  for (let j = 0; j < vowels.length; j++) {
    let vowelChar = vowels[j];
    
    // If match found, add vowel to result Array:
    if (inputChar.toLowerCase() === vowelChar) {
       resultArray.push(inputChar.toUpperCase());
      }
    }
};

resultString = resultArray.join('');
console.log(resultString);