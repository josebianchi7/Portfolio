# Author: Jose Bianchi
# GitHub username: josebianchi7

def maxMin(k, arr):
    """
    Create a subset, of size k, using elements from arr.
    Test formula:
        max(arr') - min(arr') = u, where u = 'unfairness'     
    
    param k: subset size
    param arr: list of integers
    
    return min  u
    """
    # Need arr sorted and a variable for max index of subset
    arr.sort()
    k_max = k - 1

    curr_u = max(arr) - min(arr)

    # Increment elements in arr to find new unfairness
    for num in range(len(arr)-k_max):
        arr_element_min = arr[num]
        arr_element_max = arr[num+k_max]

        # Test if new unfairness is less than curr_u
        new_u = arr_element_max - arr_element_min
        if new_u < curr_u:
            curr_u = new_u
    
    return curr_u


arr1 = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
result = maxMin(4, arr1)
print(result)   

arr2 = [4504, 1520, 5857, 4094, 4157, 3902, 822, 6643, 2422, 7288, 8245, 9948, 2822, 1784, 7802, 3142, 9739, 5629, 5413, 7232]
result2 = maxMin(5, arr2)
print(result2)   
        