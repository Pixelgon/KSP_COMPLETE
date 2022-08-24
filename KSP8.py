# -----------------------------------------------------------
# KSP8
# Vytvoril Matej Matejka
# -----------------------------------------------------------
from math import ceil, floor, sqrt

def isprime(cislo):
    if cislo == 1:
        return False

    if cislo == 2:
        return True
    if cislo > 2 and cislo % 2 == 0:
        return False

    max_delitel = floor(sqrt(cislo))
    for a in range(3, 1 + max_delitel, 2):
        if cislo % x == 0:
            return False
    return True

origin = open("01.in", "r")
n = int(origin.readline())
origin.close()

odmocnina = ceil(floor(n))
radek = " " * odmocnina
sloupec = []
for i in range(odmocnina):
    sloupec.append(radek)
x = odmocnina // 2
y = odmocnina // 2

if odmocnina % 2 == 0:
    x -= 1
    y -= 1

sloupec[y] = sloupec[y][:x] + "X" + sloupec[y][x+1:]
smer = 0

for i in range(2, n ):
    if smer == 0:
        x += 1
        if sloupec[y-1][x] == " ":
            smer = 1
        if smer == 1:
            y -= 1
            if sloupec[y][x-1] == " ":
                smer = 2
        if smer == 2:
            x -= 1
            if sloupec[y+1][x] == " ":
                smer = 3
        if smer == 3:
            y += 1
            if sloupec[y][x+1] == " ":
                smer = 0
        if isprime(i):
            sloupec[y] = sloupec[y][:x] + "#" + sloupec[y][x + 1:]
        else:
            sloupec[y] = sloupec[y][:x] + "." + sloupec[y][x + 1:]

output = open("01.out", "w")
for x in sloupec:
    output.write(x + "\n")
output.close()
exit()

