# -----------------------------------------------------------
# KSP3
# Vytvoril Matej Matejka
# -----------------------------------------------------------
import math


def isprime(cislo):
    if cislo == 1:
        return False

    if cislo == 2:
        return True
    if cislo > 2 and cislo % 2 == 0:
        return False

    max_delitel = math.floor(math.sqrt(cislo))
    for a in range(3, 1 + max_delitel, 2):
        if cislo % a == 0:
            return False
    return True


origin = open("01.in", "r")
n = int(origin.readline())
output = open("01.out", "w")


while n != 0:
    num = int(origin.readline())
    if isprime(num):
        output.write("PRVOCISLO"+"\n")
    else:
        output.write("SLOZENE"+"\n")
    n -= 1

origin.close()
output.close()
print("Hotovo!")
exit()
