from car import Car
from account import Account

def clases():
    car = Car('OUL929', Account('Nicolas Diaz', 'RAR1504'))
    print(vars(car))
    print(vars(car.driver))
    
    
if __name__ == '__main__':
    clases()