import string

data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ [range(int(r.split('-')[0]), int(r.split('-')[1])+1) for r in item.rstrip().split(',')] for item in src.readlines() ]

# Part 1
def part1(data):
  tally = 0
  for item in data:
    A, B = set(item[0]), set(item[1])
    if A <= B or B <= A:
      tally += 1
  return tally

print(part1(data))

# Part 2
def part2(data):
  tally = 0
  for item in data:
    A, B = set(item[0]), set(item[1])
    if A.intersection(B):
      tally += 1
  return tally

print(part2(data))