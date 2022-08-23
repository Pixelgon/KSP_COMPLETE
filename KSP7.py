# -----------------------------------------------------------
# KSP7
# Vytvoril Matej Matejka
# -----------------------------------------------------------

# Nacetem file cislem
origin = open("01.in", "r")
numA = int(origin.readline())
numB = int(origin.readline())
origin.close()


def gcd(na, nb):
    if nb == 0:
        return na
    else:
        return gcd(nb, na % nb)


def lcm(x, y):
    return int(x * y / gcd(x, y))


output = open("01.out", "w")
output.write(str(gcd(numA, numB)) + "\n")
output.write(str(lcm(numA, numB)))
output.close()
exit()
