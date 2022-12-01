from collections import deque

data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [int(item) for item in src.readlines() ]

# Part 1
def part1(data):
  i = data[0]
  inc = 0
  for n in data[1:]:
    if n > i:
      inc+=1
    i = n
  return inc

print("Part 1\n-----------")
print(part1(data))

print()
# Part 2
data2 = [ sum(data[i-1:i+2]) for i, _ in enumerate(data) ]

print("Part 2\n-----------")
print(part1(data2[1:-1]))