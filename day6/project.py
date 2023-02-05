# Today the exercises and the project were on a site called Reeborg's World (https://reeborg.ca/index_en.html). I've passed trough the following "phases" today:
# Hurdle 1
# Hurdle 2
# Hurdle 3
# Hurdle 4
# Maze

# This is the code I developed for the maze (the funniest phase):


def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif right_is_clear() != True and front_is_clear():
        move()
    elif right_is_clear() != True and front_is_clear() != True:
        turn_left()

#PS: sometimes it gets an infinite loop on a certain spot and I will come back to resolve it when I learn how to debugg