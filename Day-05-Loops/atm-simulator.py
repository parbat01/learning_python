
#In this program i've used do-while loop to display the facility of a atm and user will enter the user to get that facility 
balance=2000
trans=[]
while True:
    print("""========== ATM ==========
                1. Check Balance
                2. Deposit Money
                3. Withdraw Money
                4. Transaction History
                5. Exit""")
    num=int(input("Choose an option :"))
    match num:
        case 1:
            print("Your balance is :",balance)
        case 2:
            money=int(input("Enter the money you want to deposite :"))
            if(money>1):
                balance+=money
                trans.append("Deposited:" + str(money))
                print("Rs.",money,"deposited successfully !\n Your new balance :",balance)
            else:
                print("Please enter right amount.!!")
        case 3:
            money1=int(input("Enter the money you want to withdraw :"))
            if(balance>money1 and money1>1):
                balance-=money1
                trans.append("Withdrawn:" + str(money1))
                print("Rs.",money1,"withdrawn successfully !\n Your new balance :",balance)
            else:
                print("Insuficient balance.!!")
        case 4:
            
            
            print("=====Transaction History=====")
            for transaction in trans:
                print(transaction)
        case 5:
            print("Thankyou for banking with us.!!!")
            break
        case _:
            print("Invalid number")

