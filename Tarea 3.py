#Ejercicio 1
A = float(input("Ingrese el primer número: "))
B = float(input("Ingrese el segundo número: "))

C = A if A > B else B

print("El mayor es:", C)

#Ejercicio 2
def buscapa(palabrabuscada, *args):
    return "Palabra encontrada" if palabrabuscada in args else "Palabra no encontrada"

texto = input("Ingrese un texto separado las palabras por espacios: ").split()
palabrabuscada = input("¿Qué palabra quiere buscar?: ")

resultado = buscapa(palabrabuscada, *texto)
print(resultado)

#Ejercicio 3

A = float(input("Ingrese un número para ver si es par o impar: "))
resultado = "Par" if A % 2 == 0 else "Impar"
print("El número es:", resultado)

#Ejercicio 4
def calpromedio(*args):
    return sum(args) / len(args) if len(args) > 0 else 0

numeros = input("Ingrese números separados por espacios: ").split()
numeros = [float(numero) for numero in numeros]

promedio = calpromedio(*numeros)

print("El promedio es:", promedio)

#Ejercicio 5
def validar_argumentos(funcion): 
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) < 2:
            print("Error, se necesitan como minimo dos argumentos")
        else:
            return funcion(*args, **kwargs)
    return wrapper

@validar_argumentos
def sumar(a, b):
    return a + b

print(sumar(5, 3)) #Pruebo con 2
print(sumar(5)) #Pruebo con 1
print(sumar()) #Pruebo con 0 
