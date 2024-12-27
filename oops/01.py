class Car: #class and object
    total_car = 0 
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def full_name(self):
            return f"{self.__brand} {self.model}"
     # Encapsulation
    def get_brand(self):
          return self.__brand

     # Polymorphism
    def fuel_type(self):
     return "Petrol or diesel"
    
# Inheritance
class ElectricCar(Car):
     def __init__(self,brand,model,battery_size):
          super().__init__(brand,model)
          self.battery_size = battery_size
    
     def electric_car_detail(self):
          return f"{self.brand} {self.model} {self.battery_size}"

     def fuel_type(self):
          return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S","80kWH")
# print(my_tesla.brand)
# print(my_tesla.model)
# print(my_tesla.electric_car_detail())
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

safari = Car("Tata","safari")
# print(safari.fuel_type())


my_car = Car("Toyota","Porsche")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())

print(Car.total_car)
