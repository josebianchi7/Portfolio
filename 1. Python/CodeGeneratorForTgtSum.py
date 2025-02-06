def dft_helper(target, codes, curr_code, start):
    """
    Helper function for digits for target
    """
    # base case
    if len(curr_code) == 4:
        if target == 0:
            valid_code = curr_code[:]
            codes.append(valid_code)
        return

    for dig in range(start, 10):
        if dig <= target:
            curr_code.append(dig)
            dft_helper(target - dig, codes, curr_code, dig)

            # backtrack
            curr_code.pop()


def digits_for_target(S):
    """
    Given an integer S, find all ways to get any of
    the 10 digits (0-9) to sum to S, using 4 digits. 
    Take away start variable to generate all permuations
    of solutions. 
    """
    solutions = []
    dft_helper(S, solutions, [], 0)
    print(solutions)
    return len(solutions)


# print(digits_for_target(2))
# print(digits_for_target(35))
print(digits_for_target(11))
