from collections import deque

data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ [int(item) for item in group.split()]
            for group in src.read().split('\n\n')
         ]

# Part 1
print(max(sum(item) for item in data))

# Part 2
print(sum(sorted(sum(item) for item in data)[-3:]))