class User:
    def __init__(self, first_name, last_name, age,):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        

    def describe_user(self):
        
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")

    def greet_user(self):
       
        print(f"Hello, {self.first_name} {self.last_name}!")

# Create instances representing different users
user1 = User("John", "Doe", 30,)
user2 = User("Jane", "Smith", 25,)
user3 = User("Bob", "Johnson", 40,)

# Call both methods for each user
users = [user1, user2, user3]
for user in users:
    user.describe_user()

