"""
Day 13 - Polymorphism in action
Shows how inheritance enables flexible, reusable code.
"""

# Re-using the classes from day13_basics
from day13_basics import Vehicle, Car, ElectricCar


def show_vehicle_info(vehicle):
    """
    Display info about ANY vehicle.
    Works on Vehicle, Car, ElectricCar - or any future subclass!
    """
    print(f"  📋 {vehicle.describe()}")
    print(f"  🔑 {vehicle.start()}")


def start_all_vehicles(vehicles):
    """
    Start a whole list of mixed vehicle types.
    No need to know which is which - polymorphism handles it.
    """
    print("\n🚗 Starting fleet...")
    for v in vehicles:
        print(f"  → {v.start()}")


def find_electric_cars(vehicles):
    """
    Filter a mixed list to find only electric cars.
    Uses isinstance() to check types.
    """
    return [v for v in vehicles if isinstance(v, ElectricCar)]


if __name__ == "__main__":
    # Create a mixed fleet of different vehicle types
    fleet = [
        Vehicle("Trek", 2024),
        Car("Toyota", 2023, 4),
        Car("Honda", 2022, 2),
        ElectricCar("Tesla", 2024, 4, 75),
        ElectricCar("Rivian", 2024, 4, 130),
    ]
    
    # Show info for each vehicle - same function handles all 3 types!
    print("📦 Fleet inventory:")
    for v in fleet:
        show_vehicle_info(v)
        print()
    
    # Start them all - polymorphism in action
    start_all_vehicles(fleet)
    
    # Filter for electric cars only
    print("\n⚡ Electric vehicles in fleet:")
    evs = find_electric_cars(fleet)
    print(f"  Found {len(evs)} EV(s)")
    for ev in evs:
        print(f"  → {ev.describe()}")
    
    # Demonstrate isinstance() with the inheritance chain
    print("\n🔍 Type checks for the Tesla:")
    tesla = fleet[3]
    print(f"  isinstance(tesla, ElectricCar) = {isinstance(tesla, ElectricCar)}")
    print(f"  isinstance(tesla, Car)         = {isinstance(tesla, Car)}")
    print(f"  isinstance(tesla, Vehicle)     = {isinstance(tesla, Vehicle)}")