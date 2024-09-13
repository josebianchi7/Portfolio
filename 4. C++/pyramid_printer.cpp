/*
Name: Jose Bianchi 
GitHub username: josebianchi7
Current corresponding execution filename: pyramid.exe

Long Code Description: The function pyramid_printer accepts one argument of type integer.
The function must print from 1 to the integer argument and back to one, but
Each line contains its number printed the same amount of times as the number separated by
an asterisk (*).Example: line 2: 2*2, line 3: 3*3*3, line 4: 4*4*4*4, then it repeats in 
descending order printing the max line again.
*/

// import necessary libraries:
#include <iostream>           // iostream affords input and output via the console
#include <string>

// Begin main function:
int main() {

    int max_num = 1;
    std::cout << "Hello! ";
    std::cout << "Please input an integer between 1 and 100 for me to print a pyramid to: \n";

    std::cin >> max_num;

    // Print beginning 1 outside of loop for convenience, since it will never need an asterisk
    std::cout << "\n1\n";

    // Going up pyramid loop:
    // Start at 2 for print integer, end at max_num (inlcusive), increment integer for print (i)
    for (int i = 2; i < (max_num + 1); i++) {
        
        // Repeat printing of integer amount of times equal to print integer - 1, so we do not end with asterisk
        int counter = 0;
        while (counter < (i - 1)) {

            std::cout << std::to_string(i) << "*";
            counter++;
        }

        // Final printing of current integer for current line, then go to next line and next greater integer
        std::cout << std::to_string(i) << "\n";

    }  

    // Going down pyramid loop, start at input argument, stop so last print integer is 2, decrement print integer
        for (int i = max_num; i > 1; i--) {
        
        int counter = 0;
        while (counter < (i - 1)) {

            std::cout << std::to_string(i) << "*";
            counter++;
        }

        std::cout << std::to_string(i) << "\n";

    }  

    // Print ending 1 outside of loop for convenience, since it will never need an asterisk
    std::cout << "1\n\n";

    // Farewell statement:
    std::cout << "Thank you very much for trying this code.\n";

    return 0;

}
