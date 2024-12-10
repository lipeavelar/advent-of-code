with open('input.txt') as f:
    lines = f.read().split('\n\n')

rules = lines[0].split('\n')
updates = lines[1].split('\n')
must_be_before = dict()
for rule in rules:
    key, value = rule.split('|')
    if key not in must_be_before:
      must_be_before[key] = []
    must_be_before[key].append(value)

count = 0
for update in updates:
    pages = update.split(',')
    should_count = False
    i = 1
    while i < len(pages):
        if pages[i] not in must_be_before:
            i += 1
            continue
        for j in range(0, i):
            if pages[j] in must_be_before[pages[i]]:
                should_count = True
                move = pages.pop(j)
                pages.insert(i, move)
                break
        else:
            i += 1
    if should_count:
        count += int(pages[len(pages) // 2])

print(count)
