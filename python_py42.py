def szamolas(a):
    return 2*a - 3

lista = []

for a in range(0, 5):
    ertek = szamolas(a)
    if ertek not in lista:
        lista.append(ertek)

print("Nem negatív elemek: ", [ertek for ertek in lista if ertek >= 0])