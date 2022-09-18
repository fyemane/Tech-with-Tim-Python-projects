import turtle, random, math, winsound

border_edge = 300
heart = "heart-20x20.gif"

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        # outside boundary box
        self.goto(-border_edge + 10, border_edge)
        self.score = 0

    # clears old score and updates to new one
    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, 
                   align="left", font=("Arial", 14, "normal"))

    # update score by number of points
    def change_score(self, points):
        self.score += points
        self.update_score()

    def play_sound(self, filename):
        winsound.PlaySound(filename, winsound.SND_ASYNC)

class Border(turtle.Turtle):
    def __init__(self):
        # class constructor for parent class
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        # animation speed
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-border_edge, -border_edge)
        self.pendown()
        self.goto(-border_edge, border_edge)
        self.goto(border_edge, border_edge)
        self.goto(border_edge, -border_edge)
        self.goto(-border_edge, -border_edge)

# player class is child of turtle class
class Player(turtle.Turtle):
    # class constructor
    def __init__(self):
        # initiate turtle class
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color("white")
        # own attribute
        self.speed = 1

    # create class method (moe)
    def move(self):
        # self.forward is builtin method  
        self.forward(self.speed)

        # border checking
        if self.xcor() > border_edge - 10 or self.xcor() < -border_edge + 10:
            self.left(60)
        if self.ycor() > border_edge - 10 or self.ycor() < -border_edge + 10:
            self.left(60)

    # directions
    def turnleft(self):
        self.left(30)
    def turnright(self):
        self.right(30)

    # acceleration
    def increasespeed(self):
        self.speed += 1
    def decreasespeed(self):
        self.speed -= 1

class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("circle")
        # self.shape(heart)
        self.speed = 3
        self.goto(random.randint(-border_edge + 50, border_edge - 50),
                  random.randint(-border_edge + 50, border_edge - 50))
        # set random direction
        self.setheading(random.randint(0, 360))

    # create class method
    def move(self):
        # self.forward is builtin method  
        self.forward(self.speed)

        # border checking
        if self.xcor() > border_edge - 10 or self.xcor() < -border_edge + 10:
            self.left(60)
        if self.ycor() > border_edge - 10 or self.ycor() < -border_edge + 10:
            self.left(60)
    
    # random position and direction
    def jump(self):
        self.goto(random.randint(-border_edge + 50, border_edge - 50),
                  random.randint(-border_edge + 50, border_edge - 50))
        self.setheading(random.randint(0, 360))

# collision check
def isCollision(t1, t2):
    # uses pythagorean theorem to check if object centers near to collide
    a = t1.xcor() - t2.xcor()
    b = t1.ycor() - t2.ycor()
    distance = math.sqrt((a **2) + (b ** 2))

    if distance < 20:
        return True
    else:
        return False
