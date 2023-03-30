from car import Car

def clases():
    car = Car()
    car.license = 'AMS234'
    car.driver = 'Andres Herrera'
    print(vars(car))
    
    car2 = Car()
    car2.license = 'OUL929'
    car2.driver = 'Nicolas Diaz'
    print(vars(car2))

if __name__ == '__main__':
    clases()