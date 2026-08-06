#In this program i'll use slicing concept of string and print the letter.
word="PythonProgramming"
print(word[0:6]) #This will only print python
#the last index of string will not print 
print(word[6:])#This will print programming we didn't write last index but python will 
#automatically detect as len(str) which is 17 
print(word[:10])
