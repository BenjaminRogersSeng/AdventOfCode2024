import os, re

x_width = 0
y_width = 0

matrix = []

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file, 'r') as file:
    for line in file:
        x_width = len(line)
        y_width += 1
        matrix.append(line.strip('\n'))
        
def split_matrix_into_3x3_chunks(matrix):
    n = len(matrix)       # Number of rows
    m = len(matrix[0])    # Number of columns
    chunk_size = 3

    chunks = []

    # Iterate over each starting position for a 3x3 matrix
    for start_row in range(n - chunk_size + 1):
        for start_col in range(m - chunk_size + 1):
            # Extract the 3x3 submatrix
            submatrix = [
                matrix[i][start_col:start_col + chunk_size]
                for i in range(start_row, start_row + chunk_size)
            ]
            chunks.append(submatrix)

    return chunks
        
def flatten_slices(matrix):
    n = len(matrix)       # Number of rows
    m = len(matrix[0])    # Number of columns

    diagonals = []
    anti_diagonals = []
    result = []

    # Main diagonals
    for d in range(n + m - 1):
        diagonal = []
        for row in range(n):
            col = d - row
            if 0 <= col < m:
                diagonal.append(matrix[row][col])
        if diagonal and len(diagonal) == 3:
            result.append(diagonal)

    # Anti-diagonals
    for d in range(-(n - 1), m):
        anti_diagonal = []
        for row in range(n):
            col = row + d
            if 0 <= col < m:
                anti_diagonal.append(matrix[row][col])
        if anti_diagonal and len(anti_diagonal) == 3:
            result.append(anti_diagonal)
    return result

def check_for_xmas(submatrix):
    counter = 0
    for sublist in submatrix:
        # print(''.join(sublist))
        if re.search(r"MAS|SAM", ''.join(sublist)): # regex accounts for both forward and backward
            counter += 1
            
    return 1 if counter == 2 else 0

counter = 0

matrix = split_matrix_into_3x3_chunks(matrix)
for submatrix in matrix:
    submatrix = flatten_slices(submatrix)
    # print(submatrix)
    counter += check_for_xmas(submatrix)
    
print(counter)