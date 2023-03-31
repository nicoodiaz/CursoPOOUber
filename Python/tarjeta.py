from payment import Payment
from datetime import date


class Tarjeta(Payment):
    franquicia = str()
    fecha_vencimiento = date.today()
    cvv = int()
    
    def __init__(self, id, franquicia, fecha_vencimiento, cvv):
        super().__init__(id)
        self.franquicia = franquicia
        self.fecha_vencimiento = fecha_vencimiento
        self.cvv = cvv