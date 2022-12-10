data = ""

with open('test.txt', 'r') as src:
  # Parse the dataset
  data = [ item.rstrip().split() for item in src.readlines() ]


# Direction mapping
d = {
  'U': (0, 1),
  'D': (0, -1),
  'L': (-1, 0),
  'R': (1, 0)
}


class RopeEnd:
    def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y
      self.visited = set((x, y))
    def __str__(self):
      return f"({self.x}, {self.y})"
    def move(self, direction):
      self.x += d[direction][0]
      self.y += d[direction][1]
      self.visited.add((self.x, self.y))


def move_one(head, tail, direction):
  """Move one step"""

  head.move(direction)

  if (tail.x - head.x) in [-2, 2]:
    tail.move(direction)
    if tail.y != head.y:
      tail.y = head.y
    return
  if (tail.y - head.y) in [-2, 2]:
    tail.move(direction)
    if tail.x != head.x:
      tail.x = head.x
    return

  
    

# Part 1
def part1(data):
  head = RopeEnd()
  tail = RopeEnd()
  for instruction in data:
    for tick in range(int(instruction[1])):
      move_one(head, tail, instruction[0])
      print(head, tail)
  print("Final:", head, tail)
  return len(tail.visited)


print(part1(data))
