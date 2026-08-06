# Ask the user for the bill amount.
# If the bill is 1000 or more, give a 10% discount.
# Otherwise, no discount.
# Print:
# Original bill
# Discount
# Final amount
# Bonus: If the bill is over 5000, give a 20% discount.

bill=float(input("Enter your bill amount :"))
if(bill>=1000 and bill<5000):
    print("Congratulation you get 10% discount!!!")
    print(" Original bill :",bill ,"\n","Discount :","10% of",bill,"\n","Final amount :",(bill-((10)/100)*bill))
elif(bill>5000):
      print("Congratulation you get 20% discount!!!")
      print(" Original bill :",bill ,"\n","Discount :","20% of",bill,"\n","Final amount :",(bill-((20)/100)*bill))
else:
    print("No any discount")
    print("Original bill :",bill ,"\n","Discount :0%\n" "Final amount :",bill)