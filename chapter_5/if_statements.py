cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(f"{user.title()}, you can post a response if you wish.")


age = 12
if age < 4:
 print("Your admission cost is $0.")
elif age < 18:
 print("Your admission cost is $25.")
else:
 print("Your admission cost is $40.")

age = 12
if age < 4:
 price = 0
elif age < 18:
 price = 25
else:
 price = 40
print(f"Your admission cost is ${price}.")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
 if requested_topping in available_toppings:
    print(f"Adding {requested_topping}.")
 else:
    print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")