 #In this i'll build a simple Student Management System for a small class.
names=[]
ages=[]
mark=[]
while True:
    print(""" ========== STUDENT MANAGEMENT SYSTEM ==========

                    1. Add Student
                    2. View Students
                    3. Search Student
                    4. Calculate Class Result
                    5. Delete Student
                    6. Exit""")
    num=int(input("Enter the number :"))
    match num:
        case 1:
            
            def add_stu(name):
                
                if  not any(char.isdigit() for char in name ):
                    names.append(name)
                else:
                    print("There should not be any number in the name\nPlease re-enter name ")
                    add_stu(name=input("Enter full name of a student :"))
            add_stu(name=input("Enter full name of a student :"))
            def add_stu1(age):
                if (age>0and age<25):
                    
                    ages.append(age)
                else:
                    print("Please enter valid age..!!")
                    add_stu1(age=int(input("Enter age of a student :")))
            add_stu1(age=int(input("Enter age of a student :")))
            def add_stu2(marks):
                
                if (marks>=0 and marks<=100):
                    mark.append(marks)
                else:
                    print("Please enter valid marks..!!")
                    add_stu2(marks=float(input("Enter marks of a student :")))
            add_stu2(marks=float(input("Enter marks of a student :")))
                
        case 2:
            if len(names)>0:
                print("======Students=======")
                for i in  range(len(names)):
                    print(i+1,".","Name :", names[i] ,"Age :", ages[i], "Mark :", mark[i])
            else:
                print("No student found.")
        case 3:
            stu_name=input("Enter student name :")
            for i in range(len(names)):
                if(names[i]==stu_name):
                    print("!!Student found!!")
                    print(i+1,".","Name :", names[i] ,"Age :", ages[i], "Mark :", mark[i])
                    break
            else:
                print("!!!!Student not found....!!!!")
        case 4:
            print("Total number of students : ",len(names))
            calcu=0
            for i in range(len(names)):
                calcu+=mark[i]
            avg=calcu/(len(names))
            print("The average mark of a class :",avg)
            high=mark[0]
            for i in mark:
                if i>high:
                    high=i
            print("The highest mark of a class :",high)
            small=mark[0]
            for i in mark:
                if i<small:
                    small=i
            print("The lowest mark of a class is :",small)
            count=0
            for i in mark:
                if i>40:
                    count+=1
            print("The number of student passed is :" ,count)
            print("The number of student failed is :",(len(names)-count))
        case 5:
            stu_name=input("Enter student name you want to delete :")
            for i in range(len(names)):
                if(names[i]==stu_name):
                    names.pop(i)
                    ages.pop(i)
                    mark.pop(i)
                    print("Studenet deleted successfully..!")
                    break
            else:
                print("!!!!Student not found....!!!!")
            
        case 6:
            print("Thank you for using Student Management System...!!!!!")
            break
        case _:
            print("Please enter right number.")
   
    

