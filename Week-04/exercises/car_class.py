class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def carInfo(self):
        print("Car Info:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


brand = input("Enter car brand: ")
model = input("Enter car model: ")
year = int(input("Enter car manufactured year: "))

c = Car(brand, model, year)
c.carInfo()
