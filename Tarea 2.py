"""Ejercicio 1: Escribe un programa que intente dividir dos números. 
Si el segundo número es cero, captura la excepción ZeroDivisionError 
y muestra un mensaje de error al usuario."""

nro1 = float(input("Ingrese el primer número: "))
nro2 = float(input("Ingrese el segundo número: "))

try:
    resultado = nro1 / nro2
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

"""Ejercicio 2: Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario."""

nro= 1
cadena= "Damian"

try:
    resultado = nro + cadena
    print("El resultado de la suma es:", resultado)
except TypeError:
    print("Error: No se puede sumar un número y una cadena.")


"""Ejercicio 3: Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra"""

persona = {
    "nombre": "Damian",
    "edad": 25
}

try:
    print(persona["direccion"])

except KeyError:
    print("Error: la clave no existe en el diccionario.")


"""Ejercicio 4: Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe.
"""
nombre_archivo = "archivo.txt"

try:
    with open(nombre_archivo, "r") as archivo:
        print(archivo.read())

except FileNotFoundError:
    print("Error: el archivo no existe.")

    with open(nombre_archivo, "w") as archivo:
        archivo.write("Archivo creado automáticamente.")

    print("Se creó el archivo correctamente.")



"""Ejercicio 5: Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
"""
try:
    nro1 = float(input("Ingrese el primer número: "))
    nro2 = float(input("Ingrese el segundo número: "))

    resultado = nro1 / nro2

    print("Resultado:", resultado)

except ValueError:
    print("Error: debe ingresar un número válido.")

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")