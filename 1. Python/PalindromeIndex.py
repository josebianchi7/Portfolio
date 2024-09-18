# Author: Jose Bianchi
# GitHub username: josebianchi7

def palindromeIndex(s):
    """
    Given a string of lowercase letters, s,
    determine index of a character to be removed to make
    resulting string a palindrome.
    If word is already a palindrome, return -1
    Otherwise return index of string letter to remove from reverse side
    """
    s_list = [a for a in s]

    rev_s_list = s_list[::-1]

    # First test if current argument is a palindrome
    if s_list == rev_s_list:
        return -1

    # Find first non-match between s and rev_s   
    for index in range(len(s_list)):
        if s_list[index] != rev_s_list[index]:

            # Create test without current index, is passes, return current index
            test_list = s_list[:]
            test_list.pop(index)
            rev_test_list = test_list[::-1]
            if rev_test_list == test_list:
                return index 
            else:
                return len(s_list) - index - 1



if __name__ == '__main__':
    string1 = 'aaabhgftlfghbaaa'
    result1 = palindromeIndex(string1)
    print(result1)

