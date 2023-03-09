# Coffee Machine 

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

balance = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def ingredients_ok(ingredients):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f'Sorry, we ran out of {i} :(')
            return False
    return True


def insert_coins():
    print('Insert your coins.')
    total = 0
    total += int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.10
    total += int(input('How many nickels?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total


def transition_ok(inserted_money, price):
    if inserted_money >= price:
        troco = round(inserted_money - price, 2)
        print(f'Here is ${troco} in change.')
        global balance
        balance += price
        return True
    else:
        print('Sorry, that\'s not enough money.')
        return False


def prepare_drink(drink_name, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f'Here is your {drink_name}. Enjoy!')


power_on = True

while power_on:
    drink = input('What do you want? (espresso/latte/cappuccino): ')
    if drink == 'off':
        power_on = False
    elif drink == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Balance: {balance}$')
    else:
        product = MENU[drink]   # usa da escolha do usuário pra procurar no dictionary
        if ingredients_ok(product['ingredients']):
            payment = insert_coins()
            if transition_ok(payment, product['cost']):
                prepare_drink(drink, product['ingredients'])
