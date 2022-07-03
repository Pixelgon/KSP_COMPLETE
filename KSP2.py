# -----------------------------------------------------------
# KSP2
# Vytvoril Matej Matejka
# -----------------------------------------------------------

# Nacteni hodnot
origin = open("01.in", "r")
text = origin.readline()
a = int(origin.readline())
b = int(origin.readline())
c = int(origin.readline())
d = int(origin.readline())
origin.close()
# Vypsani outputu
out = open("01.out", "w")
out.write(text[a:a+b]+"\n")
out.write(text[c:-1-d]+"\n")
out.close()
exit()
