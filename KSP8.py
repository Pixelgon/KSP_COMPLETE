# -----------------------------------------------------------
# KSP8
# Vytvoril Matej Matejka
# -----------------------------------------------------------
from math import ceil, floor, sqrt

def isprime(N):
    prime_num = True
    for j in range(2, N):
        if (N % j) == 0:
            prime_num = True
            return True
            break

origin = open("01.in", "r")
n = int(origin.readline())
origin.close()

odmocnina = ceil(sqrt(n))
radek = " " * odmocnina + " "
sloupec = []
for i in range(odmocnina):
    sloupec.append(radek)
x = odmocnina // 2
y = odmocnina // 2
sloupec[y] = sloupec[y][:x] + "X" + sloupec[y][x+1:]
smer = 0

for i in range(2, n+1):
        if smer == 0: #smer vpravo
            x += 1
            if sloupec[y-1][x] == " ":
                smer = 1 
        elif smer == 1: 
            y -= 1
            if sloupec[y][x-1] == " ":
                smer = 2 
        elif smer == 2: 
            x -= 1
            if sloupec[y+1][x] == " ":
                smer = 3 
        elif smer == 3: 
            y += 1
            if sloupec[y][x+1] == " ":
                smer = 0 
        if isprime(i) is True:
            sloupec[y] = sloupec[y][:x] + "." + sloupec[y][x + 1:]
            print("yes")
        else:
            sloupec[y] = sloupec[y][:x] + "#" + sloupec[y][x + 1:]
            print("no")

output = open("01.out", "w")
stripped = list(map(str.strip, sloupec))
for x in stripped:
    output.write(x + "\n")
output.close()
exit()

