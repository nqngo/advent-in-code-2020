from copy import deepcopy

with open('input.txt', 'r') as src:
  # Parse the dataset
  rmap, rins = src.read().split('\n\n')
  pmap = [ [line[i:i+4].strip() for i in range(0,len(line),4)]
          for line in rmap.split('\n') ]

  # Parse the box mapping
  bmap = { str(i+1):[] for (i,v) in enumerate(pmap[0]) }  
  for line in pmap[:-1]:
    for (i, v) in enumerate(line):
      if v:
        bmap[str(i+1)].insert(0, v)

  # Parse the instruction
  ins = []
  for line in rins.split('\n'):
    p = line.split()
    ins.append({ 'move': int(p[1]), 'from': p[3], 'to': p[5]})


# Move the box around
def move(data, instruction):
  bto = data[instruction['to']]
  bfrom = data[instruction['from']]
  boxes = [ bfrom.pop() for i in range(0, instruction['move'])]
  bto.extend(boxes)


# Move the box around
def move2(data, instruction):
  bto = data[instruction['to']]
  bfrom = data[instruction['from']]
  boxes = bfrom[0 - instruction['move']:]
  bto.extend(boxes)
  data[instruction['from']] = bfrom[:0 - instruction['move']]


# Part 1
def part1(bmap, ins):
  wmap = deepcopy(bmap)
  for instruction in ins:
    move(wmap, instruction)

  return ''.join([ wmap[k][-1].strip('[').strip(']') for k in wmap ])

print(part1(bmap, ins))

# Part 2
def part2(bmap, ins):
  wmap = deepcopy(bmap)
  for instruction in ins:
    move2(wmap, instruction)

  return ''.join([ wmap[k][-1].strip('[').strip(']') for k in wmap ])

print(part2(bmap, ins))