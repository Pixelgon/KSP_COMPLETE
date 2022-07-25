# -----------------------------------------------------------
# KSP5
# Vytvoril Matej Matejka
# -----------------------------------------------------------

origin = open("01.in", "r")

studentN = int(origin.readline())
school = {}

for i in range(studentN):
    studentName = origin.readline().strip()
    teacherName = set()
    teacherN = int(origin.readline())
    for x in range(teacherN):
        teacherName.add(origin.readline().strip())
    school[studentName] = teacherName

origin.close()
students = list(school.keys())
breaktrought = school[students[0]]

for studentName in students:
    breaktrought = breaktrought & school[studentName]

output = open("01.out", "w")

if len(breaktrought) == 0:
    output.write("NEEXISTUJE\n")
else:
    output.write("%r" % (breaktrought[0]))


StudentMaxTeacherA = ""
StudentMaxTeacherB = ""
MaxTeachersN = 0

pos = 0

for StudentA in students:
    pos += 1
    for StudentB in students[pos:]:
        unifTeacher = school[StudentA] | school[StudentB]
        if len(unifTeacher) > MaxTeachersN:
            StudentMaxTeacherA = StudentA
            StudentMaxTeacherB = StudentB
            MaxTeachersN = len(unifTeacher)

output.write("%s %s\n" % (StudentMaxTeacherA, StudentMaxTeacherB))

output.close()
print("Hotovo!")
exit()
