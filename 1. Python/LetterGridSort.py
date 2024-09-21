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
    for row in range(len(grid)):
        row_letters = sorted(list(grid[row])) 
        # Once letters are sorted in ascending order, push back into grid as string                   
        grid[row] = ''.join(row_letters)       
        
    # Check columns for total columns in any given row, in this case, first row    
    for column in range(len(grid[0])):
        # Increment rows using j
        j = 0
        while j < len(grid):
            column_letter = grid[j][column]
            next_col_letter = grid[j+1][column]
            if next_col_letter < column_letter:
                return 'NO'    
            j+=1
            
    # If all columns pass check, return YES
    return 'YES'


if __name__ == '__main__':
    grid1 = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
    print(grid_sort(grid1))
    grid2 = ['abc', 'lmp', 'qrt']

    grid3 = ['mpxz', 'abcd', 'wlmf']

    grid4 = ['abc', 'hjk', 'mpq', 'rtv']
    print(grid_sort(grid4))
