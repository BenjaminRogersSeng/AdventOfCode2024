import os
        
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
    return b in KEY_IS_LESS_THAN[a] 

def sort_update(a, b):
    if is_less_than(a, b):
        return -1
    elif is_less_than(b, a):
        return 1
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
        print(update, " - correct")
        counter += get_middle_number(update)
    else:
        print(update, " - incorrect")
        corrected_update = sorted(update, key=lambda x: (x, [is_less_than(x, y) for y in update]))
        counter_corrected += get_middle_number(corrected_update)
        print(f"{corrected_update} - {check_sorted(corrected_update)}")

print(counter)
print(counter_corrected)

# input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
# with open(input_file, 'r') as file:
#     mode = 0
#     for line in file:
#         if line == '\n':
#             mode = 1
#             continue
    
#         line = line.strip('\n')   
#         if mode == 0:
#             rules.append(Rule(int(line.split('|')[0]), int(line.split('|')[1])))
#         elif mode == 1:
#             updates.append([int(x) for x in line.split(',')])
#         else:
#             raise Exception('Invalid mode')
     
# def check_update(rules, update):
#     truthy = True

#     for rule in rules:
#         if rule.L in update and rule.R in update:
#             if update.index(rule.L) > update.index(rule.R):
#                 return False
            
#     return truthy

# def correct_update(rules, update):
#     for i in range(1, len(update)):
#         key = update[i]
#         j = i - 1
#         while j >= 0 and not check_update(rules,):
#             update[j + 1] = update[j]
#             j -= 1
#         update[j + 1] = key
#     return update

# counter = 0
# middle_number_counter = 0
# middle_number_counter_corrected = 0
# correct_updates = []
# incorrect_updates = []

# for update in updates:
#     if(check_update(rules, update)):
#         correct_updates.append(update)
#         middle_number_counter += update[(len(update)/2).__floor__()]
#     else:
#         incorrect_updates.append(update)

# # for update in incorrect_updates:
# #     corrected_update = correct_update(rules, update)
# #     middle_number_counter_corrected += update[(len(update)/2).__floor__()]


# # print(len(updates))
# # print(len(correct_updates))
# # print(len(incorrect_updates))

# corrected_update = correct_update(rules, incorrect_updates[0])
# print(f"{incorrect_updates[0]} - {check_update(rules, incorrect_updates[0])}\n{corrected_update} - {check_update(rules, corrected_update)}")

# # print(middle_number_counter)
# # print(middle_number_counter_corrected)