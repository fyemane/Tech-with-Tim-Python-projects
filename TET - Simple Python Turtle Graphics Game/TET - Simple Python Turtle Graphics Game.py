#https://www.youtube.com/playlist?list=PLlEgNdBJEO-n8FdWb-7f_C4dFC07IY9tb
# with @TokyoEdTech
import turtle, random, os, winsound, time

end_the_game = False
# set up screen
wn = turtle.Screen()
wn.title("Asteroids")
wn.bgcolor("white")
wn.bgpic("space_background.gif")
# drops frames
wn.tracer(0)

# draw pen
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# create player turtle
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
# no trail
player.penup()
player.speed(0)

# create the score
score = 0

# create asteroid
asteroids = []
num_of_asteroids = 10
for count in range(num_of_asteroids):
    asteroids.append(turtle.Turtle())
for asteroid in asteroids:
    asteroid.color("red")
    asteroid.shape("circle")
    asteroid.penup()
    asteroid.speed(0)
    asteroid.setposition(random.randint(-290, 290), random.randint(-290, 290))

# set speed variable
speed = 1

# define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 1

def decrease_speed():
    global speed
    speed -= 1

def endgame():
    global end_the_game
    end_the_game = True

# set keyboard bindings
wn.listen()
wn.onkeypress(turn_left, "a")
wn.onkeypress(turn_right, "d")
wn.onkeypress(increase_speed, "w")
wn.onkeypress(decrease_speed, "s")
wn.onkeypress(endgame, "e")

#sound
frequency = 23000
duration = 200

# main game loop
while True:
    wn.update()
    player.forward(speed)

    # boundary checking for player
    if player.xcor() > 290 or player.xcor() < -290 or player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        winsound.Beep(frequency, duration)

    for asteroid in asteroids:
        # move the asteroid
        asteroid.forward(3)
        asteroid.right(random.randint(0, 1))

        # player collides with enemy
        if player.distance(asteroid) < 20:
            asteroid.setposition(random.randint(-290, 290), random.randint(-290, 290))
            asteroid.right(random.randint(165, 195))
            score += 1
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)

            # draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 300)
            score_string = "Score: %s" % score
            mypen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

        # boundary checking for asteroids
        if asteroid.xcor() > 290 or asteroid.xcor() < -290 or asteroid.ycor() > 290 or asteroid.ycor() < -290:
            asteroid.right(random.randint(165, 195))
            # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if end_the_game:
        wn.exitonclick()

    time.sleep(0.01)

delay = raw_input("press enter to finish.")