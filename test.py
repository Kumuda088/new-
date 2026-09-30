from abc import ABC,abstractmethod

## Define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

## Derived class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"


## Derived class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

## Function that demonstates polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())


## Create objects of car and motorcycle
car = Car()
motorcycle = Motorcycle()
start_vehicle(car)