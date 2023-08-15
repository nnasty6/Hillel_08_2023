from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

file = open(ROOT_DIR / "rockyou.txt")
# text: str = file.readline()
counter = 0

while True:
    try:
        word = file.readline()
        counter += 1
        print(word)
    except Exception:
        break
file.close()
print(counter)
