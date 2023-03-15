import random

lista = [random.randint(1, 10) for i in range(5)]
osszeg = sum(lista)

print("Lista elemei: ", lista)

print("Annak összege: ", osszeg)