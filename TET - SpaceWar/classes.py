import turtle, random, winsound, time

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        # construct parent class
        turtle.Turtle.__init__(self, shape = spriteshape)
        # animation speed method
        self.speed(0)
        self.penup()
        self.color(color)
        # check if on screen
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)
        # boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60) 
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    # collision detection
    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        # construct parent class
        Sprite.__init__(self, spriteshape, color, startx, starty)
        # stretch shape
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 4
        self.lives = 3

    # directions
    def turn_left(self):
        self.lt(45)
    def turn_right(self):
        self.rt(45)

    # change velocity
    def accelerate(self):
        self.speed += 1
    def deccelerate(self):
        self.speed -= 1

class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        # construct parent class
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        # set random direction
        self.setheading(random.randint(0, 360))

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        # construct parent class
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 8
        # set random direction
        self.setheading(random.randint(0, 360))

        def move(self):
            self.fd(self.speed)
            # boundary detection
            if self.xcor() > 290:
                self.setx(290)
                self.lt(60) 
            if self.xcor() < -290:
                self.setx(-290)
                self.lt(60)
            if self.ycor() > 290:
                self.sety(290)
                self.lt(60)
            if self.ycor() < -290:
                self.sety(-290)
                self.lt(60)

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        # construct parent class
        Sprite.__init__(self, spriteshape, color, startx, starty)
        # make missile shorter
        self.shapesize(stretch_wid=.2, stretch_len=.4, outline=None)
        self.speed = 20
        # what's going on with missile, missile not used in game beginning
        self.status = "ready"
        # move offscreen at start
        self.goto(-1000, 100)

    # set bullet to fire when firing
    def fire(self):
        if self.status == "ready":
            # play missile sound
            winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
            # missile set to fire at player's pos and heading
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    # move bullet when fired
    def move(self):
        # move off screen
        if self.status == "ready":
            self.goto(-1000, 100)
        # set to fire
        if self.status == "firing":
            self.fd(self.speed)

        # border check
        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"

class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        # construct parent class
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=.1, stretch_len=.1, outline=None)
        # initially offscreen
        self.goto(-1000, -100)
        # each particle called fram starting on frame 0
        self.frame = 0

    # different startx, starty
    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))
        self.frame = 1

    def move(self):
        # particles disappear after a while
        if self.frame > 0:
            self.fd(10)
            self.frame += 1
        if self.frame > 20:
            self.frame = 0
            self.goto(-1000, -1000)

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        # state of game
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        # set border pen
        self.pen.speed(0)
        self.pen.color("white")
        # thick border
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        # draw border
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = "Score: {}".format(self.score)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.write(msg, font=("Arial", 16, "normal"))

player = Player("triangle", "white", 0, 0)