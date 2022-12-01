import re

data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ {item.split(':')[0]:item.split(':')[1] for item in passport.replace('\n', ' ').split()}
            for passport in src.read().split('\n\n')]
  

valid_field = ['byr', 'iyr','eyr','hgt', 'hcl', 'ecl', 'pid']

print('Part 1:\n-------------------')
tally = 0
for passport in data:
  if all(field in passport for field in valid_field):
    tally +=1

print(tally)

ecl_valid = 'amb blu brn gry grn hzl oth'.split()
print('Part 2:\n-------------------')
tally = 0
for passport in data:
  # Skip if does not have all fields
  if not all(field in passport for field in valid_field):
    continue
  # Birth Year
  byr = int(passport['byr'])
  if not (1920 <= byr <= 2002):
    continue
  # Issue Year
  iyr = int(passport['iyr'])
  if not (2010 <= iyr <= 2020):
    continue
  # Expiration Year
  eyr = int(passport['eyr'])
  if not (2020 <= eyr <=2030):
    continue
  # Height
  hgt = re.match(r"(\d+)(cm|in)$", passport['hgt'])
  if hgt is None:
    continue
  if hgt.group(2) == 'in':
    if not(59 <= int(hgt.group(1)) <= 76):
      continue
  elif hgt.group(2) == 'cm':
    if not (150 <= int(hgt.group(1)) <= 193):
      continue
  # Hair colour
  hcl = re.match(r"^#[0-9a-f]{6}$", passport['hcl'])
  if hcl is None:
    continue
  # Eye Color
  if passport['ecl'] not in ecl_valid:
    continue
  # Passport ID
  pid = re.match(r"^[0-9]{9}$", passport['pid'])
  if pid is None:
    continue
  tally += 1

print(tally)
