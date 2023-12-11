import sys
import re

def find_first(matches: list[tuple[int, int, int]]) -> int:
  pos_save = None
  digit_save = None

  for digit, pos, _ in matches:
      if not pos is None:
        if pos_save is None or pos < pos_save:
          pos_save = pos
          digit_save = digit
  
  return digit_save

def find_last(matches: list[tuple[int, int, int]]) -> int:
  pos_save = None
  digit_save = None

  for digit, _, pos in matches:
      if not pos is None:
        if pos_save is None or pos > pos_save:
          pos_save = pos
          digit_save = digit
  
  return digit_save

def match_digit(text:str, digit: tuple[int, str]) -> tuple[int, int, int]:
  digit_int, digit_text = digit
  if digit_text:
    pattern = str(digit_int) + "|" + digit_text
  else:
    pattern = str(digit_int)

  matches = [match for match in re.finditer(pattern, text)]
  if matches:
    return (digit_int, matches[0].start(), matches[len(matches) - 1].start())
  else:
    return (digit_int, None, None)

def parse_line(text: str) -> int:
  digit_list = [
    (1, "one"),
    (2, "two"),
    (3, "three"),
    (4, "four"),
    (5, "five"),
    (6, "six"),
    (7, "seven"),
    (8, "eight"),
    (9, "nine"), 
    (0, "")
    ]
  digit_matches = [match_digit(text, digit) for digit in digit_list]

  return int(str(find_first(digit_matches)) + str(find_last(digit_matches)))

if __name__ == "__main__":
  # Check input arguments -----
  if len(sys.argv) != 2:
    print("This script must be called with one argument (the path to the input file)!")
    exit()
  file_path = sys.argv[1]

  with open(file_path) as file:
    numbers = [parse_line(line) for line in file.readlines()]

    solution = sum (numbers)
    print(f"The answer for day 1 part 2 is: {solution}")
