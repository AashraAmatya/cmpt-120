print ("This program calculates a student's grade average.")
grades = []
while(True):
    grade = float(input("Enter grade: "))
    if grade < 0 :
        break 
    grades.append(grade)

total = 0.0
for grade in grades:
   total = total + grade

final = total/(len(grades))
print ("Student's average = " + str(final))
if final >= 90:
    print ("Student's average grade: A+")
elif final >= 85 and final <90:
    print ("Student's average grade: A")
elif final >=80 and final <85:
    print ("Student's average grade: B+")
elif final >=75 and final <80:
    print ("Student's average grade: B")
elif final >=70 and final <75:
    print ("Student's average grade: C+")
else:
    print ("Student's average grade: C")


    
