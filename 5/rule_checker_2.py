import os
import functools
        
input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file, 'r') as file:
	raw_rules, raw_updates = file.read().split('\n\n')
	
RULES = [list(map(int, rule.split('|'))) for rule in raw_rules.split('\n')]
UPDATES = [list(map(int, update.split(','))) for update in raw_updates.split('\n')]

# print(RULES)
# print(UPDATES)

KEY_IS_LESS_THAN = {}
for rule in RULES:
    for i in range(len(rule) - 1):
        if rule[i] not in KEY_IS_LESS_THAN:
            KEY_IS_LESS_THAN[rule[i]] = set()
        KEY_IS_LESS_THAN[rule[i]].add(rule[i + 1])

# print(KEY_IS_LESS_THAN)

def is_less_than(a, b):
    if a not in KEY_IS_LESS_THAN:
        return False
    return b in KEY_IS_LESS_THAN[a] 

def sort_pages(a, b):
    if is_less_than(a, b):
        return -1
    elif is_less_than(b, a):
        return +1
    else:
        return 0
    
def check_sorted(update):
    for i in range(len(update) - 1):
        if not is_less_than(update[i], update[i + 1]):
            return False
    return True

def get_middle_number(update):
    return update[len(update) // 2]

counter = 0
counter_corrected = 0

for update in UPDATES:
    if check_sorted(update):
        # print(update, " - correct")
        counter += get_middle_number(update)
    else:
        # print(update, " - incorrect")
        corrected_update = sorted(update, key=functools.cmp_to_key(sort_pages))
        counter_corrected += get_middle_number(corrected_update)
        # print(f"{corrected_update} - {check_sorted(corrected_update)}")

# print(counter)
print(counter_corrected)