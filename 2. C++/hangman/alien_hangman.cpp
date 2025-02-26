/*
Name: Jose Bianchi 
GitHub username: josebianchi7
Compile files: alien_hangman.cpp, hangman_functions.cpp
Description: program to play hangman, but using an alien abduction animation
instead of a hanging person. 
*/

#include <iostream>
#include <vector>
#include <string>
#include "hangman_funcs.hpp"

int main() {

    // Introduction message function call
    greet();

    // Variable initializers:
    std::string codeword = "potatoes";
    // Ensure answer is of equal size to codeoword
    std::string answer = "________";
    int misses = 0;

    // Reszeable object to contain incorrect guesses
    std::vector<char> incorrect;

    bool guess;
    char letter;
    char code_letter;
    int letter_count;

    // Game loop to run as long as answer does not match codeword and incorrect guesses is less than 7
    while (answer != codeword && misses < 7) {
        // Capture player input
        std::cout << "Please enter your guess: \n";
        std::cin >> letter;
        guess = false;
        letter_count = 0;

        // Check if letter input is in codeword
        for (int k=0; k < codeword.size(); k++) {
            code_letter = codeword[k];
            
            // If match is found, set index in answer to correct letter guess
            if (letter == code_letter) {
                answer[k] = letter;
                guess = true;
                letter_count++;
            }
        }

        // Check if last guess was correct, if not add last guess to incorrect letters vector
        if (guess == true) {
            std::cout << "Correct! ";
            if (letter_count == 1) {
                std::cout << "There is 1 " << letter << " in the codeword.\n";
            }
            else {
                std::cout << "There are "<< letter_count << " " << letter << "'s in the codeword.\n";
            }
        } 
        else {
            std::cout << "Incorrect! The tractor beam pulls the person in further.\n";
            incorrect.push_back(letter);
            misses++;
        }
        
        // Call display misses function to show current alien abduction animation
        display_misses(misses);

        // Display incorrect guesses statement
        display_status(incorrect, answer);
        
    }
    // Call end game function to inform player if they won or lost
    end_game(answer, codeword);

    return 0;

}