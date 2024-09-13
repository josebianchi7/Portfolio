
def flippingMatrix(matrix):
    """
    Given a matrix (array with sub-arrays corresponding to rows in matrix),
    with even and an equal amount of rows and columns.
    Each cell contains an integer, and the goal is to maximize the sum of
    elements in the n x n sub-matrix located in the upper left quadrant of the
    matrix, for a matrix of total size = 2n.
    :param matrix:
    :return: max possible sum
    """
    matrix_size = len(matrix)
    
    quad_size = matrix_size // 2
    
    # # Matrix size 1 case, not needed for this code, but if needed later, only one possible solution
    # if matrix_size == 1:
    #     return matrix[0][0]
    
    # If matrix is 2 x 2, the largest element is the max sum
    if matrix_size == 2:
        max = matrix[0][0]
        for row in range(matrix_size):
            for column in range(matrix_size):
                element = matrix[row][column] 
                
                if element > max:
                    max = element
                    
        return max 
    
    comp_arr = []
    max_quad = []
    end_row = matrix_size
    # Amount of element that need to be compared = amount of rows
    for start_row in range(quad_size):

        end_row -= 1
        end_column = matrix_size - 1
        
        for start_column in range(quad_size):
                        
            # Each element will only have 3 other comparison elements

            element1 = matrix[start_row][start_column]
            element2 = matrix[start_row][end_column]
            element3 = matrix[end_row][start_column]
            element4 = matrix[end_row][end_column]

            comp_arr.append(element1)
            comp_arr.append(element2)
            comp_arr.append(element3)
            comp_arr.append(element4)

            # Find max of current transfer points
            max_val = element1
            for element in comp_arr:
                if element > max_val:
                   max_val = element

            # Append max to final quad solution array
            max_quad.append(max_val)
            comp_arr = []

            # Decrement end pointer to move to next transfer further in matrix
            end_column -= 1 

    # Find new max_sum
    max_sum = 0
    for value in max_quad:
        max_sum += value

    return max_sum

ex1 = [[1, 2], [3, 4]]
ex2 = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

print(flippingMatrix(ex2))
