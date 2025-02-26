name = "Lesedi"
surname = "Mothupi"
location = "Johannesburg"

print(name + " " + surname)

full_name_location = f"{name} {surname}, {location}"

print(full_name_location)

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#To add a tab to your text, use the character combination \t:
print("Python")
print("\tPython")

#To add a newline in a string, use the character combination \n:
print("Languages:\nPython\nC\nJavaScript")

#To ensure that no whitespace exists at the right side of a string, use the rstrip() method:
favorite_language = 'python '
favorite_language.rstrip()

#To remove the whitespace from the string permanently, you have to associate the stripped value with the variable name:
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
favorite_language

#You can also strip whitespace from the left side of a string using the lstrip() method, or from both sides at once using strip():
favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()


#here’s how you can initialize the variables x, y, and z to zero:
x, y, z = 0, 0, 0

#Zen of Python
import this
