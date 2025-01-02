import random

# Linear Search
def linear_search(arr, target: object) -> bool:
    """
    Iterate through array to find if given target is in array.
    Return True if found, and False otherwise. Time complexity = O(n).

    :param arr: unsorted array
    :param target: object that may be in arr.

    :return bool: True if object is in array, False otherwise.
    """
    for i in range(len(arr)):
        currElement = arr[i]
        if target == currElement:
            return True
    return False      



# Binary Search
def binary_search(arr, target: object) -> bool:
    """
    Conduct a binary search in a SORTED array, by iteratively testing 
    midpoint elements. Return True if found, and False otherwise. 
    Time complexity = O(log (n)).

    :param arr: sorted array
    :param target: object that may be in arr.

    :return bool: True if object is in array, False otherwise.
    """
    start = 0
    end = len(arr) - 1
    mid = (start + end)// 2
    midElement = arr[mid]
    while target != midElement:
        # If target is less than mid, move end pointer to index before mid
        if target < midElement:
            end = mid - 1
            # Recalculate new midElement
            mid = (start + end)// 2
            midElement = arr[mid]

        # If target is greater than mid, move start pointer to index after mid
        elif target > midElement:
            start = mid + 1
            # Recalculate new midElement
            mid = (start + end)// 2
            midElement = arr[mid]

        # Target is not in array if start and end cross over each other
        if start > end:
            return False    

    return True


if __name__ == '__main__':
    arr1 = [1, 0]
    arr2 = [1]
    arr3 = [9, 8, 5, 7, 2, 6, 1]
    arr4 = []
    for i in range(10):
        arr4.append(random.randint(0, 100))
    arr5 = []
    for i in range(50):
        arr4.append(random.randint(-100, 100))   
    arr6 = ["bear", "cat", "dog", "monkey", "octopus"]     

    print(linear_search(arr6, "octopus"))    
    print("\n")