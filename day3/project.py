print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

quest1 = input('You are at a cross road. Where do you want to go? Type "left" or "right". ').lower()
if quest1 == 'left':
    quest2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or type "swim" to swim across. ').lower()
    if quest2 == 'wait':
        quest3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ').lower()
        if quest3 == 'yellow':
            print('You found the treasure! You won!')
        elif quest3 == 'blue':
            print('You enter a room of beasts. Game over')
        elif quest3 == 'red':
            print('It is a room full of fire. Game over.')
    elif quest2 == 'swim':
        print('You get attacked by an angry trout. Game over.')
elif quest1 == 'right':
    print('You fell into a hole. Game over.')
