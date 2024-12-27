class Car: 
    total_Car = 0
    # created a class
    def __init__(self,userbrand,usermodel):
        #yedi __ use garyo vane chai variable private huncha i.e it will be encapsulated and we have to access it via method
        self.__brand = userbrand
        self.__model = usermodel
        Car.total_Car += 1

    # encapsulation
    def get_brand(self):
        return self.__brand + "!"

    # class method and self
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    #polymorphism
    def fuel_type(self):
        return "Petrol or Desiel"

    # static method
    @staticmethod
    def general_description():
        return "Car is a means of transportation"
    
    # property decorator: it will not allow to override the orgiginal value and to acces the model we dont have to call func instead we can access it normaly like Car.model instead of Car.model()
    @property
    def model(self):
        return self.__model
    
    #inheritance
class ElectricCar(Car):
    def __init__(self,userbrand,usermodel,battery_size):
        super().__init__(userbrand,usermodel)
        self.batter_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"
    

my_tesla = ElectricCar("Tesla","Model S","85KwH")

# checking if my_tesla is an instance of Car and electric car or not
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))
# print(my_tesla.general_description())
# print(my_tesla.fuel_type())
# print(my_tesla.get_brand())
# print(my_tesla.brand,my_tesla.model,my_tesla.batter_size)
# print(my_tesla.model)
# print(my_tesla.batter_size)

safari = Car("Toyota","BMW")
# print(safari.model)
# print(safari.fuel_type())

# print(Car.total_Car)

# my_car = Car("Toyota","Corola")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

#multiple inheritance

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla","Model X")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())