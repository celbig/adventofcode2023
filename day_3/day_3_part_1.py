import sys
import re

if __name__ == "__main__":
  # Check input arguments -----
  if len(sys.argv) != 2:
    print("This script must be called with one argument (the path to the input file)!")
    exit()
  file_path = sys.argv[1]


  with open(file_path) as file: 

    solution = None
    print(f"The solution for day 2 part 2 is: {solution}")


