# Entrada de datos (input)
print("- Funciones para ingresar datos\n")

nombre = input("¿Cuál es tu nombre? ") # input permite ingresar datos
edad = input("¿Cuántos años tienes? ") # input permite ingresar datos

print("Nombre:", nombre, ", clase de dato:", type(nombre))
print("Edad:", edad, ", clase de dato:", type(edad))

# Si necesitas que la edad sea un int
edad = int(edad)
print("Edad:", edad, ", clase de dato:", type(edad))
# Si te percatas, la variable edad ya no es un str, sino, una clase int
