data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ item.rstrip() for item in src.readlines() ]

cycle = {
  'addx': 2,
  'noop': 1,
}


def render_crt(data):
  circuit = []
  c = 0
  X = 1
  for instruction in data:
    if 'noop' in instruction:
      c += cycle[instruction]
      circuit.append((c, X))
    elif 'addx' in instruction:
      INS, V =  instruction.split()
      circuit.append((c + 1, X))
      c += cycle[INS]
      circuit.append((c, X))
      X += int(V)
  return circuit


# Part 1
def part1(data):
  SAMPLE = [20, 60, 100, 140, 180, 220]
  circuit = render_crt(data)
  sample_points = [circuit[s-1] for s in SAMPLE]
  return sum(s[0]*s[1] for s in sample_points)

print(part1(data))


# Part 2
def part2(data):
  COLS = 40
  ROWS = 6
  circuit = render_crt(data)
  for idx in [i for i in range(0, len(circuit), COLS)]:
    for idx, cursor in enumerate(circuit[idx:idx+COLS]):
      if idx in range(cursor[1]-1, cursor[1]+2):
        print("#", end="")
      else:
        print(".", end="")
    print()
  return 0

print(part2(data))