name = input("Enter your name :")
name = name.lower()
if not name.isalpha():
    raise ValueError("Please enter a valid name ")

print(f"Are you ready for quiz {name} ?\n     Lets Goooo...!")
easyques = [
    "1. What is the capital city of France?",
    "2. How many continents are there on Earth?",
    "3. What is the largest ocean on Earth?",
]
medques = [
    "1. Which is the largest planet in our Solar System?",
    "2. What is the chemical symbol for gold?",
    "3. Who wrote Romeo and Juliet?",
]
hardques = [
    "1. Which element has the atomic number 26?",
    "2. What is the deepest point in Earth's oceans called?",
    "3. Which scientist formulated the three laws of motion?",
]
esopt = ["A. Rome", "B. Paris", "C. Madrid", "D. Berlin"]
esopt1 = ["A. 5", "B. 6", "C. 7", "D. 8"]
esopt2 = ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"]
mdopt = ["A. Earth", "B. Saturn", "C. Jupiter", "D. Neptune"]
mdopt1 = ["A. Ag", "B. Fe", "C. Au", "D. Go"]
mdopt2 = [
    "A. Charles Dickens",
    "B. William Shakespeare",
    "C. Mark Twain",
    "D. Jane Austen",
]
hdopt = ["A. Copper", "B. Iron", "C. Zinc", "D. Nickel"]
hdopt1 = [
    "A. Mariana Trench",
    "B. Tonga Trench",
    "C. Java Trench",
    "D. Puerto Rico Trench",
]
hdopt2 = [
    "A. Albert Einstein",
    "B. Galileo Galilei",
    "C. Isaac Newton",
    "D. Nikola Tesla",
]
esans = ["B", "C", "C"]
mdans = ["C", "C", "B"]
hdans = ["B", "A", "C"]
score = []
score1 = []
score2 = []
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
                    a = input("Enter your option A to D:")
                    score.append(a.upper())
                    if esans[0].lower() == str(a).lower():
                        count += 1
                elif i == 1:
                    for i in esopt1:
                        print(i, end="\n")
                    a = input("Enter your option A to D:")
                    score.append(a.upper())
                    if esans[1].lower() == str(a).lower():
                        count += 1
                else:
                    for i in esopt2:
                        print(i, end="\n")
                    a = input("Enter your option A to D:")
                    score.append(a.upper())
                    if esans[2].lower() == str(a).lower():
                        count += 1

            print("Your score is :", count)
            print("Your answers are :", score)
            print("Correct ansers are :", esans)
        case 2:
            for i in range(len(medques)):
                print(medques[i])
                if i == 0:
                    for i in mdopt:
                        print(i, end="\n")
                    a = input("Enter your option A to D:")
                    score1.append(a.upper())
                    if mdans[0].lower() == str(a).lower():
                        count += 1
                elif i == 1:
                    for i in mdopt1:
                        print(i, end="\n")
                    a = input("Enter your option A to D:")
                    score1.append(a.upper())
                    if mdans[1].lower() == str(a).lower():
                        count += 1
                else:
                    for i in mdopt2:
                        print(i, end="\n")
                    a = input("Enter your option A to D:")
                    score1.append(a.upper())
                    if mdans[2].lower() == str(a).lower():
                        count += 1
            print("Your score is :", count)
            print("Your answers are :", score1)
            print("Correct ansers are :", mdans)
        case 3:
            for i in range(len(hardques)):
                print(hardques[i])
                if i == 0:
                    for i in hdopt:
                        print(i, end="\n")
                    a = input("Enter your option A to D:")
                    score2.append(a.upper())
                    if hdans[0].lower() == str(a).lower():
                        count += 1
                elif i == 1:
                    for i in hdopt1:
                        print(i, end="\n")
                    a = input("Enter your option A to D:")
                    score2.append(a.upper())
                    if hdans[1].lower() == str(a).lower():
                        count += 1
                else:
                    for i in hdopt2:
                        print(i, end="\n")
                    a = input("Enter your option A to D:")
                    score2.append(a.upper())
                    if hdans[2].lower() == str(a).lower():
                        count += 1

            print("Your score is :", count)
            print("Your answers are :", score2)
            print("Correct ansers are :", hdans)

except ValueError as e:
    print(e)
finally:
    print("Thanks for playing...!!")
