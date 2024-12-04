with open('input.txt') as f:
    lines = f.readlines()
    distance = 0
    left = []
    right = dict()
    for i in range(0, len(lines)):
        values = lines[i].split()
        left.append(int(values[0]))
        r_value = int(values[1])
        if r_value in right:
            right[r_value] += 1
        else:
            right[r_value] = 1

    for i in range(0, len(left)):
        if left[i] in right:
            distance += left[i] * right[left[i]]
    print (distance)
