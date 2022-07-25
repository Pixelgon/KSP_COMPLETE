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
text = origin.readline()
a = int(origin.readline())
b = int(origin.readline())
c = int(origin.readline())
d = int(origin.readline())
origin.close()
#volani funkce
output(text, a, b, c, d)
exit()
