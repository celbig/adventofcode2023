import sys
import re

class Draw:
  def __init__(self, text) -> None:
    red_search = re.search(r"([0-9]+) red", text)
    if red_search:
      self.red = int(red_search.group(1))
    else:
      self.red = 0
    
    green_search = re.search(r"([0-9]+) green", text)
    if green_search:
      self.green = int(green_search.group(1))
    else:
      self.green = 0

    blue_search = re.search(r"([0-9]+) blue", text)
    if blue_search:
      self.blue = int(blue_search.group(1))
    else:
      self.blue = 0


  def compatible(self, red, green, blue) -> True:
    if self.red <= red and self.green <= green and self.blue <= blue:
      return True
    else:
      return False

class Game: 
  def __init__(self, line) -> None:
    split_line = line.split(":")

    self.game_id = int(re.match(r"Game ([0-9]+)", split_line[0]).group(1))
    self.draws = [Draw(draw) for draw in split_line[1].split(";")]
    
  def compatible(self, red, green, blue) -> True:
    return all([draw.compatible(red, green, blue) for draw in self.draws])
    
if __name__ == "__main__":
  # Check input arguments -----
  if len(sys.argv) != 2:
    print("This script must be called with one argument (the path to the input file)!")
    exit()
  file_path = sys.argv[1]

  # problem data
  red = 12
  green = 13
  blue = 14
  print(f"Solving for {red} red, {green} green, and {blue} blue...")

  with open(file_path) as file: 
    games = [Game(line) for line in file.readlines()]

    print(games[0].compatible(red, green, blue))
    compatible_games = [g for g in games if g.compatible(red, green, blue)]

    solution = sum([g.game_id for g in compatible_games])
    print(f"The solution for day 2 part 1 is: {solution}")


