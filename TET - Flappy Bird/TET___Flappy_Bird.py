#https://www.youtube.com/watch?v=zaD6TsM6Pj8&list=PLlEgNdBJEO-keECn0rTUTM7Be7PWUr2F-&index=7 
# @TokyoEdTech
import turtle, time

# make window
wn = turtle.Screen()
wn.title("Flappy Bird by @TokyoEdTech")
wn.bgcolor("blue")
wn.bgpic("background.gif")
wn.setup(500, 800)
wn.tracer(0)

# register shape
wn.register_shape("bird.gif")

pen = turtle.Turtle()
pen.speed(0)
pen.ht()
pen.penup()
pen.color("white")
pen.goto(0, 250)
pen.write("0", move=False, align="left", font=("Arial", 32, "normal"))

player = turtle.Turtle()
# animation speed
player.speed(0)
player.penup ()
player.color("yellow")
player.shape("bird.gif")
# resize
player.goto(-200, 0)
# change in x,y
player.dx = 0
player.dy = 0.5


pipe1_top = turtle.Turtle()
# animation speed
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("green")
pipe1_top.shape("square")
# resize
pipe1_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_top.goto(300, 250)
# change in x,y
pipe1_top.dx = -2
pipe1_top.dy = 0
pipe1_top.value = 1

pipe1_bottom = turtle.Turtle()
# animation speed
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("green")
pipe1_bottom.shape("square")
# resize
pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_bottom.goto(300, -250)
# change in x,y
pipe1_bottom.dx = -2
pipe1_bottom.dy = 0


pipe2_top = turtle.Turtle()
# pipe 2
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color("green")
pipe2_top.shape("square")
# resize
pipe2_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_top.goto(600, 280)
# change in x,y
pipe2_top.dx = -2
pipe2_top.dy = 0
pipe2_top.value = 1

pipe2_bottom = turtle.Turtle()
# animation speed
pipe2_bottom.speed(0)
pipe2_bottom.penup()
pipe2_bottom.color("green")
pipe2_bottom.shape("square")
# resize
pipe2_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_bottom.goto(600, -220)
# change in x,y
pipe2_bottom.dx = -2
pipe2_bottom.dy = 0


pipe3_top = turtle.Turtle()
# pipe 2
pipe2_top.speed(0)
pipe3_top.penup()
pipe3_top.color("green")
pipe3_top.shape("square")
# resize
pipe3_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe3_top.goto(900, 320)
# change in x,y
pipe3_top.dx = -2
pipe3_top.dy = 0
pipe3_top.value = 1

pipe3_bottom = turtle.Turtle()
# animation speed
pipe3_bottom.speed(0)
pipe3_bottom.penup()
pipe3_bottom.color("green")
pipe3_bottom.shape("square")
# resize
pipe3_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe3_bottom.goto(900, -180)
# change in x,y
pipe3_bottom.dx = -2
pipe3_bottom.dy = 0

# define function
def go_up():
    max_vel = 8
    player.dy += max_vel
    if player.dy > max_vel:
        player.dy = max_vel

# keyboard binding
wn.listen()
wn.onkeypress(go_up, "space")

pipes = [(pipe1_top, pipe1_bottom), (pipe2_top, pipe2_bottom), (pipe3_top, pipe3_bottom)]
gravity = -0.2

# initialize scoring
player.score = 0
print("Score: {}".format(player.score))

# main game loop
while True:
    # pause
    time.sleep(0.01)
    # update the screen
    wn.update()

    # add gravity
    player.dy += gravity

    # move player
    y = player.ycor()
    y += player.dy
    player.sety(y)

    # bottom border
    if player.ycor() < -390:
        player.dy = 0
        player.sety(390)

    for pipe_pair in pipes:
        pipe_top = pipe_pair[0]
        pipe_bottom = pipe_pair[1]

        # move pipe 1
        x = pipe_top.xcor()
        x += pipe_top.dx
        pipe_top.setx(x)

        x = pipe_bottom.xcor()
        x += pipe_bottom.dx
        pipe_bottom.setx(x)

        # move pipes to start
        if pipe_top.xcor() < -350:
            pipe_top.setx(600)
            pipe_bottom.setx(600)
            pipe_top.value = 1

        # check for collisions with pipes
        # pipe 1
        if (player.xcor() + 10 > pipe_top.xcor() - 30) and \
           (player.xcor() - 10 < pipe_top.xcor() + 30):
            if (player.ycor() + 10 > pipe_top.ycor() - 180) or \
               (player.ycor() - 10 < pipe_bottom.ycor() + 180):
                pen.clear()
                pen.write("Game Over", move=False, align="center", font=("Arial", 16, "normal"))
                wn.update()
                time.sleep(3)
                # reset score
                player.score = 0
                # move pipes back
                pipe_top.setx(450)
                pipe_bottom.setx(450)
                # move player back
                player.goto(-200, 0)
                player.dy = 0
                # reset the pen
                pen.clear()
                pen.write("0", move=False, align="center", font=("Arial", 16, "normal"))
                

        # check for score
        if pipe_top.xcor() + 30 < player.xcor() - 10:
            player.score += pipe_top.value
            pipe_top.value = 0
            pen.clear()
            pen.write(player.score, move=False, align="left", font=("Arial", 32, "normal"))

