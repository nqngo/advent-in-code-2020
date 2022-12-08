data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ list(map(int, item.rstrip())) for item in src.readlines() ]

# Transpose the data
data2 = list(map(list, zip(*data)))

# Part 1
def part1(data, data2):
  coordinates = [(x, y) for x in range(len(data))
                        for y in range(len(data2))]
  visible = 0
  for x, y in coordinates:
    if x in [0, len(data) - 1] or y in [0, len(data) - 1]:
      visible += 1
      continue
    tree = data[x][y]
    row_pre = data[x][:y]
    row_post = data[x][y+1:]
    col_pre = data2[y][:x]
    col_post = data2[y][x+1:]
    if tree > max(row_pre) or tree > max(row_post) or \
       tree > max(col_pre) or tree > max(col_post):
      visible += 1

  return visible

print(part1(data, data2))

# Part 2
def part2(data, data2):
  coordinates = [(x, y) for x in range(len(data))
                        for y in range(len(data2))]
  best_score = 0
  for x, y in coordinates:
    score = 1
    if x in [0, len(data) - 1] or y in [0, len(data) - 1]:
      continue
    tree = data[x][y]
    row_pre = data[x][:y]
    row_post = data[x][y+1:]
    col_pre = data2[y][:x]
    col_post = data2[y][x+1:]
    
    if len(row_pre) > 1:
      seen = 1
      for i in reversed(row_pre[1:]):
        if tree > i:
          seen += 1
        else:
          break
      score *= seen
    if len(row_post) > 1:
      seen = 1
      for i in row_post[:-1]:
        if tree > i:
          seen += 1
        else:
          break
      score *= seen
    if len(col_pre) > 1:
      seen = 1
      for i in reversed(col_pre[1:]):
        if tree > i:
          seen += 1
        else:
          break
      score *= seen
    if len(col_post) > 1:
      seen = 1
      for i in col_post[:-1]:
        if tree > i:
          seen += 1
        else:
          break
      score *= seen
    if score > best_score:
      best_score = score
  return best_score

print(part2(data, data2))