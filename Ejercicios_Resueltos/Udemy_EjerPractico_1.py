print("Propocione los siguientes datos de un libro")
nombre = str(input("Propocionar el nombre del libro: "))
id = int(input("Propocionar el ID: "))
precio = float(input("Propocionar el precio: "))
envio = bool(input("Indica si el envio es gratuito (True / False): "))


print(f"Nombre: {nombre}")
print(f"ID: {id}")
print(f"Precio: {precio}")
print(f"envio gratuito?: {envio}")

print(type(envio))