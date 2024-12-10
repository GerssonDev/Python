"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""

horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
coste_hora = float(input("Ingrese el coste por hora: "))
pagar = horas_trabajadas * coste_hora

print("Su paga es de: ", pagar)