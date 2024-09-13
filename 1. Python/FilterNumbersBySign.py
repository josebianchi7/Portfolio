
def plusMinus(arr):
    """
    Given an array of integers, calculate the ratios of its elements
    that are positive, negative, and zero. Print the decimal value
    of each fraction on a new line with 6 places after the decimal.
    :param arr:
    :return: Three decimal values on their own lines
    (1. Ratio of Positives, 2. Ratio of Negatives, 3. Ratio of Zeros)
    """
    arr_size = len(arr)
    neg_counter = 0
    pos_counter = 0
    zero_counter = 0
    for element in arr:
        if element == 0:
            zero_counter += 1
        elif element < 0:
            neg_counter += 1
        elif element > 0:
            pos_counter += 1

    # Calculate Ratios
    pos_ratio = pos_counter / arr_size
    neg_ratio = neg_counter / arr_size
    zero_ratio = zero_counter / arr_size

    # Print values with 6 places after decimal using f-string
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


if __name__ == '__main__':
   arr = [-4, 3, -9, 0, 4, 1]

   plusMinus(arr)
