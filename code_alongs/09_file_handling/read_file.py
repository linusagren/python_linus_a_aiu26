from pathlib import Path

# __file__ -> absolute path to this script
# .parent -> parent directory of this script
# / "data" -> add this directory to the path
DATA_PATH = Path(__file__).parent / "data"

print(DATA_PATH)

with open(DATA_PATH / "quotes.txt", "r") as file:
    print(file.read())