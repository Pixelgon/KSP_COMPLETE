# -----------------------------------------------------------
# KSP4
# Vytvoril Matej Matejka
# -----------------------------------------------------------

origin = open("01.in", "r")
nA = int(origin.readline())
sA = []
sB = []

for i in range(nA):
    sA.append(int(origin.readline()))
sA.sort()

nB = int(origin.readline())
for i in range(nB):
    sB.append(int(origin.readline()))
sB.sort()
origin.close()

ndvojic = 0
for x in sA:
    for y in sB:
        if x == y:
            ndvojic += 1

output = open("01.out", "w")
output.write(str(ndvojic))
output.close()
print("Hotovo!")
exit()
