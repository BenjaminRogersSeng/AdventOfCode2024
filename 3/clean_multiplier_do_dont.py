import os, re

input_string = ""

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file, 'r') as file:
    input_string = file.read()

matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_string)
mul_enabled = True  
results = []

# Process matches in order
for match in matches:
    if match == "do()":
        mul_enabled = True
    elif match == "don't()":
        mul_enabled = False
    elif match.startswith("mul(") and mul_enabled:
        # Extract numbers from the mul() instruction
        a, b = map(int, re.findall(r"\d+", match))
        results.append(a * b)
print(sum(results))