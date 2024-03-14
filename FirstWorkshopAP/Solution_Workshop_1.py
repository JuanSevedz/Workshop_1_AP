"""
This program is a vehicle catalog that allows users to view, add, 
and filter different types of vehicles, such as cars, trucks, yachts, 
and motorcycles. Users can perform these actions through an interactive menu.
"""

class Engine:
    """
    Class  for the engine object in a vehicle.
    
    Attributes:
        -engine_type (str): Tipo de motor (por ejemplo, "Gasolina", "Diésel", etc.).
        -potency (int): Potencia del motor en caballos de fuerza.
        -weight (float): Peso del motor en kilogramos.
    """
    def __init__(self, engine_type, potency, weight):
        """
       This function  initializes the attributes of the class 'Engine'.
       
       """
        self.engine_type = engine_type
        self.potency = potency
        self.weight = weight

class Vehicle:
    """
    This class represents  a generic vehicle with common attributes and one diferent than each others.
    
    Attributes:
    
        -vehicle_type (str): Vehicle type ("Car", "Truck", "Yacht", "Motorcycle").
        -chassis (str): Chassis type of the vehice ('A' o 'B').
        -model (str): Vehicle model like(spor, luxury, conventional, sedan,etc).
        -gas_consumption (float): Vehicle gasoline consumption.
        -year (int): When was manufactured the vehicle in years.
        -engine (Engine): Engine associate to the vehicle.
    """
    def __init__(self, vehicle_type, chassis, model, gas_consumption, year, engine):
        """
       This function  is used to initialize a new instance of the class Vehicle.
       
       """
        self.vehicle_type = vehicle_type
        self.chassis = chassis
        self.model = model
        self.gas_consumption = gas_consumption
        self.year = year
        self.engine = engine

    def calculate_gas_consumption(self):
        """
        Calcula el consumo de gasolina del vehículo.

        Returns:
            float: Consumo de gasolina calculado.
        """   
        chassis_factor= 0.3 if self.chassis == 'A' else 0.5 if self.chassis == 'B' else 0 
        return 1.1 * self.engine.potency + 0.2 * self.engine.weight - chassis_factor
    
class Car(Vehicle):
    """
    This class make a specific type of a vehicle, Car.
    """
    def __init__(self, chassis, model, gas_consumption, year, engine, num_doors):
        super().__init__('Car', chassis, model, gas_consumption, year, engine)
        self.num_doors = num_doors

class Truck(Vehicle):
    """
    This class make a specific type of a vehicle, Truck.
    """
    def __init__(self, chassis, model, gas_consumption, year, engine, payload_capacity):
        super().__init__('Truck', chassis, model, gas_consumption, year, engine)
        self.payload_capacity = payload_capacity

class Yacht(Vehicle):
    """
    This class make a specific type of a vehicle, Yacht.
    """
    def __init__(self, chassis, model, gas_consumption, year, engine, length):
        super().__init__('Yacht', chassis, model, gas_consumption, year, engine)
        self.length = length

class Motorcycle(Vehicle):
    """
    This class make a specific type of a vehicle, Motorcycle.
    """
    def __init__(self, chassis, model, gas_consumption, year, engine, num_wheels):
        super().__init__('Motorcycle', chassis, model, gas_consumption, year, engine)
        self.num_wheels = num_wheels


def vehicle_info(vehicle):
    """
    This function show all information of Vehicles.
    """
    print(f"Type: {vehicle.vehicle_type}")
    print(f"Chassis: {vehicle.chassis}")
    print(f"Model: {vehicle.model}")
    print(f"Year: {vehicle.year}")
    print(f"Gas Consumption: {vehicle.gas_consumption}")
    print(f"Engine Type: {vehicle.engine.engine_type}")
    print(f"Engine Potency: {vehicle.engine.potency}")
    print(f"Engine Weight: {vehicle.engine.weight}")
    
    #Specific attributes for subclasses
    if isinstance(vehicle, Car):
        print(f"Number of Doors: {vehicle.num_doors}")
    elif isinstance(vehicle, Truck):
        print(f"Payload Capacity: {vehicle.payload_capacity}")
    elif isinstance(vehicle, Yacht):
        print(f"Length: {vehicle.length}")
    elif isinstance(vehicle, Motorcycle):
        print(f"Number of Wheels: {vehicle.num_wheels}")

    print("\n")

