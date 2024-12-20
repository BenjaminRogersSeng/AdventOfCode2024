import os, re

input_string = ""
final_calc = 0

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file, 'r') as file:
    input_string = file.read()

matches = re.findall(r"mul\((\d+),(\d+)\)", input_string)

results = [(int(a) * int(b)) for a, b in matches]
print(sum(results))