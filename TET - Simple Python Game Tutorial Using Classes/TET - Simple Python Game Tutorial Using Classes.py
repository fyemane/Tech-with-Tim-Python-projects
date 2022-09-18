# https://www.youtube.com/playlist?list=PLlEgNdBJEO-lwI_F15DAQmgmqh5E7OYt_
# by @TokyoEdTech
import time
from classes import *

# setup screen
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("Simple Python Turtle Graphics Game (Class Version) by @TokyoEdTech")
wn.bgpic("kbgame-bg.gif")
wn.register_shape(heart)

# class instances
player = Player()
border = Border()
game = Game()

# draw the border
border.draw_border()

# create multiple goals
goals = []
for count in range(6):
    goals.append(Goal())

# set keyboard bindings
# tells turtle model to detect keyboard input
# using WASD keys
turtle.listen()
turtle.onkey(player.turnleft, "a")
turtle.onkey(player.turnright, "d")
turtle.onkey(player.increasespeed, "w")
turtle.onkey(player.decreasespeed, "s")

# stop program from updating, speeds up program
wn.tracer(0)

# main loop
while True:
    # calculates everything then draws
    wn.update()
    player.move()

    for goal in goals:
        goal.move()
    
        # check for collision between player and goal
        if isCollision(player, goal):
            goal.jump()
            game.change_score(10)
            game.play_sound("explosion.wav")
