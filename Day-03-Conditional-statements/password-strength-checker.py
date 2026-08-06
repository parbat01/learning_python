#In this program i'll check the strength of a given password
word=input("Enter your password:")
if(len(word)>=8):
        if(word.isalnum()==True ):
            print("Strength of a Password : strong")
        else:
            print("Strength of a Password : Medium")
   
else:
    print("Strength of a Password : Weak")
    