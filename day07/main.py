from collections import deque
import re

OUT_RE = re.compile(r'(\w+ \w+) bags contain (.*)')
IN_RE = re.compile(r'(\d+) (\w+ \w+) bags?')
data = {}

def expand(inner):
  # Traverse down the graph and flatten all children
  queue = deque(data.get(inner, ()))
  while queue:
    count, bag = queue.pop()
    queue.extend((count * subcount, subbag)
                 for subcount, subbag in data.get(bag, ()))
    yield count, bag

with open('input.txt', 'r') as src:
  # Parse the dataset
  for line in src.readlines():
    outer, inners = re.match(OUT_RE, line).groups()
    data[outer] = [(int(match.group(1)), match.group(2))
                  for match in re.finditer(IN_RE, inners)]

flat_data = {inner: list(expand(inner)) for inner in data}

print("Part 1\n-----------")
print(sum(any(bag == 'shiny gold' for count, bag in flat_data[outer])
      for outer in flat_data))

print("Part 2\n-----------")
print(sum(count for count, bag in flat_data['shiny gold']))