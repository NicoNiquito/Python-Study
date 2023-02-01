# Banker roulette

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_itens = len(names)
random_choice = random.randint(0, num_itens - 1)
chosen_one = names[random_choice]
print(f'{chosen_one} is going to buy the meal today!')