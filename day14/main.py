# Higher or Lower Game objectives:
 
# show the ASCIIS 
# select a random A and B value from game_data
# print A and B
# ask for which of them has more followers
# if the answer is right + 1 point, if wrong end game and show score
# if right then B = A and select a new B
# clear console and print all again


from art import logo, vs
from game_data import data
import random
#from replit import clear

#clear()
#print(logo)

a = random.choice(data)
print(a)

b = random.choice(data)
print(b)

while a == b:
  b = random.choice(data)
print(b)

def resume_a():
  name = a['name']
  description = a['description']
  country = a['country']
  return f'Compare A: {name}, a {description}, from {country}.'

def resume_b():
  name = b['name']
  description = b['description']
  country = b['country']
  return f'Against B: {name}, a {description}, from {country}.'

guess = input('Who has more followers? Type \'A\' or \'B\': ').lower()

def compare():
    if int(a['follower_count']) > int(b['follower_count']):
        return 'a' 
    else:
       return 'b'

score = 0

if compare() == guess:
   score += 1
   #clear()
   print(logo)
   print(f'You\'re right! Current score: {score}.')
else:
   game_over = True


def game():
   print(logo)
   score = 0
   while not game_over:
    a = random.choice(data)
    b = random.choice(data)
    
    while a == b:
        b = random.choice(data)

    def resume_a():
        name = a['name']
        description = a['description']
        country = a['country']
        return f'Compare A: {name}, a {description}, from {country}.'
    
    def resume_b():
        name = b['name']
        description = b['description']
        country = b['country']
        return f'Against B: {name}, a {description}, from {country}.'
    
    print(resume_a())
    print(vs)
    print(resume_b())
    
    guess = input('Who has more followers? Type \'A\' or \'B\': ').lower()

    def compare():
        if int(a['follower_count']) > int(b['follower_count']):
            return 'a' 
        else:
            return 'b'
        
    if compare() == guess:
        score += 1
        #clear()
        game()
        

    else:
        game_over = True