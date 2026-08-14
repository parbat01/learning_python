# In this program i'll ask user to input a path and check whether the path exists or not and  many more
import os

count = 0
count1 = 0
fpath = input("Enter folder path :")
if os.path.exists(fpath):
    print(" The given path exists in your computer.")
    status = " The path is Folder" if os.path.isdir(fpath) else " The path is File "
    print(status)
    l = os.listdir(fpath)
    print("All the files and folders are :", l)
    for i in l:
        full_path = os.path.join(fpath, i)

        if os.path.isfile(full_path):
            count += 1
        else:
            count1 += 1
    print("Total number of file is :", count)
    print("Total number of folder is :", count1)

else:
    print("The given path do not exists in your computer")
