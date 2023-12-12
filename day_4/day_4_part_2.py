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
    return len(ours_winning)
  

    
if __name__ == "__main__":
  # Check input arguments -----
  if len(sys.argv) != 2:
    print("This script must be called with one argument (the path to the input file)!")
    exit()
  file_path = sys.argv[1]

  cards_copies = {}
  cards = {}
  with open(file_path) as file: 
    for line in file.readlines():
      card = Card(line)
      cards[card.id] = card

      if not card.id in cards_copies:
        cards_copies[card.id] = 1
      else:
        cards_copies[card.id] += 1

      for offset in range(card.value()):
        id = 1 + card.id + offset
        if not id in cards_copies:
          cards_copies[id] = 0
        cards_copies[id] += cards_copies[card.id]
      

    solution = sum([cards_copies[id] for id in cards_copies])
    print(f"The solution for day 4 part 1 is: {solution}")


