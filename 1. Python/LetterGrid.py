# Author: Jose Bianchi
# GitHub username: josebianchi7

def grid_sort(grid):
    """
    Given a grid of letters, rearrange elements of each row
    alphabetically, ascending. Determine if columns are also in
    ascending alphabetical order, from top to bottom.
    
    param grid: array of characters, representing a grid,
    where each element is a string representing a row.
    
    return string: YES if columns are ascending alphabetical,
    otherwise NO
    """
    # Check if rows are ascending, by converting row strings in row lists
    # with letters from string as elements in row_list
    for num in range(len(grid)):
        row_string = grid[num]
        row_list = []
        for i in range(len(row_string)):
            row_list.append(row_string[i])

        row_list = sorted(row_list)
        # Once a row is sorted in ascending order, convert back to string
        # And push back into grid
        grid[num] = ''.join(row_list)

    # Then check columns:
    a_row = grid[0]
    max_column = len(a_row) - 1
    for column in range(max_column+1): 
            
        row = 0
        while row < (len(a_row) - 1):
            curr_c_char = grid[row][column]
            next_c_char = grid[row+1][column]
            
            if next_c_char < curr_c_char:
                return 'NO'
            
            row += 1

    # If column tester does not find an issue, return 'YES'
    return 'YES' 
     

if __name__ == '__main__':
    grid1 = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
    result1 = gridChallenge(grid1)
    print(result1)
