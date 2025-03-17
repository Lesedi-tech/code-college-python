from pathlib import Path

"""contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('my-code/code-college-python/chapter_10/programming.txt')
path.write_text(contents)"""


"""new_guest = input("Username?")
path = Path('my-code/code-college-python/chapter_10/guest.txt')
path.write_text(new_guest)"""


# Initialize an empty list to store guest names
guest_names = []
path = Path('my-code/code-college-python/chapter_10/guest_book.txt')
# Start a while loop to collect names
while True:
    name = input("Please enter your name (or 'quit' to exit): ")
    
    # Check if the user wants to quit
    if name.lower() == 'quit':
        break
    
    # Add the name to the list
    guest_names.append(name)

for guest in guest_names:
    path.write_text(guest + '\n')