# Author: Jose Bianchi
# GitHub username: josebianchi7
# Description: The function below, permute(), can accept a string, an array of string characters, or an array of single integers,
# and will calculte how many possible permutations can be made, using a factorial calculation, and print each arrangement.
# The function will produce variables for necessary properties of object input, and an empty array to store results.
# These new objects become arguments for the helper function, permute_helper(). 
# Using recursion and a for loop, the permute_helper() creates a tree, to reeach the end of a 
# branch, then backs up one step, makes a swap, and increments back up tree to add new permutation to an array.
# It will reverse its swap after complete, (backtracks), then will go down a new branch, and if possible, a new leaf on
# that branch using the for loop. 



def permute_helper(char_array, start, end, permutations):
    """
    Helper function to handle recursion, create new permutations, and append to result array.
    All permutations are created once last index is swapped with first index.
    """
    # Every array_size - 1 function call, a new permutation will be added
    if start == end:
        string_obj = ''.join(char_array)
        permutations.append(string_obj)
    else:
        # Increment char_array variable (i) to stop at last index
        for i in range(start, end):

            # Swaps begin when end of current branch is reached
            char_array[start], char_array[i] = char_array[i], char_array[start]
            
            # Function call to get to end of current branch, but once start == end, stack can remove that function,
            # And go to previous function call on stack
            permute_helper(char_array, start+1, end, permutations)
            
            # After a successful ending branch is reached, reset array to previous permutation before swap,
            # then in last stack function call, continue for loop, to swap a lower start index with current i  
            char_array[start], char_array[i] = char_array[i], char_array[start]  # backtrack
           

def permute(object):
    """
    Given an object (string or array), log all possible permutations into list,
    and print all permutations from list.

    param object: string or array with string character or single digit integers
    
    return max_perm: total number of possible permutations
    """
    permutations_list = []

    object_size = len(object)

    max_perm = 1
    if object_size> 2:
        counter = 2
        while counter <= object_size:
            max_perm *= counter
            counter += 1

    print("Total possible permutations:", max_perm)        
        
    # If object is a string, convert each letter/ character into an array element:
    if type(object) is str:      

        letters = []
        for char_index in range(len(object)):
            letters.append(object[char_index])

        # Call recursive function to add permutations to result list
        permute_helper(letters, 0, object_size, permutations_list)

        # Print permuations in final list
        for arrangement in permutations_list:
            print(arrangement)

        return

    # If object is already of list type and if with integers:
    elif type(object) is list:

        if type(object[0]) is int:
            string_num_arr = []
            for index in range(object_size):
                string_num_arr.append(str(object[index]))

            permute_helper(string_num_arr, 0, object_size, permutations_list)

            # Print permuations in final list
            for arrangement in permutations_list:
                print(arrangement)
            return

        # If object argument elements are strings, proceed to call recursive function
        permute_helper(object, 0, object_size, permutations_list)

        # Print permuations in final list
        for arrangement in permutations_list:
            print(arrangement)

        return
    

# Test cases:
if __name__ == '__main__':
    result0 = permute("a")
    result1 = permute("abcd")    
    # arr1 = [1, 2, 3, 4, 5]
    # result2 = permute(arr1)
    # arr2 = ['a', 'b', 'c', 'd', 'e', 'f']
    # result3 = permute(arr2)
