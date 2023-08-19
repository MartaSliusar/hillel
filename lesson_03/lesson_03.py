from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent

file = open(ROOT_DIR / "rockyou.txt")
text = file.readline()

counter = 0

while True:
    try:
        word = file.readline()
        counter += 1
        print(counter)
    except Exception:
        break

file.close

print(counter)
