/*
Name: Jose Bianchi 
GitHub username: josebianchi7
Current corresponding execution filename: quiz.exe

Long Code Description: The code below contains questions and a point system, 
which can be formatted to make unique personality quizzes. The current 
personality quiz is related to Harry Potter.
*/

// import necessary libraries:
#include <iostream>    
#include <string>              
#include <stdlib.h>           // includes functions for program termination, resource cleanup, and random using rand() and srand()
#include <ctime>              // includes functions for processing time, system time, and run time of a program

int main() {

    // Personality Quiz (Harry Potter Sorting House edition):
    int gryffindor = 0;
    int hufflepuff = 0;
    int ravenclaw = 0;
    int slytherin = 0;

    int answer = 0;

    std::cout << "Welcome to The Sorting Hat Quiz!\n\n";
    std::cout << "Please enter reponses using digit for answer.\n\n";

    //Question 1:
    std::cout << "Q1) When I'm dead, I want people to remember me as: \n\n";
    std::cout << "   1) The Good\n";
    std::cout << "   2) The Great\n";
    std::cout << "   3) The Wise\n";
    std::cout << "   4) The Bold\n";
  
    std::cin >> answer;

    switch (answer) {
        case 1: 
            gryffindor += 1;
            break;
        case 2: 
            hufflepuff += 1;
            break;
        case 3: 
            ravenclaw += 1;
            break;
        case 4: 
            slytherin += 1;
            break;
        default:
            std::cout << "Invalid response. Moving on.\n";
            break;  
    }

    //Question 2:
    std::cout << "Q2) Do you prefer dawn or dusk?  \n\n";
    std::cout << "   1) Dawn\n";
    std::cout << "   2) Dusk\n";
  
    std::cin >> answer;

    switch (answer) {
        case 1: 
            gryffindor += 1;
            hufflepuff += 1;
            break;
        case 2: 
            ravenclaw += 1;
            slytherin += 1;
            break;
        default:
            std::cout << "Invalid response. Moving on.\n";
            break;  
    }
    //Question 3:
    std::cout << "Q3) Which kind of instrument most pleases your ear? \n\n";
    std::cout << "   1) Violin\n";
    std::cout << "   2) Trumpet\n";
    std::cout << "   3) Piano\n";
    std::cout << "   4) Drum\n";
  
    std::cin >> answer;

  switch (answer) {
    case 1: 
      slytherin += 1;
      break;
    case 2: 
      hufflepuff += 1;
      break;
    case 3: 
      ravenclaw += 1;
      break;
    case 4: 
      gryffindor += 1;
      break;
    default:
      std::cout << "Invalid response. Moving on.\n";
      break;  
    }
  
    //Question 4:
    std::cout << "Q4) Which road tempts you most?\n\n";
    std::cout << "   1) The wide, sunny grassy lane\n";
    std::cout << "   2) The narrow, dark, lantern-lit alley\n";
    std::cout << "   3) The twisting, leaf-strewn path through woods\n";
    std::cout << "   4) The cobbled street lined (ancient buildings)\n";
  
    std::cin >> answer;

    switch (answer) {
        case 1: 
            hufflepuff += 1;
            break;
        case 2: 
            slytherin += 1;
            break;
        case 3: 
            gryffindor += 1;
            break;
        case 4: 
        ravenclaw += 1;
            break;
        default:
            std::cout << "Invalid response. Moving on.\n";
            break;  
    }
    // //Question 5:
    // std::cout << "Q5) (INSERT NEXT QUESTION HERE) \n\n";
    // std::cout << "   1)  \n";
    // std::cout << "   2)  \n";
    // std::cout << "   3)  \n";
    // std::cout << "   4)  \n";
  
    // std::cin >> answer;

    // switch (answer) {
    //   case 1: 
    //     gryffindor += 1;
    //     break;
    //   case 2: 
    //     hufflepuff += 1;
    //     break;
    //   case 3: 
    //     ravenclaw += 1;
    //     break;
    //   case 4: 
    //     slytherin += 1;
    //     break;
    //   default:
    //     std::cout << "Invalid response. Moving on.\n";
    //     break;  
    // }

    // Determine which house has the highest point
    int max = 0;
    std::string winner;

    // If need to see points per house:
    // std::cout << "\n";
    // std::cout << "Gryffindor: " << gryffindor << "\n";
    // std::cout << "Hufflepuf: " << hufflepuff << "\n";
    // std::cout << "Ravenclaw: " << ravenclaw << "\n";
    // std::cout << "Slytherin: " << slytherin << "\n";

    if (gryffindor > max) {
        max = gryffindor;
        winner = "Gryffindor";
    }
    if (hufflepuff > max) {
        max = hufflepuff;
        winner = "Hufflepuff";
    }
    if (ravenclaw > max) {
        max = ravenclaw;
        winner = "Ravenclaw";
    }
    if (slytherin > max) {
        max = slytherin;
        winner = "Slytherin";
    }

    // Print winner
    std::cout << "\n" << "You belong in House " << winner << "!\n";

    return 0;
}