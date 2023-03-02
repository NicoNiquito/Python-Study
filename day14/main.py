# Higher or Lower Game
 
from art import logo, vs
from game_data import data
import random
#from replit import clear

def resume(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}.'

def comparison(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
print(logo)

game_over = False

b= random.choice(data)

while not game_over:
    a = b
    b = random.choice(data)

    while b == a:
        b = random.choice(data)


    print(f'Compare A: {resume(a)}')
    print(vs)
    print(f'Against B : {resume(b)}')


    guess = input('Who was more followers? Type \'A\' or \'B\': ').lower()

    a_followers = a['follower_count']
    b_followers = b['follower_count']

    right_answer = comparison(guess, a_followers, b_followers)

    #clear()
    #print(logo)

    if right_answer:
        score += 1
        
        print(f'You\'re right!    Current score: {score}')
    else:
        game_over = True
        print(f'Nope, that\'s wrong. Final score: {score}')
        