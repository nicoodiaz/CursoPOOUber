from car import Car

class UberVan(Car):
    type_car_accepted = []
    seats_material = []
    
    def __init__(self, license, driver, type_car_accepted, seats_material):
        super.__init__(license, driver)
        self.type_car_accepted = type_car_accepted
        self.seats_material = seats_material
        
    def setPassenger(self, passenger):
        if passenger == 6:
            self.setPassenger = passenger
        else:
            print("You need yo assign 6 passengers")
