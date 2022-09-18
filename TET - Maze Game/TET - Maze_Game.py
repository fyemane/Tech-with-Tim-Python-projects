#https://www.youtube.com/playlist?list=PLlEgNdBJEO-lNDJgg90fmfAq9RzORkQWP
# TokyoEdTech
"""
600x600 screen area
24x24 sprites
25x25 grid

topleft block = -288, 288
topright block = 288, 288
bottomleft block = -288, -288
bottomright block = 288, -288
"""
from classes import *

# setup turtle screen
wn = turtle.Screen()
# screen bg color
wn.bgcolor("black")
# title
wn.title("A Maze Game")
# setup dimensions
wn.setup(700,700)
# turn off screen updates
wn.tracer(0)

# create levels list
# 25x25
levels = [""]
# define first level
level_1 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
           "XP XXXXXXXE         XXXXX",
           "X  XXXXXXX  XXXXXX  XXXXX",
           "X       XX  XXXXXX  XXXXX",
           "X       XX  XXXXXX  XXXXX",
           "XXXXXX  XX  XXX       EXX",
           "XXXXXX  XX  XXX        XX",
           "XXXXXX  XX    XXXX  XXXXX",
           "X  XXX        XXXX  XXXXX",
           "X  XXX  XXXXXXXXXXT XXXXX",
           "X         XXXXXXXXXXXXXXX",
           "X                XXXXXXXX",
           "XXXXXXXXXXXX     XXXXX  X",
           "XXXXXXXXXXXXXXX  XXXXX  X",
           "XXX  XXXXXXXXXXX        X",
           "XXXE                    X",
           "XXX          XXXXXXXXXXXX",
           "XXXXXXXXXXX  XXXXXXXXXXXX",
           "XX   XXXXXX             X",
           "XX   XXXXXX             X",
           "XX    XXXXXXXXXXXX  XXXXX",
           "XX         XXXXX    XXXXX",
           "XXXXE                   X",
           "XXXXXXXXXXXXXXXXXXXXXXXXX"]
# add maze to mazes list
levels.append(level_1)

# create level setup function
def setup_maze(level):
    # how many rows
    for y in range (len(level)):
        # how many columns
        for x in range(len(level[y])):
            # get the character at each x,y coordinate
            # NOTE the order of y and x in the next line
            character = level[y][x]
            # calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            # check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                # Stamp a copy of the turtle shape onto the canvas
                pen.stamp()
                # add coordinates to wall list, tuple
                walls.append((screen_x, screen_y))
            # check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)
            # check if it is a T (representing Treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
            # check if it is a E (representing Enemy)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

# add a treasures list
treasures = []
# add enemies list
enemies = []

# create objects
pen = Pen()

# set up the level
setup_maze(levels[1])

# keyboard binding
turtle.listen()
turtle.onkeypress(player.go_left, "a")
turtle.onkeypress(player.go_right, "d")
turtle.onkeypress(player.go_up, "w")
turtle.onkeypress(player.go_down, "s")

# start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move(), t=250)

# main game loop
while True:
    # check for player-treasure collision
    # iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            # add the treasure gold to player gold
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            # destroy the treasure
            treasure.destroy()
            # remove treasure from treasures list
            treasures.remove(treasure)

    # iterate through enemy list to see if player collides
    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player dies!")

    # update screen
    wn.update()
