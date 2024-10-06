// Header file containing function declarations for alien_hangman.cpp program.

#include <vector>
#include <iostream>
#include <string>


void greet();
void display_misses(int misses);
void end_game(std::string answer, std::string codeword);
void display_status(std::vector<char> incorrect, std::string answer);


