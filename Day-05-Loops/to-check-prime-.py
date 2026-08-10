#In this program i'll check whether the number is prime or composite
num=int(input("Enter your number :"))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1

if(count==2):
    print("The number is prime")
else:
    print("The number is composite")