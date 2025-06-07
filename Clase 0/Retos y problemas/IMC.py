# Ejercicio del IMC 1

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en m: "))

imc = peso / (altura**2)

print("Tu IMC es de:", round(imc, 2))
