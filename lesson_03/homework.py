from pathlib import Path
from typing import Generator

ROOT_DIR = Path(__file__).parent.parent
analyzed_file = ROOT_DIR / "rockyou.txt"

results: list[str] = []
counter = 0


def get_lines_with_user(filename: Path, word: str) -> Generator:
    with open(filename, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if word in line.lower():
                yield line


for line in get_lines_with_user(analyzed_file, "user"):
    decision = input(f"Do you want to add line {line} to results? Yes -y, No - n: ")
    if decision == "y":
        results.append(line)
        print(f"Line: {line} is added")
        counter += 1
    elif decision == "n":
        continue
    else:
        break

print(f"{counter=}")
print(f"{results=}")
