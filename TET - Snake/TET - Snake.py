# by @TokyoEdTech
# https://www.youtube.com/playlist?list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ
import turtle, time, random, os
from color import *
# best high score = 1100

delay = 0.1
is_paused = False
exit_game = False

# score
score = 0
high_score = 0

# set up screen
wn = turtle.Screen()
canvas = wn.getcanvas()
root = canvas.winfo_toplevel()

wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
# turns off animation/screen updates
wn.tracer(0)

# color theme
theme = "blue"

# snake head
head = turtle.Turtle()
# fastest animation speed
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
# in the middle
head.direction = "still"
head.destination = (0,0)

# snake food
food = turtle.Turtle()
# fastest animation speed
food.speed(0)
food.shape("circle")
food_color = random_color(theme)
food.color(food_color)
food.penup()
food.goto(0, 100)

# list of segments
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))

# change direction
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

# functions
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)
    """
    # smoother instead of blocky animation
    # move towards destination
    destination_x = head.destination[0]
    destination_y = head.destination[1]

    if head.xcor() < destination_x:
        head.setx(head.xcor() + 1)
    elif head.xcor() > destination_x:
        head.setx(head.xcor() - 1)
    elif head.ycor() < destination_y:
        head.sety(head.ycor() + 1)
    elif head.ycor() > destination_y:
        head.sety(head.ycor() - 1)
    else:
        # we are same spot at destination, recalc based on last key pressed
        if head.direction == "up":
            destination_y += 20
        elif head.direction == "down":
            destination_y -= 20
        elif head.direction == "left":
            destination_x -= 20
        elif head.direction == "right":
            destination_x += 20

        head.destination = (destination_x, destination_y)
    """


def redo_game():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    global segment, delay, score
    # hide the segments
    for segment in segments:
        # clear turtle’s drawings, re-center turtle, and reset vars
        segment.reset()
        segment.hideturtle()
    # clear the segments list
    segments.clear()

    # reset the delay
    delay = 0.1

    # reset the score
    score = 0
    # update the score display
    pen.clear()
    pen.write("Score: {}    High Score: {}".format(score, high_score), 
              align="center",vfont=("Courier", 24, "normal"))

def pause_game():
    global is_paused
    if is_paused:
        is_paused = False
    else:
        is_paused = True

def endgame():
    global exit_game
    exit_game = True

# keyboard bindings
#key_choice = input("Arrow keys or WASD keys?\n")
#if key_choice.lower() == "arrow" or key_choice.lower() == "a":
#    wn.listen()
#    wn.onkeypress(go_up, "Up")
#    wn.onkeypress(go_down, "Down")
#    wn.onkeypress(go_left, "Left")
#    wn.onkeypress(go_right, "Right")
#elif key_choice.lower() == "wasd" or key_choice.lower() == "w":
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
#else:
#    print("Invalid response")
#    os._exit(0)

print("Press Q to pause the game for 5 seconds.")
print("Press E to end the game.")
wn.onkeypress(pause_game, "q")
wn.onkeypress(endgame, "e")

# main game loop
while True:
    # update the window
    wn.update()

    # snake exits screen at border collision and enters at opposite side
    if head.xcor() > 290:
        head.setx(-280)
    if head.xcor() < -280:
        head.setx(280)
    if head.ycor() > 290:
        head.sety(-280)
    if head.ycor() < -290:
        head.sety(280)

    # check for collision with food
    if head.distance(food) < 20:
        # move the food to random spot that aligns like grid
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        next_food_color = random_color(theme)
        food.color(random_color(theme))
        # wn.bgcolor(random_color())
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(random_color(theme))
        new_segment.penup()
        # append the new segment to list of segments
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.0001

        # increase the score
        score += 10
        if score > high_score:
            high_score = score

        # update the score display
        pen.clear()
        pen.hideturtle()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    # move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            redo_game()

    # check if player paused game
    if is_paused:
        time.sleep(5)
        is_paused = False

    # check if player ended game
    if exit_game:
        break

    # stop updating by [delay] seconds
    time.sleep(delay)
