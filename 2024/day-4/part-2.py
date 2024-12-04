def check_cross(top_element, bottom_element):
    return (top_element == 'M' and bottom_element == 'S') or (top_element == 'S' and bottom_element == 'M')

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

count = 0
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[0])-1):
        if lines[i][j] == 'A':
            if check_cross(lines[i - 1][j - 1], lines[i + 1][j + 1]) and check_cross(lines[i - 1][j + 1], lines[i + 1][j - 1]):
                count += 1

print(count)
    
