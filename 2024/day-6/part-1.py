def is_crate(x, y):
    return guard_map[y][x] == "#"

def print_map(map):
    for line in map:
        print("".join(line))
    print()

with open('input.txt') as f:
    guard_map = [list(line.strip()) for line in f.readlines()]
x = -1
y = -1
for i in range(len(guard_map)):
    if "^" in guard_map[i]:
        y, x = i, guard_map[i].index("^")
        break

direction = 0
directions_modifier = [(0, -1), (1, 0), (0, 1), (-1, 0)]
distinct_positions = 1
guard_map[y][x] = "X"
while True:
    new_x, new_y = directions_modifier[direction]
    x += new_x
    y += new_y
    if x < 0 or x >= len(guard_map) or y < 0 or y >= len(guard_map[0]):
        break
    if is_crate(x, y):
        direction = (direction + 1) % 4
        x -= new_x
        y -= new_y
        continue
    if guard_map[y][x] == ".":
        guard_map[y][x] = "X"
        distinct_positions += 1

print(distinct_positions)
    
     
