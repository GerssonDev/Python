"""
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interes anual: "))
n_años = int(input("Ingrese el numero de años: "))

capital_obtenido =  round( cantidad_invertir * (1 + (interes_anual / 100)) ** n_años,2)

print("El capital obtenido de la inversion es: ",capital_obtenido)
