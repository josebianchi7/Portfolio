/*
Name: Jose Bianchi 
GitHub username: josebianchi7
Current corresponding execution filename: palindrome.exe

Description: Function included to test if a string word is a palindrome, then main function will capture user
input and test using palindrome function to return string with determination.
*/

#include <iostream>
#include <string>

// Define is_palindrome() here:
bool is_palindrome(std::string text) {

    // Initiate string to hold reverse of word argument  
    std::string rev_text;

    // Iterate from end of word to beginning and push letters into rev_text
    for (int i = (text.size() - 1); i >= 0; i--) {
        rev_text += text[i];
    }

    // If palindrom, return true, otherwise return false
    if (text == rev_text) {
        return true;
    }
    else {
        return false;
    }
}

int main() {
  
    std::string test_word;
    std::cout << "Hello, please submit a word and I will let you know if it is a palindrome.\n";
    std::cin >> test_word;

    if (is_palindrome(test_word) == true) {
        std::cout << "Yes, " << test_word << " is a palindrome!\n";
    }
    else {
        std::cout << "No, " << test_word << " is not a palindrome.\n";
    }
    
    return 0;
}