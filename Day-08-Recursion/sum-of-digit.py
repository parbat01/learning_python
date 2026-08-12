
def digit(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(n<0):
        return "Please enter positive number.."
    else:
        a=n%10
        return  a+digit(n//10)
print( "The sum of a digit of a number is",digit(n=int(input("Enter a number"))))
