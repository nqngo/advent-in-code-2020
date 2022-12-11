import math
from copy import deepcopy


MONKEYS = {}
MONKEYS2 = {}

class Monkey:
    def __init__(self, items, operation, test, truthy, falsy, collections):
      self.items = items
      self.operation = operation
      self.test = test
      self.truthy = truthy
      self.falsy = falsy
      self.inspected = 0
      self.collections = collections
    def inspect(self):
      while self.items:
        self.inspected += 1
        item = self.operation(self.items.pop(0))
        if self.test(item):
          self.collections[self.truthy].items.append(item)
        else:
          self.collections[self.falsy].items.append(item)


with open('input.txt', 'r') as src:
  # Parse the dataset
  instructions = src.read().split('\n\n')
  
  gcd = math.prod(int(instruction.split('\n')[3].split('divisible by')[-1].strip()) for instruction in instructions)

  for instruction in instructions:
    datum = instruction.split('\n')
    id = datum[0].rstrip(':')[-1]
    items = [ int(i) for i in datum[1].split(':')[1].split(', ') ]
    ops = datum[2].split('=')[1]
    operation = eval(f"lambda old: ({ops}) // 3")
    t = datum[3].split('divisible by')[-1].strip()
    test = eval(f"lambda x: False if x % {t} else True")
    truthy = datum[4][-1]
    falsy = datum[5][-1]
    MONKEYS[id] = Monkey(
      items = items,
      operation = operation,
      test = test,
      truthy = truthy,
      falsy = falsy,
      collections = MONKEYS,
    )
    operation = eval(f"lambda old: ({ops}) % gcd")
    MONKEYS2[id] = Monkey(
      items = deepcopy(items),
      operation = operation,
      test = test,
      truthy = truthy,
      falsy = falsy,
      collections = MONKEYS2,
    )


def monkey_business(monkeys, cycles):
  for iter in range(cycles):
    for m in monkeys:
      monkeys[m].inspect()
  return math.prod(sorted(monkeys[m].inspected for m in monkeys)[-2:])


print(monkey_business(MONKEYS, 20))
print(monkey_business(MONKEYS2, 10000))