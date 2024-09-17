def twoArrays(k, A, B):
    """
    Given two arrays, A and B, permute (reorder) them into A' and B',
    such that all same indexed elements from A' and B' can be summed to be
    greater than or equal to input k.
    Elements in A and B will be greater than or equal to zero.
    Return YES if such permutations to satisfy the target relation exist.
    Otherwise, return NO.

    :param k: target integer
    :param A: array of integers
    :param B: array of integers
    :return: YES or NO based on if inputs satisfy target relation or not.
    """
    # Create variables
    arr_size = len(A)

    # Sort both arrays and reverse one
    A[:] = reversed(sorted(A[:]))
    B[:] = sorted(B[:])

    # Test if current sum is greater than or equal to k
    test_index = 0
    while test_index < arr_size and A[test_index] + B[test_index] >= k:
        curr_sum = A[test_index] + B[test_index]
        # If last element sum satisfies target relation, return YES
        if test_index + 1 == arr_size:
            return "YES"

        # If true, iterate to next elements in permutation
        test_index += 1

    # If test fails, return NO
    return "NO"


a0 = [0, 1]
b0 = [0, 2]
k0 = 1

a1 = [2, 1, 3]
b1 = [7, 8, 9]
k1 = 10

a2 = [1, 2, 2, 1]
b2 = [3, 3, 3, 4]
k2 = 5

a3 = [0, 1, 2, 3, 4, 7, 6, 5, 4, 3]
b3 = [4, 3, 5, 6, 7, 4, 3, 3, 2, 1]
k3 = 7

a4 = [3, 4, 2, 1, 0, 3, 4, 5, 6, 7]
b4 = [4, 3, 5, 6, 7, 4, 3, 3, 2, 1]
k4 = 7


print(twoArrays(k0, a0, b0))
print(twoArrays(k1, a1, b1))
print(twoArrays(k2, a2, b2))
print(twoArrays(k3, a3, b3))
print(twoArrays(k4, a4, b4))
