"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""

horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
coste_hora = float(input("Ingrese el coste por hora: "))
pagar = int (horas_trabajadas * coste_hora)

print(f"Su paga es de: {pagar}")