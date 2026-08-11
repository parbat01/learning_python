#In this program i'll work with a small dataset of students and build a program that analyzes the data.
students = [
    {"name": "Ram", "age": 18, "marks": 78, "subject": "Python"},
    {"name": "Sita", "age": 19, "marks": 92, "subject": "Python"},
    {"name": "Hari", "age": 18, "marks": 65, "subject": "Python"},
    {"name": "Gita", "age": 20, "marks": 88, "subject": "Python"},
    {"name": "Mina", "age": 19, "marks": 45, "subject": "Python"},
    {"name": "Parbat", "age": 20, "marks": 34, "subject": "Python"}
]
def view_student():
    for i in range(len(students)):
        print(i+1, students[i].get("name"), "Age :", students[i].get("age"),"Marks :" ,students[i].get("marks"), "Subject :", students[i].get("subject"))

def cal_avg():
    sum=0
    for i in range(len(students)):
        avg=students[i].get("marks")
        sum+=avg
    print("The average of marks is : ", sum/len(students))

def high_mark():
                high=students[0].get("marks")
                stu=students[0] .get("name")
                for i in range(len(students)):
                    if (students[i].get("marks")>high):
                        high=students[i].get("marks")
                        stu=students[i] .get("name")
                print("Highest marks :",high)
                print("Student :",stu)
                

def low_mark():
                low=students[0].get("marks")
                stu=students[0] .get("name")
                for i in range(len(students)):
                    if (students[i].get("marks")<low):
                        low=students[i].get("marks")
                        stu=students[i] .get("name")
                print("Lowest marks :",low)
                print("Student :",stu)
               


def passed():
                
                pased=False
                print(" ==== Passed students =====")
                for i in range(len(students)):
                    if(students[i].get("marks")>40):
                        print(i+1, students[i].get("name"))
                       
                        pased=True
                if not pased:
                    print("No student passed..!")

def failed():
                
                
                fail=False
                print(" ==== Failed students =====")
                for i in range(len(students)):
                    if(students[i].get("marks")<40):
                        print(i+1, students[i].get("name"))
                       
                        fail=True
                if not fail:
                    print("No student failed..!")
                


def unique_age():
                    unique=set()
                    
                    for i in range(len(students)):
                        unique.add(students[i].get("age"))
                    return unique
                    


def search_stu(name):
                found=False
                for i in range(len(students)):
                    if(students[i].get("name").lower()==name.lower()):
                        print("====Student found====")
                        print(i+1,".", students[i].get("name"),"\nAge :" , students[i].get("age"),"\nMarks :" , students[i].get("marks"), "\nSubject :" ,students[i].get("subject"))
                        found=True
                        break
                if not found:
                    print("Student not found..!")


def statics():
                print("======STATISTICS======")
                fail=0
                passs=0
                for i in students:
                    if i.get("marks")>40:
                        passs+=1
                    else:
                        fail+=1
                add=0
                for i in students:
                    add+=i.get("marks")
                
                print("Total Students :" , len(students))
                print("Average Marks : ", add/len(students))
                high_mark()
                low_mark()
                print("Passed Students : ",passs)
                print("Failed Students : ",fail)
                print("Unique Ages :",len(unique_age()),", i.e",unique_age())

while True:
    print(""" ================================
        STUDENT DATA ANALYZER
 ================================
                1. View all students
                2. Calculate average marks
                3. Find highest marks
                4. Find lowest marks
                5. Show passed students
                6. Show failed students
                7. Find unique ages
                8. Search student
                9. Show statistics
                10. Exit""")
    num=int(input("Enter a number :"))
    match num:
        case 1:
           view_student()
        case 2:
           cal_avg()
        case 3:
            high_mark()
        case 4:
          low_mark()
        case 5:
          passed()
        case 6:
          failed()
        
        case 7:
           unique_age()
        case 8:
            search_stu(name=input("Enter the name of a student :"))
        case 9:

            statics()
        case 10:
            print("Thank you for using student data analyzer...!")
            break
        case _:
            print("You  entered wrong number...!")
  
        
 