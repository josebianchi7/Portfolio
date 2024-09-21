# Author: Jose Bianchi
# GitHub username: josebianchi7

def dynamicArray(n, queries):
    """
    Declare an array that contains n empty arrays.
    Declare an integer, lastAnswer, set to 0
    
    There are 2 types of queries, given as an array of strings to be parsed
        1. Query 1 x y
            a. idx = (x XOR lastAnswer) % n
            b. Append the integer y to arr[idx]
        2. Query 2 x y
            a. idx = (x XOR lastAnswer) % n 
            b. Assign the value arr[idx][y%size(arr[idx])] to lastAnswer
            c. Store new value of lastAnswer to an answers array
               
    param n: number of empty array to initialize arr
    param queries: array of strings with 3 spaced instegers
    
    return answers_arr: result of each type 2 query in order
    """
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answer_arr = []
    
    for i in range(len(queries)):
        query = queries[i]
        
        if query[0] == 1:
            x = query[1]
            idx = (x ^ lastAnswer) % n
            y = query[2]            
            inner_arr = arr[idx]
            inner_arr.append(y)
            
            
        elif query[0] == 2:
            x = query[1]
            idx = (x ^ lastAnswer) % n
            y = query[2]
            index = y % len(arr[idx])
            lastAnswer = arr[idx][index]
            answer_arr.append(lastAnswer)

    return answer_arr   
    

if __name__ == '__main__':
    q1 = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
    print(dynamicArray(2, q1))
