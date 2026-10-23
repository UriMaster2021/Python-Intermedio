from .cuentabancaria import CuentaBancaria


class CuentaCheque(CuentaBancaria):

    def __init__(
        self,
        titular,
        cbu,
        saldo_inicial=0,
        costo_emision=50
    ):
        super().__init__(titular, cbu, saldo_inicial)
        self.costo_emision = costo_emision


    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero.")
        total = monto + self.costo_emision
        if total <= self.saldo:
            self.saldo = self.saldo - total
            print(
                f"Extracción exitosa: ${monto} "
                f"| Comisión: ${self.costo_emision}"
            )
            return True
        else:
            print("Error: saldo insuficiente para cubrir la extracción y comisión.")
            return False
