import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
split_pattern = r"(do\(\)|don't\(\))"
with open('input-3.txt', 'r') as file:
  content = file.read()
segments = re.split(split_pattern, content)

should_do = True
to_process = ''

for segment in segments:
  if segment == "don't()":
    should_do = False
  elif segment == "do()":
    should_do = True
  elif should_do:
    to_process += segment

matches = re.findall(pattern, to_process)
result = sum([int(a) * int(b) for a, b in matches])
print(result)
