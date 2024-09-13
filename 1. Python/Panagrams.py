def pangrams(s):
    """
    A Pangram is a string that contains every letter of the alphabet.
    Given a sentence, determine if every letter in the English alphabet
    is used. Ignore case. Return string
    :param s: sentence string.
    :return: string response "pangram" or "not pangram" based
    on result.
    """
    # Create list with alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']

    # Convert all letters in input string to lowercase
    lower_s = s.lower()
    sentence_size = len(lower_s)

    # Iterate through input string, compare letters to alphabet list
    for letter_count in range(sentence_size):
        curr_s_letter = lower_s[letter_count]

        for letter in alphabet:
            # First time string letter matches alphabet letter,
            # Remove (cross out) letter from alphabet
            if curr_s_letter == letter:
                alphabet.remove(letter)

            # If alphabet length reaches zero, return "pangram"
            if len(alphabet) == 0:
                return "pangram"
            # If string letter is not in alphabet, it has already been
            # removed and function can move onto next letter

    # At end of iteration of input string, alphabet length is not zero,
    # return "not pangram"
    if len(alphabet) > 0:
        return "not pangram"


if __name__ == '__main__':
    s1 = "We promptly judged antique ivory buckles for the prize"
    s2 = "The quick brown fox jumps over the lazy dog"

    print(pangrams(s1))
    print(pangrams(s2))
