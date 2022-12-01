data = ""

with open('src.txt', 'r') as src:
  data = [ int(value.rstrip('\n')) for value in src.readlines() ]

# Part 1
for point in data:
  for second in data:
      if ( point + second == 2020 ):
        print("%d * %d = %d" % (point, second, point*second) )

# Part 2
for point in data:
  for second in data:
    for third in data:
      if ( point + second + third == 2020 ):
        print("%d * %d * %d = %d" % (point, second, third, point*second*third) )
