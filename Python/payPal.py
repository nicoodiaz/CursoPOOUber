from payment import Payment

class PayPal(Payment):
    referencia = str()
    sucursal = str()
    
    def __init__(self, id, referencia, sucursal):
        super().__init__(id)
        self.referencia = referencia
        self.sucursal = sucursal