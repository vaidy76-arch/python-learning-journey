"""
Day 13 - Inheritance Basics
Demonstrating parent class, child class, super(), method override
"""
class Vehicle:
    """A generic vehicle - the parent class."""
    
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def describe(self):
        return f"{self.year} {self.brand}"
    
    def start(self):
        return f"{self.brand} engine starting.."
    
class Car(Vehicle):
    """A Car - inherits from Vehicle, adds num_doors."""
    def __init__(self, brand, year,num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def honk(self):
        return f"{self.brand} goes BEEP!!"
    

class ElectricCar(Car):
    """An electric car - inherits from Car, overrides start(), extends describe()."""
    
    def __init__(self, brand, year, num_doors, battery_kwh):
        # Chain the inheritance: ElectricCar → Car → Vehicle
        super().__init__(brand, year, num_doors)
        self.battery_kwh = battery_kwh
    
    def start(self):
        # COMPLETE OVERRIDE - ignore parent's noisy engine sound
        return f"{self.brand} silently powers on... 🔋"
    
    def describe(self):
        # EXTEND - call parent's describe, then add to it
        parent_description = super().describe()
        return f"{parent_description} (Electric, {self.battery_kwh} kWh)"
    
    def charge(self):
        # NEW METHOD - only ElectricCars can do this
        return f"{self.brand} charging... ⚡"
    
if __name__ == "__main__":
    # Create a generic vehicle
    bike = Vehicle("Trek", 2024)
    print(f"Bike: {bike.describe()}")
    print(f"Action: {bike.start()}")
    
    print()
    
    # Create a regular car
    my_car = Car("Toyota", 2023, 4)
    print(f"Car: {my_car.describe()}")
    print(f"Action: {my_car.start()}")
    print(f"Honk: {my_car.honk()}")
    
    print()
    
    # Create an electric car
    tesla = ElectricCar("Tesla", 2024, 4, battery_kwh=75)
    print(f"EV: {tesla.describe()}")        # ← extended describe
    print(f"Action: {tesla.start()}")        # ← overridden start
    print(f"Honk: {tesla.honk()}")           # ← inherited from Car
    print(f"Charge: {tesla.charge()}")       # ← EV-specific