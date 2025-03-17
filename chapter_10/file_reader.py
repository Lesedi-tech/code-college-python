from pathlib import Path
path = Path('my-code/code-college-python/chapter_10/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
 print(line)