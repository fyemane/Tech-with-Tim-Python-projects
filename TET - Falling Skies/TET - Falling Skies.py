#https://www.youtube.com/playlist?list=PLlEgNdBJEO-kqEqgLXTVLloAFemDusfPK
# with @TokyoEdTech
import turtle, random, os, winsound, time

score = 0
lives = 3

# sound
sound_deer_cry = "deer_cry.wav"
sound_power_up = "power_up.wav"

wn = turtle.Screen()
wn.title("Falling Skies")
wn.bgcolor("green")
wn.bgpic("forest.gif")
wn.setup(width=800, height=600)
# shuts off all screen updates
wn.tracer(0)

# draw border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-400, -300)
border.pendown()
# 3 pixels wide
border.pensize(3)
# draw a square
for side in range(2):
    border.forward(800)
    border.left(90)
    border.forward(600)
    border.left(90)
border.hideturtle()

# register shapes
wn.register_shape("deer_left.gif")
wn.register_shape("deer_right.gif")
wn.register_shape("acorn.gif")
wn.register_shape("hunter_left.gif")
wn.register_shape("hunter_right.gif")

# add the player
player = turtle.Turtle()
# turtle animation speed
player.speed(0)
player.shape("deer_right.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# create a list of good guys
good_guys = []

# add the good guys
for index in range(20):
    good_guy = turtle.Turtle()
    # turtle animation speed
    good_guy.speed(0)
    good_guy.shape("acorn.gif")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(random.randint(-390, 390), random.randint(300, 450))
    good_guy.speed = random.randint(1, 4)
    good_guys.append(good_guy)

# create a list of bad guys
bad_guys = []

# add the bad guys
for index in range(20):
    bad_guy = turtle.Turtle()
    # turtle animation speed
    bad_guy.speed(0)
    bad_guy.shape("hunter_right.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(random.randint(-390, 390), random.randint(300, 450))
    bad_guy.speed = random.randint(1, 4)
    bad_guys.append(bad_guy)

# make the pen
pen = turtle.Turtle()
# turtle animation speed
pen.speed(0)
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0, 260)
pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

# function
def go_left():
    player.direction = "left"
    player.shape("deer_left.gif")


def go_right():
    player.direction = "right"
    player.shape("deer_right.gif")


def move():
    if player.direction == "left":
        player.setx(player.xcor() - 5)
    elif player.direction == "right":
        player.setx(player.xcor() + 5)


# keyboard binding
wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# main game loop
while True:
    # update screen
    wn.update()

    # move the player
    move()

    # boundary checking for player
    if player.xcor() > 380:
        player.setx(380)
    if player.xcor() < -390:
        player.setx(-390)

    for good_guy in good_guys:
        # move the good guy
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)

        # boundary checking for good guys
        if y < -300:
            x = random.randint(-390, 390)
            y = random.randint(300, 350)
            good_guy.goto(x, y)

        # player collides with good guys
        if player.distance(good_guy) < 40:
            winsound.PlaySound(sound_power_up, winsound.SND_ASYNC)
            x = random.randint(-390, 390)
            y = random.randint(300, 350)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    for bad_guy in bad_guys:
        # move the bad guys
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)

        # boundary checking for bad guys
        if y < -300:
            x = random.randint(-390, 390)
            y = random.randint(300, 350)
            bad_guy.goto(x, y)

        # player collides with bad guys
        if player.distance(bad_guy) < 30:
            winsound.PlaySound(sound_deer_cry, winsound.SND_FILENAME)
            x = random.randint(-390, 390)
            y = random.randint(300, 350)
            bad_guy.goto(x, y)
            lives -= 1
            pen.clear()
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    if lives == 0:
        pen.clear()
        pen.color("red")
        pen.write("GAME OVER".format(score, lives), align="center", font=("Courier", 24, "normal"))
        wn.exitonclick()
        os._exit(1)

    time.sleep(0.01)


# best high score = 510