# Initial Catalog
engine1 = Engine('Gasoline', 200, 300)

car1 = Car('A', 'Sedan', 0, 2022, engine1, 4)
car1.gas_consumption = car1.calculate_gas_consumption()

truck1 = Truck('B', 'Pickup', 0, 2020, engine1, 1000)
truck1.gas_consumption = truck1.calculate_gas_consumption()

yacht1 = Yacht('A', 'Luxury', 0, 2023, engine1, 50)
yacht1.gas_consumption = yacht1.calculate_gas_consumption()

motorcycle1 = Motorcycle('B', 'Sport', 0, 2021, engine1, 2)
motorcycle1.gas_consumption = motorcycle1.calculate_gas_consumption()

vehicles = [car1, truck1, yacht1, motorcycle1]

def show_all_vehicles(vehicles):
    """
    This function show the  information of all vehicles in a list.
    """
    print("Catalog of Vehicles:")
    for vehicle in vehicles:
        vehicle_info(vehicle)

def show_vehicle_type(vehicles, vehicle_type):
    """
    This function show a specifict part of the catalog wanted  by the user.
    It receives as parameter a string that represents the type of vehicle we want to see and a list with all the vehicles from the catalog.
    """
    filtered_vehicles = [vehicle for vehicle in vehicles if isinstance(vehicle, vehicle_type)]
    if filtered_vehicles:
        print(f"Catalog of {vehicle_type.__name__}s:")
        for vehicle in filtered_vehicles:
            vehicle_info(vehicle)
    else:
        print(f"No {vehicle_type.__name__}s found in the catalog.")

def add_vehicle_to_catalog(vehicles):
    """"
    This function adds a new vehicle to the catalog.
    """
    chassis = input("Enter chassis type (A/B): ").upper()  # Pass the letter to Capital letters for exception.
    if chassis not in ['A', 'B']:
        print("Invalid chassis type. Please enter 'A' or 'B'.")
        return

    model = input("Enter vehicle model: ")
    year = int(input("Enter year: "))
    engine_type = input("Enter engine type: ")
    potency = int(input("Enter engine potency: "))
    weight = float(input("Enter engine weight: "))
    engine = Engine(engine_type, potency, weight)

    vehicle_type = input("Enter vehicle type (Car/Truck/Yacht/Motorcycle): ")
    if vehicle_type == 'Car':
        num_doors = int(input("Enter number of doors: "))
        vehicle = Car(chassis, model, 0, year, engine, num_doors)
    elif vehicle_type == 'Truck':
        payload_capacity = float(input("Enter payload capacity: "))
        vehicle = Truck(chassis, model, 0, year, engine, payload_capacity)
    elif vehicle_type == 'Yacht':
        length = float(input("Enter length: "))
        vehicle = Yacht(chassis, model, 0, year, engine, length)
    elif vehicle_type == 'Motorcycle':
        num_wheels = int(input("Enter number of wheels: "))
        vehicle = Motorcycle(chassis, model, 0, year, engine, num_wheels)
    else:
        print("Invalid vehicle type. Vehicle not added to catalog.")
        return

    vehicle.gas_consumption = vehicle.calculate_gas_consumption()
    vehicles.append(vehicle)
    print("Vehicle added to catalog.")


def menu(vehicles):
    """
    This  function displays the main menu and handles user inputs.
    """
    while True:
        print("\nMenu:")
        print("1. Show Catalog")
        print("2. Show vehicles of a specific type")
        print("3. Add a vehicle to the catalog")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_all_vehicles(vehicles)
        elif choice == '2':
            vehicle_type = input("Enter vehicle type (Car/Truck/Yacht/Motorcycle): ")
            if vehicle_type in ['Car', 'Truck', 'Yacht', 'Motorcycle']:
                show_vehicle_type(vehicles, eval(vehicle_type))
            else:
                print("Invalid vehicle type.Please choose one  of the options above.")
        elif choice == '3':
            add_vehicle_to_catalog(vehicles)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

#Deploy the menu
menu(vehicles)
