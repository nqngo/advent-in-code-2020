data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ group.split('\n') for group in src.read().split('\n\n')]

print("Part 1\n--------------")
print(sum(len(set(''.join(group))) for group in data))

print("Part 2\n--------------")
nice_data = [ [ set(answer) for answer in group ] for group in data ]
common = [ len(set.intersection(*group)) for group in nice_data ]
print(sum(common))