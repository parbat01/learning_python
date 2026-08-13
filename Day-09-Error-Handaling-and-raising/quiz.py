name = input("Enter your name :")
name = name.lower()
if not name.isalpha():
    raise ValueError("Please enter a valid name ")

print(f"Are you ready for quiz {name} ?\n     Lets Goooo...!")
easyques = ["What is 2+2?", "What is 6+4?"]
medques = ["What is 4x9?", "What is 5x6?"]
esopt = ["2", "4", "9", "10"]
esopt1 = ["11", "10", "23", "56"]
mdopt = ["2", "36", "9", "10"]
mdopt1 = ["11", "30", "23", "56"]
esans = ["4", "10"]
mdans = ["36", "30"]
hdans = ["tanx", "cosx"]
hdopt = ["cosecx", "cotx", "tanx", "secx"]
hdopt1 = ["0", "tanx", "cosx", "secx"]
hardques = ["What is sinx/cosx?", "What is derivative of sinx?"]
print("""Choose difficulty of a quiz :
         1.Easy
         2.Medium
         3.Hard""")
count = 0

try:
    x = int(input("Enter number of a difficulty :"))
    if not 1 <= x <= 3:
        raise ValueError("Difficulty must be between 1 and 3")
    match x:
        case 1:
            for i in range(len(easyques)):
                print(easyques[i])
                if i == 0:
                    for i in esopt:
                        print(i, end="\n")
                    a = input("Enter your option :")
                    if esans[0] == str(a):
                        count += 1
                else:
                    for i in esopt1:
                        print(i, end="\n")
                    a = input("Enter your option :")
                    if esans[1] == str(a):
                        count += 1

            print("Your score is :", count)
            print("Correct ansers are :", esans)
        case 2:
            for i in range(len(medques)):
                print(medques[i])
                if i == 0:
                    for i in mdopt:
                        print(i, end="\n")
                    a = input("Enter your option :")
                    if mdans[0] == str(a):
                        count += 1
                else:
                    for i in mdopt1:
                        print(i, end="\n")
                    a = input("Enter your option :").lower()
                    if mdans[1] == str(a):
                        count += 1
                print("Your score is :", count)
                print("Correct ansers are :", mdans)
        case 3:
            for i in range(len(hardques)):
                print(hardques[i])
                if i == 0:
                    for i in hdopt:
                        print(i, end="\n")
                    a = input("Enter your option :").lower()
                    if hdans[0].lower() == str(a):
                        count += 1
                else:
                    for i in hdopt1:
                        print(i, end="\n")
                    a = input("Enter your option :").lower()
                    if hdans[1].lower() == str(a):
                        count += 1

                print("Your score is :", count)
                print("Correct ansers are :", hdans)

except ValueError as e:
    print(e)
finally:
    print("Thanks for playing...!!")
