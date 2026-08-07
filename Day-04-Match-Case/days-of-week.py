#In this program i'll show the days of a week according to the number that user give
x=int(input("Enter number between (1-7) :"))
match x:
    case 1 :
        print("Sunday")
    case 2 :
        print("Monday")
    case 3 :
        print("Tuesday")
    case 4 :
        print("Wednesday")
    case 5 :
        print("Thursday")
    case 6 :
        print("Friday")
    case 7 :
        print("Saturday")
    case _ :
        print("You entered wrong number")

            

