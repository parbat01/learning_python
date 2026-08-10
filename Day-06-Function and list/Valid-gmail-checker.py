
#In this program i'll check the validation of a email . whether it is a valid email or not 
def gmail_checker(word):
    if(word.endswith("gmail.com")==True):
        if not " " in word:
            if not  word[0].isdigit():
                if word[0].islower():
                    if word[len(word)-10]=="@":
                        if  any(char.isdigit() for char in word[1:len(word)-10]):
                     
                        
                            print("Gmail created successfully!!!!!!")
                        else:
                             print("Gmail must contain number\nPlease re-enter your gmail")
                             gmail_checker(word=(input("Create  your gmail  :")))
                    else:
                        print("Invalid place of @.This must be placed before 'gmail.com'\nPlease re-enter your gmail")
                        gmail_checker(word=(input("Create  your gmail  :"))) 
                       
                else:
                    print("First letter of your gmail shouldn't be capital\nPlease re-enter your gmail")
                    gmail_checker(word=(input("Create  your gmail  :")))
            else:
                print("Sorry..!Gmail cannot start with a number\nPlease re-enter your gmail")
                gmail_checker(word=(input("Create  your gmail  :")))
            
        else:
            print("Gmail must not contain space\nPlease re-enter your gmail ")
            gmail_checker(word=(input("Create  your gmail  :")))
    else:
        print("Invalid gmail. Please put gmail.com at last \nPlease re-enter your gmail ")
        gmail_checker(word=(input("Create  your gmail  :")))
        
   
      


gmail_checker(word=(input("Create  your gmail  :")))
