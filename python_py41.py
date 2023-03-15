def szamolas(a):
    return 2*a - 3

lista = []

for a in range(-3, 5):
    ertek = szamolas(a)
    if ertek not in lista:
        lista.append(ertek)

print("Értékkészlet elemei: ", lista)