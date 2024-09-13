/*
This code allows a user to choose rock, paper, scissors, or secret choice (bomb). 
Then a computer will randomly select a choice among the first three options and 
return the winner. Please scroll to end of code to input your choice.
*/

console.log('Hi, below are the results:');

// User choice validator:
const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors' || userInput === 'bomb') {
    return userInput;
  } else {
     console.log('Error, choice invalid.');
  }
}

// Computer choice generator:
const getComputerChoice = () => {
  let num = Math.floor(Math.random() * 3);
  if (num === 0) {
      return 'rock';
  } else if (num === 1) {
      return 'paper';
  } else if (num === 2) {
      return 'scissors';
  }
};

// Choice compariosn function:
const determineWinner = (userChoice, computerChoice) => {
  // If choices match:  
  if (userChoice === computerChoice) {
      return 'Game was a tie.';
  }; 
  // Branch if user chose rock:
  if (userChoice === 'rock') {
    if (computerChoice === 'paper') {
      return 'Computer won!';
    } else {
      return 'Human won!';
    }
  } 
  // Branch if user chose paper:
  else if (userChoice === 'paper') {
      if (computerChoice === 'scissors') {
      return 'Computer won!';
    } else {
      return 'Human won!';
    }
  } 
  // Branch if user chose scissors:
  else if (userChoice === 'scissors') {
      if (computerChoice === 'rock') {
      return 'Computer won!';
    } else {
      return 'Human won!';
    }
  } 
  // Branch if user chose secret choice:
  else if (userChoice === 'bomb') {
    return 'Human won!';
  }
};

// Function expression to accept user's choice and determine winner:
const playGame = userInitialChoice => {
  let userChoice = getUserChoice(userInitialChoice);
  let computerChoice = getComputerChoice();
  console.log('Human Choice: ' + userChoice);
  console.log('Computer Choice: ' + computerChoice);
  console.log(determineWinner(userChoice, computerChoice));
};

// Call overall function AND make your choice:
playGame('Rock');
