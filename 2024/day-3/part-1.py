import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
with open('input-3.txt', 'r') as file:
  content = file.read()
matches = re.findall(pattern, content)
result = sum([int(a) * int(b) for a, b in matches])
print(result)
