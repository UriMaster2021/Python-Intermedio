class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"El coche {self.marca} {self.modelo} está encendido.")   

    def apagar(self):
        self.encendido = False
        print(f"El coche {self.marca} {self.modelo} está apagado.")



coche= Coche("Toyota", "Corolla", "Rojo") 
coche2= Coche("Honda", "Civic", "Azul")

print(coche.marca)  # muesta Toyota
print(coche2.modelo)  # muestra Civic
print(coche.color)  # muestra Rojo

coche.encender()
print(coche.encendido)  # muestra True
coche2.apagar()
print(coche2.encendido)  # muestra False

