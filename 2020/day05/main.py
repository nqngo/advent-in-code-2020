data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ (value[:7], value[7:10]) for value in src.readlines() ]


print("Part 1\n------------")

def find_row(row_code):
  min = 0
  max = 128
  for char in row_code:
    if char == 'F':
      max = (min + max) // 2
    elif char == 'B':
      min = (min + max) // 2
  return (min + max) // 2

def find_col(col_code):
  min = 0
  max = 8
  for char in col_code:
    if char == 'L':
      max = (min + max) // 2
    elif char == 'R':
      min = (min + max) // 2
  return (min + max) // 2

def seat_id(row, col):
  return row * 8 + col

seat_ids = [ seat_id(find_row(p[0]), find_col(p[1])) for p in data ]
print(max(seat_ids))

print("Part 2\n------------")
nice_data = [ (find_row(p[0]), find_col(p[1])) for p in data]
for r in range(128):
  for c in range(8):
    if (r, c) not in nice_data:
      sid = seat_id(r, c)
      if sid + 1 in seat_ids and sid - 1 in seat_ids:
        print(sid)