import random

lista = [random.randint(1, 10) for i in range(5)]

osszeg = sum(szam for szam in lista if szam % 2 == 0)

print("Lista elemei: ", lista)

paros = [szam for szam in lista if szam % 2 == 0]
print("Páros elemei: ", paros)

print("Páros elemek összege: ", osszeg)