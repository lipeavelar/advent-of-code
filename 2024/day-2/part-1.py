def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False

data = [list(map(int,l.split())) for l in open("input.txt").readlines()]

safe_count = sum([is_safe(row) for row in data])
print(safe_count)
