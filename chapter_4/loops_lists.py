magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician)

for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")


for value in range(1, 5):
 print(value)

numbers = list(range(1, 6))
print(numbers)


even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)


#Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])


print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())