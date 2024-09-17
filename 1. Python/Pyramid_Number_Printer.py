# Author: Jose Bianchi
# GitHub username: josebianchi7
# Long Code Description: The function pyramid_printer accepts one argument of type integer.
# The function must print from 1 to the integer argument and back to one, but
# Each line contains its number printed the same amount of times as the number separated by
# an asterisk (*).Example: line 2: 2*2, line 3: 3*3*3, line 4: 4*4*4*4, then it repeats in 
# descending order printing the max line again.

def pyramid_printer(n):
    """
    Given an integer argument, print a pyramid from 1 to n, with repeated numbers
    on each line equal to n, but separated by an asterisk. 1 < n <= 100.
    param n: integer argument that represent max print integer
    Function does not return an object, but will print a number pyramid.
    """

    # Since 1 will never have an asterisk, print it outside of loop
    print("1")

    # For going up the pyramid, from 2 to n (inclusive), loop to add n and a * to the string
    for num in range(2, n+1):
        
        # Reset empty string to hold current pattern
        pattern = ""
        
        counter = 0
        while counter < num - 1:
            pattern = pattern + str(num) + "*"
            counter += 1

        # To ensure pattern ends with number and not asterisk, add one more num after loop
        pattern = pattern + str(num)    

        print(pattern)    

    # For going down the pyramid, from n to 2 (inclusive):
    for num in range(n, 1, -1):
        
        # Reset empty string to hold current pattern
        pattern = ""
        
        counter = 0
        while counter < num - 1:
            pattern = pattern + str(num) + "*"
            counter += 1

        # To ensure pattern ends with number and not asterisk, add one more num after loop
        pattern = pattern + str(num)    

        print(pattern)    

    # Again, print last 1 outside loop for simplicity
    print("1")

result = pyramid_printer(1)
