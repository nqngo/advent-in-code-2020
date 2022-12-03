import string

data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ item.rstrip() for item in src.readlines() ]

# Points mapping
pts = { alpha:index+1 for (index, alpha) in enumerate(string.ascii_lowercase + string.ascii_uppercase) }

# Part 1
def part1(data):
  sum = 0
  for item in data:
    mid = len(item)//2
    A, B = set(item[:mid]), set(item[mid:])
    
    sum += pts[A.intersection(B).pop()]
  return sum

print(part1(data))

# Part 2
def part2(data):
  sum = 0
  groups = len(data)//3
  for iter in range(0, groups):
    idx = iter*3
    A, B, C = set(data[idx]), set(data[idx+1]), set(data[idx+2])
    
    sum += pts[A.intersection(B).intersection(C).pop()]
  return sum

print(part2(data))