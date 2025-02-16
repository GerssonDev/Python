"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""

pan_precio = 3.49
descuento = 0.6

barras = int(input("Introducir el número de barras vendidas que no son frescas: "))
coste = barras * pan_precio * (1 - descuento)

print("El coste de una barra fresca es " + str(pan_precio) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")