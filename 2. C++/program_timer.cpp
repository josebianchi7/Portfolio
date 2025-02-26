/*
Name: Jose Bianchi 
GitHub username: josebianchi7
Description: file contains function that can record execution time of a program. 
To accurately time function execution, must insert function at specified point in 
function or ensure function file is compiled with this file.
*/

#include <iostream>         // iostream affords input and output via the console
#include <string>           // includes string methods            
#include <stdlib.h>         // includes functions for program termination, resource cleanup, and random using rand() and srand()
#include <ctime>            // includes functions for processing time, system time, and run time of a program
#include <chrono>           // allows use of clock time in miliseconds

#include "my_functions.hpp" // header file for various function calls


int main() {

    // Record current time as start time for called function:
    std::chrono::high_resolution_clock::time_point start = std::chrono::high_resolution_clock::now();
    
    //Insert function to be measured here:
    is_palindrome("madam");

    // Record stop time and measure difference after function has completed execution, assign result to time_span:
    std::chrono::high_resolution_clock::time_point end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> time_span = end - start;

    // Print result:
    std::cout << "Function took " << time_span.count() << " miliseconds to run.\n";

    return 0;
}