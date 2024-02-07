from itertools import product

def producto_cartesiano(conjunto1, conjunto2):
    return list(product(conjunto1, conjunto2))

conjunto1 = {}
conjunto2 = {}
conjunto1 = (input("Ingresa elementos, separados por comas, para el primer conjunto: "))
conjunto2 = (input("Ingresa elementos, separados por comas, para el segundo conjunto: "))
resultado = producto_cartesiano(conjunto1, conjunto2)
print(resultado)

