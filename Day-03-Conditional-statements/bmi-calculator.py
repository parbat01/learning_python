#In this program i'll check the BMI of a person
# Less than 18.5	Underweight
# 18.5–24.9	Normal
# 25–29.9	Overweight
# 30 or above	Obese

wgt=float(input("Enter your body weight in kg :"))
height=float(input("Enter your height in metre :"))
bmi=wgt/(height**2)
if(bmi<18.5):
    print("You are Underweight")
elif(bmi>=18.5 and bmi<=24.9):
    print("You are normal")              
elif(bmi>=25 and bmi<=29.9):
    print("You are Overweight")
else:
    print("You are Obese")


