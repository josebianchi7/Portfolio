# Author: Jose Bianchi
# GitHub username: josebianchi7
# Description: Code times how long sorting functions take to run as with decorator and outputs graph showing efficiency 
#   of functions with various data sizes.


import time
import random
# from matplotlib import pyplot
from functools import wraps


def sort_timer(func):
    """Decorator function. Adds behavior of timing in seconds for other functions to run."""
    @wraps(func)        # decorator that uses wraps() function from functools to apply to other functions
    def time_wrapper(*args, **kwargs):
        initial_time = time.perf_counter()        # additional behavior before function call
        func(*args, **kwargs)
        final_time = time.perf_counter()          # additional behavior after function call
        return final_time - initial_time        # wrapper function returns elapsed time
    return time_wrapper


@sort_timer
def bubble_sort(a_list):
    """Sorts a_list in ascending order using bubble sort method"""
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """Sorts a_list in ascending order using insertion sort method"""
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def make_lists_of_sort_times(sort_function1, sort_function2):
    """
    Accepts two sort functions and an integer list of lengths of times.
    Creates two lists to record times sort functions take to sort same lists.
    Creates duplicate random integer lists to be sorted by sort functions of various lengths.
    Returns tuple of two respective lists of run times per function,
    after completing list of 10 time data points per algorithm.
    """
    lengths_list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    function1_times = []
    function2_times = []

    # For a length in lengths_list, generate random integer list with values in range [1,1000]
    for length in lengths_list:
        random_num_list = [random.randint(1, 1000) for num in range(length)]
        list_copy = random_num_list.copy()                  # copy list for other sort function to sort

        time_values1 = sort_function1(random_num_list)      # Time variable returned by decorated function on function1
        function1_times.append(f"{time_values1:.5f}")       # Append integers with only 5 digits after decimal   

        time_values2 = sort_function2(list_copy)            # Time variable returned by decorated function on sort function2
        function2_times.append(f"{time_values2:.5f}")


    print('sort function 1 runtimes :')
    print(function1_times)
    print('sort function 2 runtimes :')
    print(function2_times)

    return 


def main():
    """
    Main function that will only run when this file name is run
    and not when functions are called by another file.
    """
    make_lists_of_sort_times(bubble_sort, insertion_sort)

if __name__ == '__main__':
    main()
