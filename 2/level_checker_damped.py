import os

reports = []

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file, 'r') as file:
    for line in file:
        line = line.split('\n')[0]
        levels = list(map(int, line.split(' ')))
        reports.append(levels)
        
def permutations(levels):
    return [[x for j, x in enumerate(levels) if j != i] for i in range(len(levels))]

print(permutations([1,2,3,4]))
    
def check(levels):
    diff = list(map(lambda x: x[1] - x[0], zip(levels, levels[1:])))
    magnitude_check = all(abs(diff[i]) <=3 for i in range(len(levels) - 1))
    rising_check = all(map(lambda x: x > 0, diff))
    falling_check = all(map(lambda x: x < 0, diff))
    return magnitude_check and (rising_check or falling_check)

safe_count = 0

for levels in reports:
    safe_count += 1 if any(check(p) for p in permutations(levels)) else 0
print(safe_count, '/', len(reports), 'are safe')