import turtle, math, random, time

# register shapes
images = ["wizard_right.gif", "wizard_left.gif",
          "treasure.gif", "wall.gif",
          "enemy_left.gif", "enemy_right.gif"]
for image in images:
    turtle.register_shape(image)

# create pen class
class Pen(turtle.Turtle):
    # setup pen constructor
    def __init__(self):
        # child of turtle class
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        # remove pen trail
        self.penup()
        # animation speed
        self.speed(0)
         
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wizard_right.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    # moving and boundary detection
    def go_up(self):
        # calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        # check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        # check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # calculate the spot to move to
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        self.shape("wizard_left.gif")
        # check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y) 

    def go_right(self):
        # calculate the spot to move to
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        self.shape("wizard_right.gif")
        # check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    # use pythagorean theorem to calc distance
    # bool functions starting with "is"
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance > 5:
            return False
        else:
            return True
 
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("enemy_left.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])
    # move mechanism
    def move(self):
        # sets direction and amount to move
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("enemy_left.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("enemy_right.gif")
        else:
            dx = 0
            dy = 0

        # check if player is close
        # if so, go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            if player.xcor() > self.xcor():
                self.direction = "right"
            if player.ycor() < self.ycor():
                self.direction = "down"
            if player.ycor() > self.ycor():
                self.direction = "up"

        # calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        # check if space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            # choose diff direction
            self.direction = random.choice(["up", "down", "left", "right"])

        # set timer to mvoe next time
        turtle.ontimer(self.move, t=random.randint(100, 300))

    # find if player close
    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance > 75:
            return False
        else:
            return True

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


player = Player()

# create wall coordinate list
walls = []