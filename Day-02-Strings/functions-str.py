word= "i am a coder. I am learning python. I love python"
print(word.endswith("hon")) # Returns ture if the string ends with hon
word=word.capitalize() # capitalize first character 
print(word)
print(word.replace("python","java"))#replace python with java
print(word.find("learning")) # gives 1st index of first occurrence
print(word.count("a")) # gives a number of how many "a" are there
reverse= "" .join(reversed(word)) # reverse the string
print(reverse)
print(word.upper())#this will covert all the character in uppercase
print(word.lower())#this will convert all the character in the lower case
print(word.isalnum())# returns true if string is made up of these character A-Z,a-z,0-9
print(word.isalpha())# returns true if string is made up of these character A-Z,a-z.
print(word.islower())#returns true if all the character in the string is in lower case





