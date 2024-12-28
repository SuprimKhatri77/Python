class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
class Car(Vehicle):
    def __init__(self,brand,model,year,fuel_type):
        super().__init__(brand,model,year)
        self.fuelType = fuel_type
    def car_brand(self):
        return f"Car Brand: {self.brand}"
    def car_model(self):
        return f"Car Model: {self.model}"
    def car_year(self):
        return f"Developed Year: {self.year}"
    def fuel_type(self):
        return f"Fuel Type: {self.fuelType}"
    
car1 = Car("Tesla","Model S","2022","Electric charge")
print(car1.car_brand())
print(car1.car_model())
print(car1.car_year())
print(car1.fuel_type())