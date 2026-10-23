from .cuentabancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):

    def __init__(
        self,
        titular,
        cbu,
        saldo_inicial=0,
        limite_descubierto=500
    ):
        self.limite_descubierto = limite_descubierto
        super().__init__(titular, cbu, saldo_inicial)

    def _saldo_minimo(self):
        return -self.limite_descubierto

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero.")
        disponible = self.saldo + self.limite_descubierto
        if monto <= disponible:
            self.saldo = self.saldo - monto
            print(f"Extracción exitosa: ${monto}")
            return True
        else:
            print("Error: límite de descubierto excedido.")
            return False
