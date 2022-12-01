data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ value.rstrip('\n') for value in src.readlines() ]

# Part 1
tally = 0
pos = 0
row_size = len(data[0])
for row in data[1:]:
  pos+=3
  if pos > (row_size - 1):
    pos= pos - row_size
  if row[pos] in '#':
    tally+=1
print("Part 1\n-----------")
print(tally)

# Part 2
def slope(data, right, down):
  tally = 0
  pos = 0
  row_size = len(data[0])
  for row in data[down::down]:
    pos += right
    if pos > (row_size - 1):
      pos = pos - row_size
    if row[pos] in '#':
      tally += 1
  return tally

print("Part 2\n-----------")
print(slope(data, 1, 1)*slope(data, 3, 1)*slope(data, 5, 1)*slope(data, 7, 1)*slope(data, 1, 2))