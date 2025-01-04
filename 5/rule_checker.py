import os

class Rule:
    def __init__(self, L, R):
        self.L = L
        self.R = R
        self.Li = -1
        self.Ri = -1
    
    def __str__(self):
        return f"({self.L} {self.R}) ({self.Li} {self.Ri}) - {self.correct()}"
    
    def reset(self):
        self.Li = -1
        self.Ri = -1
    
    def correct(self):
        return self.Li < self.Ri
    
rules = []
updates = []

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file, 'r') as file:
    mode = 0
    for line in file:
        if line == '\n':
            mode = 1
            continue
    
        line = line.strip('\n')
        if mode == 0:
            rules.append(Rule(int(line.split('|')[0]), int(line.split('|')[1])))
        elif mode == 1:
            updates.append([int(x) for x in line.split(',')])
        else:
            raise Exception('Invalid mode')
     
def organize_pages(rules, update):
    update_organized = update.copy()
    for rule in rules:
        if rule.L in update and rule.R in update:
            rule.Li = update.index(rule.L)
            rule.Ri = update.index(rule.R) 

            if rule.Li > rule.Ri:
                update_organized[rule.Li], update_organized[rule.Ri] = update_organized[rule.Ri], update_organized[rule.Li]
    
    return update_organized

counter = 0
middle_number_counter = 0

for update in updates:
    organized_pages = organize_pages(rules, update)
    rules_culled = [r for r in rules if r.Li != -1 and r.Ri != -1]
    
    if(all([r.correct() for r in rules_culled])):
        print(update, " - correct")
        counter += 1
        middle_number_counter += organized_pages[(len(organized_pages)/2).__floor__()]
    else:
        print(update, " - incorrect")
        
    for rule in rules:
        rule.reset()
    
print(middle_number_counter)