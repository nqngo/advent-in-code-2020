from collections import deque

data = ""

with open('input.txt', 'r') as src:
  # Parse the dataset
  data = [ item.rstrip() for item in src.readlines() ]

result = {
  "win": 6,
  "draw": 3,
  "lose": 0
}

shape = {
  "rock": 1,
  "paper": 2,
  "scissors": 3
}

# Part 1
def part1(data):
  score = {
    "A X": result["draw"] + shape["rock"],
    "A Y": result["win"] + shape["paper"],
    "A Z": result["lose"] + shape["scissors"],
    "B X": result["lose"] + shape["rock"],
    "B Y": result["draw"] + shape["paper"],
    "B Z": result["win"] + shape["scissors"],
    "C X": result["win"] + shape["rock"],
    "C Y": result["lose"] + shape["paper"],
    "C Z": result["draw"] + shape["scissors"]
  }
  return sum(score[item] for item in data)
print(part1(data))

# Part 2
def part2(data):
  score = {
    "A X": result["lose"] + shape["scissors"],
    "A Y": result["draw"] + shape["rock"],
    "A Z": result["win"] + shape["paper"],
    "B X": result["lose"] + shape["rock"],
    "B Y": result["draw"] + shape["paper"],
    "B Z": result["win"] + shape["scissors"],
    "C X": result["lose"] + shape["paper"],
    "C Y": result["draw"] + shape["scissors"],
    "C Z": result["win"] + shape["rock"]
  }
  return sum(score[item] for item in data)
print(part2(data))