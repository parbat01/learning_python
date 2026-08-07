#In this program i'll simply design a food ordering system
print("Welcome to the Parbat's Greatest Resturant")
print("""Here is the menu:
    1.Pizza
    2.Burger
    3.Naan Roti
    4.MOMO
    5.Chilli Chicken
    6.Wings
    7.Noodles
    8.Salad
    9.Coffee
    10.Tea""")
x=int(input("Enter the number of a food which you want to eat :"))
match x:
    case 1:
        print("You selected Pizza.")
        a=int(input("Please tell us the quantity of the Pizza :"))
        print("Item:Pizza\nQuantity:",a ,"\nPrice per Pizza: 250\nTotal price :",(250*a))
        print("Thank you for your order!")
    case 2:
        print("You selected Burger.")
        a=int(input("Please tell us the quantity of the Burger :"))
        print("Item:Burger\nQuantity:",a ,"\nPrice per Burger: 150\nTotal price :",(150*a))
        print("Thank you for your order!")
    case 3:
        print("You selected Naan Roti.")
        a=int(input("Please tell us the quantity of the Naan Roti :"))
        print("Item:Naan Roti\nQuantity:",a ,"\nPrice per Naan Roti: 50\nTotal price :",(50*a))
        print("Thank you for your order!")
    case 4:
        print("You selected MOMO.")
        a=int(input("Please tell us how many plate of  MOMO you want:"))
        print("Item:MOMO\nQuantity:",a ,"\nPrice per Plate: 100\nTotal price :",(100*a))
        print("Thank you for your order!")
    case 5:
        print("You selected Chilli Chicken.")
        a=int(input("Please tell us how many plate of Chilli Chicken you want :"))
        print("Item:Chilli Chicken\nQuantity:",a ,"\nPrice per plate: 130\nTotal price :",(130*a))
        print("Thank you for your order!")
    case 6:
        print("You selected Wings.")
        a=int(input("Please tell us the quantity of the Wings :"))
        print("Item:Wings\nQuantity:",a ,"\nPrice per Wings: 60\nTotal price :",(60*a))
        print("Thank you for your order!")
    case 7:
        print("You selected Noodles.")
        a=int(input("Please tell us how many bowl of Noodles you want :"))
        print("Item:Noodles\nQuantity:",a ,"\nPrice per bowl: 80\nTotal price :",(80*a))
        print("Thank you for your order!")
    case 8:
        print("You selected Salad.")
        a=int(input("Please tell us how many plate  of Salad you want :"))
        print("Item:Salad\nQuantity:",a ,"\nPrice per plate: 40\nTotal price :",(40*a))
        print("Thank you for your order!")
    case 9:
        print("You selected Coffee.")
        a=int(input("Please tell us the quantity of the Coffee :"))
        print("Item:Coffee\nQuantity:",a ,"\nPrice per Coffee: 30\nTotal price :",(30*a))
        print("Thank you for your order!")
    case 10:
        print("You selected Tea.")
        a=int(input("Please tell us the quantity of the Tea :"))
        print("Item:Tea\nQuantity:",a ,"\nPrice per Tea: 20\nTotal price :",(20*a))
        print("Thank you for your order!")
    case _:
        print("Sorry...You entered wrong number")
    
