/*
Program will accept a question and output a random fortune.
*/

// Variable for user's name:
let userName = 'Rio';

// Ternary expression for greeting if name is entered:
userName ? console.log('Hello, ' + userName + '!') : console.log('Hello!') 

// Variable for user's question:
let userQuestion = 'Will I get a second dog?';

// Confirm user's question with print statement:
userName ? console.log(userName + ', you asked the following: ' + userQuestion + '') : console.log('You asked the following: ' + userQuestion + '');

// Random number generator:
let randomNumber = Math.floor(Math.random() * 8);

// Variable for eight ball string:
let eightBall = '';

switch (randomNumber) {
  case 0:
    eightBall = 'It is certain'
    break;
  case 1:
    eightBall = 'It is decidedly so'
    break;
  case 2:
    eightBall = 'Reply hazy try again'
    break;
  case 3:
    eightBall = 'Cannot predict now'
    break; 
  case 4:
    eightBall = 'Do not count on it'
    break;
  case 5:
    eightBall = 'My sources say no'
    break;
  case 6:
    eightBall = 'Outlook not so good'
    break;
  case 7:
    eightBall = 'Signs point to yes'
    break;       
  default:
    break;
};

// Print result:
console.log(eightBall + '.');

  
