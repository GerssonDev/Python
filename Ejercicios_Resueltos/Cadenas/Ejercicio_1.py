"""
Escribir un programa que pregunte el nombre del usuario en la consola y 
un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

nombre = str(input("Ingrese su Nombre: "))
number = int(input("Ingrese un Numero: "))

print((nombre + "\n") * number)
