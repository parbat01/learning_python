#In this program i'll check whether the given word is palindrome or not
word=input("Enter your word :")
reverse="".join(reversed(word))
if(reverse==word):
    print("The word is palindrome")

else:
    print("The word is not palindrome")
