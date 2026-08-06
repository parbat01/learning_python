word= "i am a coder. I am learning python. I love python"
print(word.endswith("hon")) # Returns ture if the string ends with hon
word=word.capitalize() # capitalize first character 
print(word)
print(word.replace("python","java"))#replace python with java
print(word.find("learning")) # gives 1st index of first occurrence
print(word.count("a")) # gives a number of how many "a" are there
reverse= "" .join(reversed(word)) # reverse the string
print(reverse)


