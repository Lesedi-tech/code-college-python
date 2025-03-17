class Resturant:
     def __init__(self, resturant_name, cuisine_type):
        """Initialize name and age attributes."""
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

     def describe_resturant(self):
        print(f"{self.resturant_name} serves {self.cuisine_type}")
    
     def open_resturant(self):
        print(f"{self.resturant_name} is Open!!!")

resturant = Resturant("Mohitos","Sea Food")
print(resturant.resturant_name)
print(resturant.cuisine_type)
resturant.describe_resturant()
resturant.open_resturant()

#9.2
restaurant1 = Resturant("Mohitos", "Sea Food")
restaurant2 = Resturant("Kebab'", "Turkish")
restaurant3 = Resturant("Pizza Hut", "Italian")


restaurant1.describe_resturant()
restaurant2.describe_resturant()
restaurant3.describe_resturant()

