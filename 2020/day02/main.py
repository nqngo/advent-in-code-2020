data = ""

with open('src.txt', 'r') as src:
  # Parse the dataset
  lines = [ value.rstrip('\n').split() for value in src.readlines() ]
  data =  [ {'first': int(l[0].split('-')[0]),
             'second': int(l[0].split('-')[1]),
             'char': l[1].rstrip(':'),
             'passwd': l[2]
            } for l in lines ]

# Part 1
tally = 0
for line in data:
  count = line['passwd'].count(line['char'])
  if count <= line['second'] and count>= line['first']:
    tally+=1
print(tally)

# Part 2
tally = 0
for line in data:
  first = line["passwd"][line["first"]-1] in line["char"]
  second = line["passwd"][line["second"]-1] in line["char"]
  if first != second:
    tally+=1
print(tally)
