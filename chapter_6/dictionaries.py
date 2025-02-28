alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

del alien_0['points']
print(alien_0)

point_value = alien_0.get('color', 'No point value assigned.')
print(point_value)


user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key, value in user_0.items():
 print(f"\nKey: {key}")
 print(f"Value: {value}")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
for name in favorite_languages.keys():
    print(name.title())

for name in sorted(favorite_languages.keys()):
 print(f"{name.title()}, thank you for taking the poll.")

for language in favorite_languages.values():
 print(language.title())


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)
