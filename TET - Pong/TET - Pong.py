#https://www.youtube.com/playlist?list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2
# by @TokyoEdTech
import turtle, time, os, winsound

# creates wn
wn = turtle.Screen()
wn.title("Pong")
# changes background color
wn.bgcolor("black")
wn.setup(width=800, height=600)
# stops wn from updating, speeds up program
wn.tracer(0)

bounce = "pong_bounce.wav"

# score
score_a = 0
score_b = 0

# Paddle A, turtle obj
paddle_a = turtle.Turtle()
# speed of animation, max speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# don't draw lines
paddle_a.penup()
# where Paddle A is at beginning of program
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("white")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 3
ball1.dy = -3

# Ball2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("blue")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -2
ball2.dy = -2

# Ball3
ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("square")
ball3.color("red")
ball3.penup()
ball3.goto(0, 0)
ball3.dx = 1
ball3.dy = -1

# Ball4
ball4 = turtle.Turtle()
ball4.speed(0)
ball4.shape("square")
ball4.color("green")
ball4.penup()
ball4.goto(0, 0)
ball4.dx = -.5
ball4.dy = -.5

balls = [ball1, ball2, ball3, ball4]

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
# don't want to draw line when pen moves
pen.penup()
# hide the object
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# exit box
game_over = turtle.Turtle()
game_over.speed(0)
game_over.shape("square")
game_over.color("white")
game_over.fillcolor("black")
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)

# function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    # set y to new y-cor
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)

# keyboard binding
# listen for keyboard input
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    # every time loop runs, updates screen
    wn.update()

    for ball in balls:

        # move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy = -ball.dy
            winsound.PlaySound(bounce, winsound.SND_ASYNC)

        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy = -ball.dy
            winsound.PlaySound(bounce, winsound.SND_ASYNC)

        if ball.xcor() > 380:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # paddle and ball collisions
        if 350 > ball.xcor() > 330 and paddle_b.ycor() + 55 > ball.ycor() > paddle_b.ycor() - 55:
            ball.setx(330)
            ball.dx *= -1
            winsound.PlaySound(bounce, winsound.SND_ASYNC)

        if -350 < ball.xcor() < -330 and paddle_a.ycor() + 55 > ball.ycor() > paddle_a.ycor() - 55:
            ball.setx(-330)
            ball.dx *= -1
            winsound.PlaySound(bounce, winsound.SND_ASYNC)

    ## AI Player
    # assume closest ball is first ball in list
    closest_ball = balls[0]
    for ball in balls:
        if ball.xcor() > closest_ball.xcor():
            closest_ball = ball

    # is paddle b's y car less then ball y cor and difference is les than 10
    if paddle_b.ycor() < closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 50:
        paddle_b_up()
    elif paddle_b.ycor() > closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 50:
        paddle_b_down()

    # when a player wins
    if score_a == 3:
        pen.clear()
        pen.write("Player A has won!", align="center", font=("Courier", 24, "normal"))
        game_over.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
        wn.exitonclick()
        os._exit(1)

    elif score_b == 3:
        pen.clear()
        pen.write("Player B has won!", align="center", font=("Courier", 24, "normal"))
        game_over.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
        wn.exitonclick()
        os._exit(1)
        
    time.sleep(0.001)
