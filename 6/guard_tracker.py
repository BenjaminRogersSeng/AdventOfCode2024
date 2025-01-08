import os
from time import sleep

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file, 'r') as file:
	raw_lab = file.read().split()

# print(raw_lab)

obstacle_map = [[x_idx, y] for y, x in enumerate(raw_lab) for x_idx in range(len(x)) if x[x_idx] == "#"]
guard_positions = [[x_idx, y] for y, x in enumerate(raw_lab) for x_idx in range(len(x)) if x[x_idx] == "^"]
guard_directions = [0]

# print(list(obstacle_map))
# print(list(guard_positions))
# print(guard_directions)

def cast_ray(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    steps = max(abs(dx), abs(dy))
    dx /= steps
    dy /= steps
    x, y = start
    locations = []
    for _ in range(steps):
        x += dx
        y += dy
        if [x, y] not in obstacle_map:
            locations.append([int(x),int(y)])
            continue
        else:
            break

    return locations if locations else None

def check_direction(position, direction):
    if direction == 0:
        return cast_ray(position, [position[0], 0])
    elif direction == 1:
       return cast_ray(position, [len(raw_lab[0]), position[1]])
    elif direction == 2:
       return cast_ray(position, [position[0], len(raw_lab)])
    elif direction == 3:
       return cast_ray(position, [0, position[1]])
    else:
        raise ValueError("Invalid direction")
    
def contains_exit(positions):
    for position in positions:
        if position[0] == 0 or position[0] == len(raw_lab[0]) or position[1] == 0 or position[1] == len(raw_lab):
            return True
    return False
    
def move_guard():     
    next_positions = check_direction(guard_positions[-1], guard_directions[-1])
    if(not contains_exit(next_positions)): # No obstacles in the way
        for position in next_positions:
            guard_positions.append(position)
        # print("Moving forward:" + str(guard_positions[-1]))
        guard_directions.append((guard_directions[-1] + 1) % 4)
        # print("Turning right: " + str((guard_directions[-1])))
        return True
    else:
        for position in next_positions:
            guard_positions.append(position)       
        # print("Exited")
        return False 

while move_guard():
    pass

# print(guard_positions)
# print(guard_directions)
print(len(set(map(tuple, guard_positions)))) # Distinct positions visited by the guard