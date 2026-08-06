#In this program i'll find the grade of a student
mark=int(input("Enter total mark of a student :"))
if(mark>=90 and mark<=100):
         print("Student achieved grade A")
elif(mark<90 and mark>=80):
         print("Student achieved grade B")
elif(mark<80 and mark>=70):
           print("Student achieved grade C")
elif(mark<70):
        print("Student achieved grade D")
else:
        print("You entered wrong number")

        