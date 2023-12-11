import sys
import re

def parse_line(text: str) -> int:
  matches = re.findall(r'[0-9]', text)
  number_text = matches[0] + matches[len(matches) - 1]
  return int(number_text)

if __name__ == "__main__":
  # Check input arguments -----
  if len(sys.argv) != 2:
    print("This script must be called with one argument (the path to the input file)!")
    exit()
  file_path = sys.argv[1]

  with open(file_path) as file:
    numbers = [parse_line(line) for line in file.readlines()]
    
    solution = sum(numbers)
    print(f"The answer for day 1 is: {solution}")
