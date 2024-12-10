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
    must_continue = True
    for i in range(1, len(pages)):
        if pages[i] not in must_be_before:
            continue
        for j in range(0, i):
            if pages[j] in must_be_before[pages[i]]:
                must_continue = False
                break
        if not must_continue:
            break
    else:
        count += int(pages[len(pages) // 2])

print(count)
