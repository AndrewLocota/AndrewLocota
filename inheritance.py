class Vehicle:
    
    def _init_(self, registration):
        self._registration = registration

    def get_registration(self):
        return(self._registration)
    
class Car(Vehicle):
    pass

class Bus(Vehicle):
    pass

my_car = Car("AA")
print(my_car.get_registration())    

print()