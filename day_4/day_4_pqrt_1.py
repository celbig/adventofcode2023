import sys
import re

class Card:
  def __init__(self, text:str):
    text = text.removesuffix("\n")
    split_text = text.split(":")
    self.id = int(re.match(r"Card *([0-9]+)", split_text[0]).group(1))
    split_numbers = split_text[1].split("|")
    self.ours = [x for x in split_numbers[0].split(" ") if x]
    self.winning = [x for x in split_numbers[1].split(" ") if x]

  def value(self):
    ours_winning = [x for x in self.ours if x in self.winning]
    if not len(ours_winning):
      return 0
    else:
      return pow(2, len(ours_winning) - 1)
    
if __name__ == "__main__":
  # Check input arguments -----
  if len(sys.argv) != 2:
    print("This script must be called with one argument (the path to the input file)!")
    exit()
  file_path = sys.argv[1]


  with open(file_path) as file: 
    cards = [Card(line) for line in file.readlines()]

    solution = sum([card.value() for card in cards])
    print(f"The solution for day 4 part 1 is: {solution}")


