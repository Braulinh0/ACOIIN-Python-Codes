# Reto
# Intercambia los valores de variable1 y de variable2 de modo que después de hacerlo te quede:
# valor de la variable 1: 3.14
# valor de la variable 2: 1000

v_1 = 3.14
v_2 = 1000

print("Antes:\n")
print("Valor de la variable 1:", v_1)
print("Valor de la variable 2:", v_2, "\n")

aux = v_1
v_1 = v_2
v_2 = aux

print("Después:\n")
print("Valor de la variable 1:", v_1)
print("Valor de la variable 2:", v_2, "\n")
