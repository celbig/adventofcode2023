import sys
import re

class Number:
  def __init__(self, line, match):
    self.value = int(match.group())
    self.line = line
    self.start = match.start()
    self.end = match.end()

  def adjacent(self, symbol):
    if symbol.line == self.line - 1 or symbol.line == self.line + 1:
      return self.start - 1 <= symbol.pos and symbol.pos <= self.end
    elif symbol.line == self.line:
      # print(f"{symbol.line} {self.value} ({self.start}, {self.end}) {symbol.value} ({symbol.pos})")
      return symbol.pos == self.start - 1 or symbol.pos == self.end
    else:
      return False
    
  def adjacent_to_any_symbol(self, symbols):
    for symbol in symbols:
      if self.adjacent(symbol):
        return True
      
    return False





class Symbol:
  def __init__(self, line, match):
    self.value = match.group()
    self.line = line
    self.pos = match.start()
  

class Gear:
  def __init__(self, line, match, numbers):
    self.symbol = Symbol(line, match)

    adjacent_number = []
    for number in numbers:
      if number.adjacent(self.symbol):
        adjacent_number += [number]
      if len(adjacent_number) > 2:
        break

    if len(adjacent_number) == 2:
      self.ratio = adjacent_number[0].value * adjacent_number[1].value
    else:
      self.ratio = 0
    

if __name__ == "__main__":
  # Check input arguments -----
  if len(sys.argv) != 2:
    print("This script must be called with one argument (the path to the input file)!")
    exit()
  file_path = sys.argv[1]

  numbers = []
  gears = []
  lines = []
  with open(file_path) as file: 
    for line_number, line in enumerate(file.readlines()):
      lines += [line]
      numbers += [Number(line_number, match) for match in re.finditer(r"([0-9]+)", line)]

    for line_number, line in enumerate(lines):
      gears += [Gear(line_number, match, numbers) for match in re.finditer(r"(\*)", line)]
    
  
    solution = sum([gear.ratio for gear in gears])
    print(f"The solution for day 3 part 1 is: {solution}")


