# Author: Jose Bianchi
# GitHub username: josebianchi7
# Description: Code with function that takes name of a text file with list of numbers, and will sum numbers from file.
# Function will then write over designated file to new result.

import os

def file_sum(num_list_filename):
    """Function that takes list of numbers with one per line and writes a new text file with sum of numbers"""
    
    # Get the directory of input file
    current_dir = os.path.dirname(__file__) if __file__ != '' else os.getcwd()
    
    # Get full path to the input file
    input_file_path = os.path.join(current_dir, num_list_filename)
    
    # Check if the input file exists
    if os.path.exists(input_file_path) is None:
        raise FileNotFoundError(f"The file '{num_list_filename}' does not exist in the current directory.")
    
    # Initalize starting sum:
    total_sum = 0      

    # Conduct summation or other defined calculation:
    with open(input_file_path, 'r') as infile:                # Use 'r' to read file
                        
        for num in infile:
            total_sum += float(num.strip())                     # Iterate over each line and add float value to total_sum

        output_file_path = os.path.join(current_dir, 'sum.txt')
        with open(output_file_path, 'w') as outfile:            # Use 'w' to write new file as human-readable
            outfile.write(str(total_sum) + '\n')                # Convert float to string to write total_sum to new file

        print(total_sum)    


if __name__ == '__main__':
    file_sum('numbers_list.txt')