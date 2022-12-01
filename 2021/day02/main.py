from collections import deque

data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ item.split() for item in src.readlines() ]

# Part 1
def part1(data):
  x = 0
  y = 0
  for d in data:
    if 'forward' in d[0]:
      x+= int(d[1])
    elif 'down' in d[0]:
      y+= int(d[1])
    elif 'up' in d[0]:
      y-= int(d[1])
  return (x*y)

print(part1(data))

# Part 2
def part2(data):
  x = 0
  aim = 0
  y = 0
  for d in data:
    if 'forward' in d[0]:
      x+= int(d[1])
      y+= int(d[1])*aim
    elif 'down' in d[0]:
      aim+= int(d[1])
    elif 'up' in d[0]:
      aim-= int(d[1])
  return (x*y)

print(part2(data))