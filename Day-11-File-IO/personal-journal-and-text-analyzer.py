import datetime as d
import os

now = d.datetime.now()  # noqa: DTZ005
now = now.strftime(
    "%d-%m-%Y  %H:%M:%S"
)  # this will give us current date and time d,m,Y for day,month,year and H<M<S for hour,minutes,second
file_path = os.path.join(
    os.path.dirname(__file__), "Journal.txt"
)  # This will give us the filepath _fiile_ means where we are at right now   Now Journal.txt will be created in the same folder as your .py file, regardless of where you run the program from.


def write(new):
    with open(file_path, "a") as f:
        f.write(now)  # This will write current date and time
        f.write(" : " + "\n")  # This will write : and move to next line
        word = new.split()  # This will mak ea list of name words cotaining words from new separated by space
        line = ""  # we are going to add those words in this empty list. this is a string btw
        for words in word:
            if (
                len(list) + len(words) + 1 <= 115
            ):  # we used +1 because there is a space after every word so and we want only 115 character to prinyt in one line
                line += (
                    words + " "
                )  # imagine words is "i" this  less than 115 so it will add to list and again after "I" the word is "am" so len of list is 1 and len of words is 2 and +1 is total 3 so 1 +3=4 which is less than 115 so we will add "am" to the list
            else:
                f.write(
                    list.rstrip() + "\n"
                )  # If the character exceedes 115 then this will write everything in list and move to next line
                line = (
                    words + " "
                )  # this will create a new list and add the remaining words + space and the loops continues
        if list:
            f.write(
                line.rstrip() + "\n"
            )  # after loops finishes the list from else part is not written so if there is something in that list  this will write that and moves to the next line


def read():
    with open(file_path, "r") as f:
        print("Your Journal :")
        data = f.read()
        print(data)


def search(word):
    with open(file_path, "r") as f:
        count = 0
        found = []

        for line_number, data in enumerate(f, start=1):
            finder = []
            if word.lower() in data.lower():
                count += 1
                finder.append("Word found")
                found.append(line_number)

        if count == 0:
            print("Word not found")
        else:
            print(finder[0])
            for finds in found:
                print("Word found on line  number :", finds)
            print("Occurrence of word :", count)


def clean():
    print("""    Are you sure you want to delete the journal? 
    Type Yes for conformation or No for going back""")
    try:
        decision = input("Enter  your final decision : ")
        decision = decision.lower()
        if decision not in ("yes", "no"):
            raise ValueError("Enter only yes or no...!")
        if decision == "yes":
            with open(file_path, "r") as f:
                f.truncate(0)
        else:
            print("Thank god you are not deleting your journal buddy..!")
    except ValueError as e:
        print(e)


def analyze():
    with open(file_path, "r") as f:
        data = f.read()
        word = data.split()
    print("Total words :", len(word))
    print("Longest word :", max(word, key=lambda x: len(x)))
    print("Shortest word :", min(word, key=lambda x: len(x)))


while True:
    print("""     ===== MY JOURNAL =====

        1. Write a new entry
        2. Read journal
        3. Search journal
        4. Analyze journal
        5. Clear journal
        6. Exit""")
    try:
        x = int(input("\nEnter number :"))
        match x:
            case 1:
                write(new=input("Enter today's entry :"))
            case 2:
                read()
            case 3:
                search(word=input("Enter word you want to search :"))
            case 4:
                analyze()
            case 5:
                clean()
            case 6:
                break
            case _ if x > 6 or x < 1:
                raise ValueError("You entered wrong number.")

    except ValueError as e:
        print(e)
    finally:
        print("Thank you for  using Personal Journal and text analyzer....!")
