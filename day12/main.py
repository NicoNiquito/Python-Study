#Number Guessing Game Objectives:

# Include an ASCII art logo. OK
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).  OK

import art
import random

print(art.logo)

print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')
difficulty = input('Choose a difficulty. Type "easy" or "hard": ')

lives = 0
if difficulty == 'easy':
    lives += 10
    print(f'You have {lives} attempts remaining to guess the number.')
elif difficulty == 'hard':
    lives += 5
    print(f'You have {lives} attempts remaining to guess the number.')
    
random_number = random.randint(1, 100) # pega um número aleatório entre 1 e 100
#print(random_number)



game_over = False

while not game_over:



    user_choice = int(input('Make a guess: '))

    if user_choice == random_number:
        print(f'Correct! The answer was {user_choice}')
        game_over = True
    
    elif user_choice > random_number:
        lives -= 1
        if lives > 0:
            print('Too high.\nGuess again.')
            print(f'You have {lives} attempts remaining to guess the number')
        else:
            print('Too high.')        
        
   
    elif user_choice < random_number:
        lives -= 1
        if lives > 0:
            print('Too low.\nGuess again.')
            print(f'You have {lives} attempts remaining to guess the number')
        else:
            print('Too low.')      
        
    if lives == 0:
        game_over = True
        print(f'You ran out of lives. The correct answer was {random_number}.')
