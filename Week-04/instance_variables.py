class Dog:
    def __init__(self, name, breed):
        self.name = name  # instance variable
        self.breed = breed  # instance variable

    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")


# Create two different Dog objects
dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Rocky", "Bulldog")


dog1.bark()  # Output: Buddy the Labrador says Woof!
dog2.bark()  # Output: Rocky the Bulldog says Woof!
