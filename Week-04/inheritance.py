class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} says Woof!")


# Create a Dog object
d = Dog("Buddy")
d.speak()  # Inherited from Animal
d.bark()  # Defined in Dog
