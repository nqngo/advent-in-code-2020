from collections import deque

data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ tuple(i.rstrip('\n').split())
           for i in src.readlines() ]


def accumlator(input):
  # Accumulator
  # Record which op we have traversed
  traversed = []
  cursor = 0
  end = len(data) - 1
  accum = 0
  # Keep a cursor on which op we have travel
  while cursor <= end:
    op, arg = input[cursor]
    if cursor in traversed:
      # Return True if there is an error
      return accum, True
    traversed.append(cursor)
    if op == 'nop':
      cursor += 1
    elif op == 'acc':
      cursor += 1
      accum += int(arg)
    elif op == 'jmp':
      cursor += int(arg)
  return accum, False


def bruteforce_correction(input):
  # Bruteforce the correct solution by
  # generate mutation of the list whenver seeing
  # a jmp or nop instruction
  for cursor in range(0,len(input) - 1):
    op, arg = input[cursor]
    if op == 'jmp':
      op = 'nop'
    elif op == 'nop':
      op = 'jmp'
    else:
      continue
    mutated_data = list(input)
    mutated_data[cursor] = (op, arg)
    accum, error = accumlator(mutated_data)
    if not error:
      return accum


print('Part 1\n-----------')
print(accumlator(data)[0])

print('Part 2\n-----------')
print(bruteforce_correction(data))