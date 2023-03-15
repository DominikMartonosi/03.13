szamok = []
while True:
    szam = input("Írj egy számot: ")
    try:
        szam = int(szam)
        if szam < -5 or szam > 5:
            break
        szamok.append(szam)
    except ValueError:
        break

print("Megadott számok: ", szamok)
print("A számok összege: ", sum(szamok))