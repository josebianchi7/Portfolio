/*
Name: Jose Bianchi 
GitHub username: josebianchi7
Current corresponding execution filename: story.exe

Long Code Description: User can navigate through an
adventure and based on their inputs, the program will
arrive at a different ending for the story adventure.

Current branch points: 3
Current ending variations: 3
*/

// import necessary libraries:
#include <iostream>           
#include <string>
#include <cmath>
#include <stdlib.h>           
#include <ctime>  

// Player will roll a dice to assess if their chosen outcome was successful
int dice(int odds) {
    
    return (rand() % odds) + 1;
    }

    /*
    Current challenge responses will increment point counters to following results:
    1. Gaining renown and becoming dragon king
    2. Gaining inner peace and becoming dragon sage
    3. Inspiring fear and becoming a dragon slayer
    */
   
int main() {
    std::cout << "\n";
    std::cout << "Hello, welcome to the dragon warrior story adventure!\n\n" <<
    "You begin this journey as a young, but independent, child, alone in the wilderness.\n" <<  
    "You must react to challenges using number responses.\n" <<
    "With a little luck, you can reach the story conclusion that is meant for you.\n\n";

    // Choices will increase score of the following outcomes:
    int king = 0;
    int sage = 0;
    int slayer = 0;

    // Health Point variable:
    int hp = 100;

    // Decision 1
    // No dice roll
    // New variables:
    //      color: dragon companion's color
    //      name: dragon companion's name
    std::cout << "During your morning hunt for food, you spot three baby dragons fighting over a dead rodent.\n" << 
    "They appear to be starving and abandoned.\n" <<
    "You move closer, but they sense you and flee in different directions.\n" <<
    "You must pick one dragon to chase, which do you choose?\n\n";

    std::cout << "   1) The scrappy red one.\n";
    std::cout << "   2) The graceful blue one.\n";
    std::cout << "   3) The mean looking black one.\n";
    
    int answer = 0;
    std::string color;
    std::cin >> answer;

    switch (answer) {
        case 1: 
            king += 1;
            color = "red";
            break;
        case 2: 
            sage += 1;
            color = "blue";
            break;
        case 3: 
            slayer += 1;
            color = "black";
            break;
        default:
            std::cout << "Invalid response. Moving on.\n";
            break;  
    }

    // Dragon Name Capture:
    std::cout << "You caught up to the baby dragon, but it collapsed from exhaustion.\n" <<
    "You take it back to your home and decide to try and look for the others another day.\n\n";
    std::string name;
    std::cout << "After a couple days, the " << color << " dragon has become healthy and seems bonded to you.\n" <<
    "What would you like to name your new dragon companion?\n\n";
    std::cin >> name; 


    
    // Decision 2
    // No dice roll
    // New variables:
    //      location_1: adventure's first phase takes place here.
    std::cout << "\n";         
    std::cout << name << " is growing larger by the day, and is now as tall as your waist.\n" <<
    "However, food in the area is not sufficient to keep you and " << name << " fed.\n" << 
    name << "'s siblings have also not been seen since that first encounter.\n"<< 
    "You decide to roam the lands, grow with your dragon, and find its siblings.\n" <<
    "You must choose a path:\n\n";
    
    std::cout << "   1) The mountains.\n";
    std::cout << "   2) The deep forest\n";
    std::cout << "   3) The desert\n";
    
    std::string location_1;
    std::cin >> answer;

    switch (answer) {
        case 1: 
            king += 1;
            location_1 = "mountains";
            break;
        case 2: 
            sage += 1;
            location_1 = "deep forest";
            break;
        case 3: 
            slayer += 1;
            location_1 = "desert";
            break;
        default:
            std::cout << "Invalid response. Moving on.\n";
            break;  
    }

    std::cout << "\nAnd so it begins, you and " << name << " will explore the " << location_1 << "!\n";


    
    // Story only continues as long as player has health points.
    while (hp > 0) { 



        // Situation 1: 
        //Challenge 1:
        std::cout << "On your way to the " << location_1 << " a wild boar begins charging at you from a distance.\n" <<
        "You must decide how to react and quick!\n\n";

        std::cout << "   1) Fight it head on and test your strength.\n";
        std::cout << "   2) Jump into a nearby tree and wait for it to pass.\n";
        std::cout << "   3) Set up a trap, and then go for the kill.\n";

        std::cin >> answer;

        // If dice roll was larger than half of dice size, move was successful, result = 1
        // Otherwise, result = 0 and user must try again, but loses hp points
        int result = 0;
        int dice_size = 6;
        int roll;

        while (result == 0) {

            // Dice Roll
            srand (time(NULL));
            roll = dice(dice_size);
            
            // To see dice roll outcome:
            // std::cout << "You rolled a " << roll <<" on a " << dice_size << "-sided die.\n";

            // Need successful roll to move forward
            if (roll > (dice_size / 2)) {
                std::cout << "Success! You may proceed.\n\n";
                result = 1;
             
            }
            else {
                hp -= 10;
                dice_size += 1;
                std::cout << "No success. You took damage.\n" <<
                "Current HP = " << hp << "/ 100. You try again.\n\n";
                if (hp == 0) {
                    // If player lost all hp, they must rerun code to try again
                    std::cout << "You did not survive the previous challenge. Please rerun program to try again.\n\n";   

                    return 0;
                }
            }
        }    
        //Reset result to zero:
        result = 0;


        // After surviving challenge, increment category point
        switch (answer) {
            case 1: 
                king += 1;
                break;
            case 2: 
                sage += 1;
                break;
            case 3: 
                slayer += 1;
                break;
            default:
                std::cout << "Invalid response. Moving on.\n";
                break;  
        }

        
        // Situation 2:
        std::cout << "You begin seeing signs posted on your path. The signs warn of an evil bear that attacks travelers.\n" <<
        "There are other paths to the " << location_1 << ", but it will add days to your travels. How do you proceed?\n\n";

        std::cout << "   1) Follow the current path and fight the bear if you must.\n";
        std::cout << "   2) Go around the bear's territory, it is not worth the risk.\n";
        std::cout << "   3) Move in carefully and begin hunting the bear.\n";

        std::cin >> answer;

        // Challenge 2:

            switch (answer) {
            case 1: 
                king += 1;
                std::cout << "\n";
                std::cout << "Shortly after ignoring the signs, the bear finds you!\n" <<
                "The bear stands at least twice your height with unnatural features and a bloodthirst you have never felt before.\n";
                break;
            case 2: 
                sage += 1;
                std::cout << "\n";
                std::cout << "As you were leaving the area, your dragon, " << name << " picks up the scent of meat. " << 
                name << " cannot help but go in the direction of food. You see the bear up ahead with a fresh kill and the beast seems disturbed.\n";
                break;
            case 3: 
                slayer += 1;
                std::cout << "\n";
                std::cout << "It does not take long for " << name << " and you to pick up the scent of blood.\n" <<
                "You show your dragon how to move silently upon prey.\n" <<
                "However, upon seeing the bear, you begin to question how this animal gained such a powerful and demonic energy.\n";
                break;
            default:
                std::cout << "Invalid response. Moving on.\n";
                break;  
        }

        std::cout << "An encounter with the deadly beast has become unavoidable. What is your next move?\n\n";

        std::cout << "   1) Face your fear and fight to subdue the beast.\n";
        std::cout << "   2) Avoid the bear's attacks, until you can learn its weakness or reason for its unnatural state.\n";
        std::cout << "   3) Use slash and run tactics to bleed the monster out until it collapses.\n";

        std::cin >> answer;

        // Need a dice roll higher than 70% of dice size for move to be successful, result = 1
        // Otherwise, result = 0 and user must try again, but loses hp points
        while (result == 0) {

            // Dice Roll
            srand (time(NULL));
        
            roll = dice(dice_size);

            // std::cout << "You rolled a " << roll <<" on a " << dice_size << "-sided die.\n";

            // Need successful roll to move forward
            if (roll > (dice_size * (3/4))) {
                std::cout << "Success!\n\n";
                result = 1;
             
            }
            else {
                hp -= 20;
                std::cout << "You took damage.\n" <<
                "Current HP = " << hp << "/ 100. You try again.\n\n";
                if (hp == 0) {
                    // If player lost all hp, they must rerun code to try again
                    std::cout << "You did not survive the previous challenge. Please rerun program to try again.\n\n";   

                    return 0;
                }
            }
        }    
        result = 0;
        switch (answer) {
            case 1: 
                king += 1;
                std::cout << "You and " << name << " won, but the bear did not survive the battle.\n" << 
                "Before you depart, you bury the bear and feel a calmness in the air.\n\n";
                break;
            case 2: 
                sage += 1;
                std::cout << "You see an arrow wound on the bar that seems to be at the center of the mutated flesh. You and " << name << 
                " work together to distract the bear, and you pull it out. The bear shrieks, but then slowly reverts to a seemingly normal bear." <<
                " The bear looks confused, but normal now, and trots back into the woods, likely grateful for your encounter.\n\n";
                break;
            case 3: 
                slayer += 1;
                std::cout << "After the bear collapses, you begin dissecting, while " << name << " rips off a healthy looking leg to eat.\n" <<
                "You find an arrow in its back that has an ominous energy, but it slowly dissipates. Another hunter is near, one with a strange power.\n\n";
                break;
            default:
                std::cout << "Invalid response. Moving on.\n";
                break;  
        }

    
        // Conditional statement to tally points and choose ending:
        int max = 0;
        std::string winner;
        std::string ending;
    

        if (king > max) {
            max = king;
            winner = "King";
            ending = "You have proven to be a righteous leader. The people of the land have chosen you to lead them.\n";
        }

        if (sage > max) {
            max = sage;
            winner = "Sage";
            ending = "You have proven to be a wise and peaceful soul. The elders grant you their highest honor among the clan.\n";
        } 

        if (slayer > max) {
            max = slayer;
            winner = "Slayer";
           ending = "You have proven to be the most feared warrior. Children will be told of your legend as a warning to never incur your wrath.\n";
        }

        std::cout << "\n" << "Congratualtions, you have become known as the Dragon " << winner << "!\n\n";

        std::cout << "Thank you for embarking on this adventure story game.\n";

        return 0;

        }

    // If player lost all hp, they must rerun code to try again
    std::cout << "You did not survive the previous challenge. Please rerun program to try again.\n";        

    return 0;
}