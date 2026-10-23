from abc import ABC, abstractmethod

class CuentaBancaria(ABC):

    def __init__(self, titular, cbu, saldo_inicial=0):
        self.titular = titular
        self._cbu = cbu
        self.saldo = saldo_inicial

    @property
    def cbu(self):
        return self._cbu

    def _saldo_minimo(self):
        return 0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < self._saldo_minimo():
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = valor


    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero.")
        self.saldo = self.saldo + monto
        print(f"Depósito exitoso: ${monto}")


    @abstractmethod
    def extraer(self, monto):
        pass

    def __str__(self):
        return (
            f"[{self.__class__.__name__}] "
            f"Titular: {self.titular} | "
            f"CBU: {self.cbu} | "
            f"Saldo: ${self.saldo:.2f}"
        )
