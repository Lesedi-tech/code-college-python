from pathlib import Path
path = Path('my-code/code-college-python/chapter_10/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
 pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))