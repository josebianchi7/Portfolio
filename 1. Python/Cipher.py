# Author: Jose Bianchi
# GitHub username: josebianchi7


def letter_shifter(s, k):
    """
    Given a message string, s, shift each letter down the alphabet by k.
    Skip any symbols. If a letter passes 'z' during shift, restart at 'a'
    param s: string message
    param k: letter shift factor
    """
    # Method 1: catalog all letters, create empty string,
    letters_upper = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
    
    letters_lower = []
    for letter in letters_upper:
        letters_lower.append(letter.lower())

    max_index = len(letters_upper) - 1
    ciper_message = ''

    for num in range(len(s)):
        char = s[num]

        # If character is uppercase, check uppercase letters
        if char.isupper():
            old_index = letters_upper.index(char)

            # Shift index, then verify new index is still in array
            new_index = old_index + k
            while new_index > max_index:
                new_index -= 26

            new_char = letters_upper[new_index]

        # for lowercase letters
        elif char.islower():
            old_index = letters_lower.index(char)
            new_index = old_index + k
            while new_index > max_index:
                new_index -= 26

            new_char = letters_lower[new_index]

        #otherwise: character must be a symbol and can be added to return string as is
        else:
            new_char = char
        
        # Add shifted character to return string
        ciper_message += new_char

    return ciper_message       


if __name__ == '__main__':
    string1 = "There's-a-starman-waiting-in-the-sky"
    result1 = letter_shifter(string1, 3)
    print(result1)
    string2 = "Hello_World!"
    result2 = letter_shifter(string2, 4)
    print(result2)
    string3 = "Peanut-Butter__Zues+Unicorn_Whale"
    result3 = letter_shifter(string3, 8)
    print(result3)
    string4 = "www.abc.xy"
    result4 = letter_shifter(string4, 87)
    print(result4)
