from itertools import product
from functools import reduce

def all_combinations(result, nums):
    operations = ['+', '*']
    for ops in product(operations, repeat=len(nums)-1):
        expression = nums[0]
        for num, op in zip(nums[1:], ops):
            expression = eval(str(expression) + op + str(num))
        if expression == result:
            return result
    return 0

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

count = 0
result = dict()
for line in lines:
    key, values = line.split(': ')
    result = int(key)
    nums = [int(l) for l in values.split(' ')]
    count += all_combinations(result, nums)

print(count)
