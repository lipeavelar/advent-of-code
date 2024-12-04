with open('input.txt') as f:
    lines = f.readlines()
    distance = 0
    left = []
    right = []
    for i in range(0, len(lines)):
        values = lines[i].split()
        left.append(int(values[0]))
        right.append(int(values[1]))

    left.sort()
    right.sort()
    for i in range(0, len(left)):
        distance += abs(right[i] - left[i])
    print (distance)
