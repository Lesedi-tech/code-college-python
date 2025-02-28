bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Aceesing Elements
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#Modifying, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

motorcycles.remove('ducati')
print(motorcycles)


#Organizing a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars.reverse()
print(cars)


#Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)