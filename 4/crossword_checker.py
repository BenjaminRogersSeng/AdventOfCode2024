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
        
def flatten_slices(matrix):
    n = len(matrix)       # Number of rows
    m = len(matrix[0])    # Number of columns

    result = []

    # Horizontal slices (rows)
    for row in matrix:
        row = list(row)
        result.append(row)

    # Vertical slices (columns)
    for col in range(m):
        result.append([matrix[row][col] for row in range(n)])

    # Main diagonals
    for d in range(n + m - 1):
        diagonal = []
        for row in range(n):
            col = d - row
            if 0 <= col < m:
                diagonal.append(matrix[row][col])
        if diagonal:
            result.append(diagonal)

    # Anti-diagonals
    for d in range(-(n - 1), m):
        anti_diagonal = []
        for row in range(n):
            col = row + d
            if 0 <= col < m:
                anti_diagonal.append(matrix[row][col])
        if anti_diagonal:
            result.append(anti_diagonal)

    
    return result

def split_sublist_into_chunks(sublists, chunk_size, step_size):
    chunks = []
    for sublist in sublists:
        if len(sublist) >= chunk_size:
            chunks.extend(
                [sublist[i:i + chunk_size] for i in range(0, len(sublist) - chunk_size + 1, step_size)]
            )
    return chunks

result = flatten_slices(matrix) 
result = split_sublist_into_chunks(result, 4, 1)
# print(result)

def check_for_xmas(matrix):
    counter = 0
    for sublist in matrix:
        # print(''.join(sublist))
        if re.search(r"XMAS|SAMX", ''.join(sublist)): # regex accounts for both forward and backward
            counter += 1
            
    return counter
        
print(check_for_xmas(result))