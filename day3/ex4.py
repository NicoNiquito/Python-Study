# Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_lower = name1.lower() + name2.lower()
name_true = name_lower.count('t') + name_lower.count('r') + name_lower.count('u') + name_lower.count('e')
name_love = name_lower.count('l') + name_lower.count('o') + name_lower.count('v') + name_lower.count('e')

love_score = str(name_true) + str(name_love)

if int(love_score) < 10 or int(love_score) > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')
