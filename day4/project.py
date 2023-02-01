rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choose = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n' ))

if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)

print('Computer chose:')

random = random.randint(0, 2)
if random == 0:
    print(rock)
elif random == 1:
    print(paper)
elif random == 2:
    print(scissors)

if choose == 0 and random == 0:
    print('It\'s a draw')
elif choose == 1 and random == 1:
    print('It\'s a draw')
elif choose == 2 and random == 2:
    print('It\'s a draw')
elif choose == 0 and random == 1:
    print('You Lose')
elif choose == 1 and random == 2:
    print('You Lose')
elif choose == 2 and random == 0:
    print('You Lose')
elif choose == 0 and random == 2:
    print('You Win!')
elif choose == 1 and random == 0:
    print('You Win!')
elif choose == 2 and random == 1:
    print('You Win!')


#You win!
#Its a draw
#You lose



