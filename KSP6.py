# -----------------------------------------------------------
# KSP6
# Vytvoril Matej Matejka
# -----------------------------------------------------------

def dectoany(num, base):
    solve = ""
    # Dokud cislo je vetsi nez nula
    while num > 0:
        # Zbytek je roven zbytku po deleni cisla zakladem
        zbytek = int(num % base)
        # Pokud je zbytek mensi nez 10
        if zbytek < 10:
            # Zbytek priradime do vysledku
            solve += str(zbytek)
        else:
            # Zbytek nahradime cislem a priradime do vysledku
            solve += chr(ord('A') + zbytek - 10)
        # Cislo vydelime zakladem
        num //= base
    solve = solve[::-1]
    # Vysledek vypiseme
    return solve


# Nacetem file cislem
origin = open("01.in", "r")
# precteme vstup, prevedeme na tuple
numeral = int(origin.readline().strip())
origin.close()
numeralbase = 2
maxBase = 0
maxZeroes = 0
print("Probíha výpočet, čekejte prosím...")

while True:
    collection = dectoany(numeral, numeralbase)
    zeroes = 0
    for i in collection[::-1]:
        if i == "0":
            zeroes += 1
        else:
            break
    if zeroes >= maxZeroes:
        maxZeroes = zeroes
        maxBase = numeralbase
    numeralbase += 1
    if len(collection) <= maxZeroes:
        break
output = open("01.out", "w")
output.write(str(maxBase))
output.close()
exit()
