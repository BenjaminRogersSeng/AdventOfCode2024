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

def check_for_xmas(matrix, x, y):
    pattern = re.compile(r"XMAS|SAMX")
    hori = re.findall(r"XMAS|SAMX", ''.join([matrix[y][i] for i in range(x_width)]))
    vert = re.findall(r"XMAS|SAMX", ''.join([matrix[i][x] for i in range(y_width)]))
    diag1 = re.findall(r"XMAS|SAMX", ''.join([matrix[i][j] for i, j in zip(range(y_width), range(x_width))]))
    diag2 = re.findall(r"XMAS|SAMX", ''.join([matrix[j][i] for i, j in zip(range(y_width), range(x_width))]))

    return len(hori) + len(vert) + len(diag1) + len(diag2)
        
print(check_for_xmas(matrix, x_width - 1, y_width - 1))