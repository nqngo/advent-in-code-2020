from copy import deepcopy

data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = src.read().rstrip()

# Part 1
def part1(data):
  stream = [set(data[i:i+4]) for i in range(len(data)-3)]
  for idx, s in enumerate(stream):
    if len(s) == 4:
        return idx+4

print(part1(data))

# Part 2
def part2(data):
  stream = [set(data[i:i+14]) for i in range(len(data)-13)]
  for idx, s in enumerate(stream):
    if len(s) == 14:
        return idx+14

print(part2(data))