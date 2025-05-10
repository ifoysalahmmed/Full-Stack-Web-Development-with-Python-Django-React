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

    def start(self):
        print("Starting the engine...")


class ElectricCar(Car):

    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def batteryInfo(self):
        self.carInfo()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

    def start(self):
        print("Starting the electric motor silently...")


brand = input("Enter car brand: ")
model = input("Enter car model: ")
year = int(input("Enter car manufactured year: "))
battery_capacity = int(input("Enter battery capacity: "))

ec = ElectricCar(brand, model, year, battery_capacity)
ec.batteryInfo()
ec.start()
