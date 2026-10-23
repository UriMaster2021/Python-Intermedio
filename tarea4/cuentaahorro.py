from .cuentabancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):

    TASA_INTERES = 0.001

    def extraer(self, monto):

        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero.")

        if monto <= self.saldo:

            self.saldo = self.saldo - monto

            print(f"Extracción exitosa: ${monto}")

            return True

        else:

            print("Error: saldo insuficiente.")

            return False

    def aplicar_interes(self):

        interes = self.saldo * self.TASA_INTERES

        self.saldo = self.saldo + interes

        print(f"Interés aplicado: ${interes:.2f}")
