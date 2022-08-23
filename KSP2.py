# -----------------------------------------------------------
# KSP2
# Vytvoril Matej Matejka
# -----------------------------------------------------------

# Vypsani outputu
def output(text, a, b, c, d):
    out = open("01.out", "w")
    out.write(text[a:a+b]+"\n")
    out.write(text[c:-1-d]+"\n")
    out.close()
    print("Hotovo!")


# Nacteni hodnot
origin = open("01.in", "r")
string = origin.readline()
aN = int(origin.readline())
bN = int(origin.readline())
cN = int(origin.readline())
dN = int(origin.readline())
origin.close()
# volani funkce
output(string, aN, bN, cN, dN)
exit()
