# https://www.youtube.com/playlist?list=PLlEgNdBJEO-kK78GXDVzytiZlJtCyiFyW
# @TokyoEdTech
import turtle, math, random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create window
wn = turtle.Screen()
wn.setup(SCREEN_WIDTH + 220, SCREEN_HEIGHT + 20)
wn.title("Space Arena! by @TokyoEdTech")
wn.bgcolor("black")
# wn.tracer(0)

pen = turtle.Turtle()
# speed of animation
pen.speed(0)
pen.shape("square")
pen.color("white")
# no trail
pen.penup()
# don't need to see turtle
pen.ht()

class Game():
    # width and height of arena are much larger than screen
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 1
        self.state = "splash"

    def start_level(self):
        sprites.clear()
        # add enemy missiles
        for enemy_missile in enemy_missiles:
            sprites.append(enemy_missile)
        # add player
        sprites.append(player)
        # add missile
        for missile in missiles:
            sprites.append(missile)

        # add enemies in full arena, some might be hidden
        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            sprites.append(Enemy(x, y, "square", "red"))
            # last element in list
            sprites[-1].dx = dx
            sprites[-1].dy = dy

        # add opwerups in full arena, some might be hidden
        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            sprites.append(Powerup(x, y, "circle", "blue"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

    def render_border(self, pen, x_offset, y_offset):
        pen.color("white")
        pen.width(3)
        pen.penup()

        # left, right, top, bottom most coords
        left = -self.width / 2.0 - x_offset
        right = self.width / 2.0 - x_offset
        top = self.height / 2.0 - y_offset
        bottom = -self.height / 2.0 - y_offset

        # rectangle border
        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

    # render stats
    def render_info(self, pen, score, active_enemies = 0):
        # side bar
        pen.color("purple")
        pen.penup()
        pen.goto(400, 0)
        pen.shape("square")
        pen.setheading(90)
        pen.shapesize(10, 32, None)
        pen.stamp()
        # white border
        pen.color("white")
        pen.width(3)
        pen.width(3)
        pen.goto(300, 400)
        pen.pendown()
        pen.goto(300, -400)
        # text
        pen.penup()
        pen.color("white")
        character_pen.scale = 1.0
        character_pen.draw_string(pen, "SPACE ARENA", 400, 270)
        character_pen.draw_string(pen, "SCORE {}".format(score), 400, 240)
        character_pen.draw_string(pen, "ENEMIES {}".format(active_enemies), 400, 210)
        character_pen.draw_string(pen, "LIVES {}".format(player.lives), 400, 180)
        character_pen.draw_string(pen, "LEVEL {}".format(game.level), 400, 150)

    def start(self):
        self.state = "playing"

class CharacterPen():
    def __init__(self, color="white", scale = 1.0):
        self.color = color
        self.scale = scale

        # create dictionary to hold all character data
        self.characters = {}
        # series of tuples representing relatvie x,y coords
        # is modular and portable to other platforms
        self.characters["1"] = ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["2"] = ((-5, 10),(5, 10),(5, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["3"] = ((-5, 10),(5, 10),(5, 0), (0, 0), (5, 0), (5,-10), (-5, -10))
        self.characters["4"] = ((-5, 10), (-5, 0), (5, 0), (2,0), (2, 5), (2, -10))
        self.characters["5"] = ((5, 10), (-5, 10), (-5, 0), (5,0), (5,-10), (-5, -10))
        self.characters["6"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0))
        self.characters["7"] = ((-5, 10), (5, 10), (0, -10))
        self.characters["8"] = ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0))
        self.characters["9"] = ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0))
        self.characters["0"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))

        self.characters["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
        self.characters["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5,0), (5, -10), (-5, -10))
        self.characters["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
        self.characters["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
        self.characters["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
        self.characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
        self.characters["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
        self.characters["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))   
        self.characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
        self.characters["L"] = ((-5, 10), (-5, -10), (5, -10))
        self.characters["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
        self.characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
        self.characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
        self.characters["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
        self.characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
        self.characters["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
        self.characters["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10)) 
        self.characters["V"] = ((-5, 10), (0, -10), (5, 10)) 
        self.characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10)) 
        self.characters["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))   
        self.characters["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))   
        self.characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0,0), (0, -10))   
        self.characters["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))   
        
        self.characters["-"] = ((-3, 0), (3, 0)) 

    def draw_character(self, pen, character, x, y):
        # may want some characters bigger than others
        scale = self.scale
        # scales down lower case
        if character in "abcdefghijklmnopqrstuvwxyz":
            scale *= 0.6

        character = character.upper()

        # check if character is in dictionary
        if character in self.characters:
            pen.penup()
            # gives first set of coords
            xy = self.characters[character][0]
            # x + relative first x coor * scale, y + relative first y coord * scale
            pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.pendown()
            # start at 1
            for i in range(1, len(self.characters[character])):
                xy = self.characters[character][i]
                # x + relative xy x coor * scale, y + relative xy y coord * scale
                pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            # penup for next character
            pen.penup()

    def draw_string(self, pen, z, x, y):
        pen.width(2)
        pen.color(self.color)
        # center the text
        # if 10 characters, move left by 9/2 characters
        x -= 15 * self.scale * ((len(z) - 1) /2)
        for character in z:
            self.draw_character(pen, character, x, y)
            x += 15 * self.scale

# splash screen
# titles
character_pen = CharacterPen("red", 3.0)
character_pen.draw_string(pen, "SPACE ARENA", 0, 160)
character_pen.scale = 1.0
character_pen.draw_string(pen, "BY FANIEL YEMANE", 0, 100)
# instructions
# player
pen.color("white")
pen.shape("triangle")
pen.goto(-150, 20)
pen.stamp()
character_pen.draw_string(pen, "Player", -150, -20)
# enemy
pen.shape("square")
pen.goto(0, 20)
pen.stamp()
character_pen.draw_string(pen, "Enemy", 0, -20)
# powerup
pen.shape("circle")
pen.color("blue")
pen.goto(150, 20)
pen.stamp()
character_pen.draw_string(pen, "Powerup", 150, -20)
# controls
character_pen.draw_string(pen, "W key", -100, -60)
character_pen.draw_string(pen, "Accelerate", 100, -60)
character_pen.draw_string(pen, "A key", -100, -100)
character_pen.draw_string(pen, "Rotate Left", 100, -100)
character_pen.draw_string(pen, "D key", -100, -140)
character_pen.draw_string(pen, "Rotate Right", 100, -140)
character_pen.draw_string(pen, "Space", -100, -180)
character_pen.draw_string(pen, "Fire", 100, -180)
# initiation
character_pen.scale = 1.0
character_pen.draw_string(pen, "PRESS S TO START", 0, -220)
character_pen.draw_string(pen, "PRESS Q TO QUIT", 0, -260)
# shuts off screen updates
wn.tracer(0)

class Sprite():
    # constructor 
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0
        self.thrust = 0.0
        self.acceleration = 0.05
        self.health = 100
        self.max_health = 100
        self.width = 20
        self.height = 20
        self.state = "active"
        self.radar = 200
        self.max_dx = 5
        self.max_dy = 5

    # collision detection
    # axis aligned bouncing box method
    def is_collision(self, other):
        if self.x < other.x + other.width and\
            self.x + self.width > other.x and\
            self.y < other.y + other.height and\
            self.y + self.height > other.y:
            return True
        else:
            return False

    def bounce(self, other):
        temp_dx = self.dx
        temp_dy = self.dy
        
        self.dx = other.dx
        self.dy = other.dy
        
        other.dx = temp_dx
        other.dy = temp_dy

    # general update function
    def update(self):
        # change direction
        self.heading += self.da
        self.heading %= 360

        # separate vectors of dx and dy
        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
        # add to current x,y coords
        self.x += self.dx
        self.y += self.dy

        self.border_check()

    # bounce from border
    def border_check(self):
        if self.x > game.width / 2.0 - 10:
            self.x = game.width / 2.0 - 10
            self.dx *= -1
        elif self.x < -game.width / 2.0 + 10:
            self.x = -game.width / 2.0 + 10
            self.dx *= -1
        if self.y > game.height / 2.0 - 10:
            self.y = game.height / 2.0 - 10
            self.dy *= -1
        if self.y < -game.height / 2.0 + 10:
            self.y = -game.height / 2.0 + 10
            self.dy *= -1

    # draw the shape
    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            # put onto screen
            pen.stamp()

            self.render_health_meter(pen, x_offset, y_offset)

    def render_health_meter(self, pen, x_offset, y_offset):
        # draw health meter
        pen.goto(self.x - x_offset - 10, self.y - y_offset + 20)
        pen.width(3)
        pen.pendown()
        # from left to right
        pen.setheading(0)

        # whether health is full/half/low
        if self.health/self.max_health < 0.3:
            pen.color("red")
        elif self.health/self.max_health < 0.7:
            pen.color("yellow")
        else:
            pen.color("green")

        # health bar
        pen.fd(20.0 * (self.health/self.max_health))
        if self.health != self.max_health:
            pen.color("grey")
            # grey bar
            pen.fd(20.0 * ((self.max_health - self.health)/self.max_health))
        pen.penup()

class Player(Sprite):
    def __init__(self, x, y, shape, color):
        # inherits from sprite class
        Sprite.__init__(self, 0, 0, shape, color)
        # only player has score and lives
        self.lives = 3
        self.score = 0
        self.heading = 90
        # rotational speed
        self.da = 0

    # rotate
    def rotate_left(self):
        self.da = 6
    def rotate_right(self):
        self.da = -6
    def stop_rotation(self):
        self.da = 0
    def accelerate(self):
        self.thrust += self.acceleration
    def deccelerate(self):
        self.thrust = 0.0

    # fire missile
    def fire(self):
        # shoots missiles one at a time
        num_of_missiles = 0
        for missile in missiles:
            if missile.state == "ready":
                num_of_missiles += 1

        # 1 missie ready
        if num_of_missiles == 1:
            for missile in missiles:
                if missile.state == "ready":
                    # missile heading comes from player
                    missile.fire(self.x, self.y, self.heading, self.dx, self.dy)

        # 2 missiles ready
        if num_of_missiles == 2:
            directions = [-5, 5]
            for missile in missiles:
                if missile.state == "ready":
                    # missile heading comes from player
                    missile.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self.dy)

        # 3 missiles ready
        if num_of_missiles == 3:
            directions = [0, -5, 5]
            for missile in missiles:
                if missile.state == "ready":
                    # missile heading comes from player
                    missile.fire(self.x, self.y, self.heading + directions.pop(), self.dx, self.dy)

    # general update function
    def update(self):
        if self.state == "active":
            # change direction
            self.heading += self.da
            self.heading %= 360

            # separate vectors of dx and dy
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            # add to current x,y coords
            self.x += self.dx
            self.y += self.dy

            self.border_check()

            # check health
            if self.health <= 0:
                self.reset()

    # reset player pos and direction
    def reset(self):
        self.x = 0
        self.y = 0
        self.health = self.max_health
        self.heading = 90
        self.dx = 0
        self.dy = 0
        self.lives -= 1

    # draw the shape
    def render(self, pen, x_offset, y_offset):
        pen.shapesize(0.5, 1.0, None)
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        # put onto screen
        pen.stamp()
        # keep shapesize only for spaceship
        pen.shapesize(1.0, 1.0, None)

        self.render_health_meter(pen, x_offset, y_offset)

class Missile(Sprite):
    def __init__(self, x, y, shape, color):
        # inherits from sprite class
        Sprite.__init__(self, x, y, shape, color)
        # ready to fire
        self.state = "ready"
        self.thrust = 8.0
        self.max_fuel = 200
        self.fuel = self.max_fuel
        self.height = 4
        self.width = 4

    # when fired, set position and direction same as player
    def fire(self, x, y, heading, dx, dy):
        if self.state == "ready":
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy

            # separate vectors of dx and dy and add own thrust
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

    #  update function
    def update(self):
        if self.state == "active":
            # bullet is fueled for some time before it resets
            self.fuel -= self.thrust
            if self.fuel <= 0:
                self.reset()

            # change direction and position
            self.heading += self.da
            self.heading %= 360
            self.x += self.dx
            self.y += self.dy

            self.border_check()

    # resets missile and cleared
    def reset(self):
        self.fuel = self.max_fuel
        self.dx = 0
        self.dy = 0
        self.state = "ready"

    # draw the shape
    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(0.2, 0.2, None)
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            # put onto screen
            pen.stamp()
            # keep shapesize only for spaceship
            pen.shapesize(1.0, 1.0, None)

class EnemyMissile(Sprite):
    def __init__(self, x, y, shape, color):
        # inherits from sprite class
        Sprite.__init__(self, x, y, shape, color)
        # ready to fire
        self.state = "active"
        self.thrust = 8.0
        self.max_fuel = 200
        self.fuel = self.max_fuel
        self.height = 4
        self.width = 4

    # when fired, set position and direction same as player
    def fire(self, x, y, heading, dx, dy):
        if self.state == "ready":
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy

            # separate vectors of dx and dy and add own thrust
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

    #  update function
    def update(self):
        if self.state == "active":
            # bullet is fueled for some time before it resets
            self.fuel -= self.thrust
            if self.fuel <= 0:
                self.reset()

            # change direction and position
            self.heading += self.da
            self.heading %= 360
            self.x += self.dx
            self.y += self.dy

            self.border_check()

    # resets missile and cleared
    def reset(self):
        self.fuel = self.max_fuel
        self.dx = 0
        self.dy = 0
        self.state = "ready"

    # draw the shape
    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(0.2, 0.2, None)
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            # put onto screen
            pen.stamp()
            # keep shapesize only for spaceship
            pen.shapesize(1.0, 1.0, None)

class Enemy(Sprite):
    def __init__(self, x, y, shape, color):
        # inherits from sprite class
        Sprite.__init__(self, x, y, shape, color)
        self.max_health = 20
        self.health = self.max_health
        self.type = random.choice(["hunter", "mine", "surveillance"])

        # type determines color and shape
        if self.type == "hunter":
            self.color = "red"
            self.shape = "square"
        elif self.type == "mine":
            self.color = "orange"
            self.shape = "square"
        elif self.type == "surveillance":
            self.color = "pink"
            self.shape = "square"
       
    # general update function
    def update(self):
        if self.state == "active":
            # change direction
            self.heading += self.da
            self.heading %= 360

            # separate vectors of dx and dy
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            # add to current x,y coords
            self.x += self.dx
            self.y += self.dy

            # check border collision
            self.border_check()

            # check health
            if self.health <= 0:
                self.reset()

            # code for different types
            if self.type == "hunter":
                # flies toward player
                if self.x < player.x:
                    self.dx += 0.05
                else:
                    self.dx -= 0.05
                if self.y < player.y:
                    self.dy += 0.05
                else:
                    self.dy -= 0.05
            elif self.type == "mine":
                # sits still
                self.dx = 0
                self.dy = 0
            elif self.type == "surveillance":
                # flies away from player
                if self.x < player.x:
                    self.dx -= 0.05
                else:
                    self.dx += 0.05
                if self.y < player.y:
                    self.dy -= 0.05
                else:
                    self.dy += 0.05

            # set max speed
            # for x
            if self.dx > self.max_dx:
                self.dx = self.max_dx
            elif self.dx < -self.max_dx:
                self.dx = -self.max_dx
            # for y
            if self.dy > self.max_dy:
                self.dy = self.max_dy
            elif self.dy < -self.max_dy:
                self.dy = -self.max_dy

    def reset(self):
        self.state = "inactive"

class Powerup(Sprite):
    def __init__(self, x, y, shape, color):
        # inherits from sprite class
        Sprite.__init__(self, x, y, shape, color)

class Camera():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y

class Radar():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y =y 
        self.width = width
        self.height = height

    def render(self, pen, sprites):
        # draw radar circle
        pen.color("white", "black")
        pen.setheading(90)
        pen.goto(self.x + self.width/2.0, self.y)
        pen.pendown()
        pen.begin_fill()
        pen.circle(self.width/2.0)
        pen.end_fill()
        pen.penup()

        # draw sprites on radar
        for sprite in sprites:
            if sprite.state == "active":
                radar_x = self.x + (sprite.x - player.x) * (self.width/game.width)
                radar_y = self.y + (sprite.y - player.y) * (self.height/game.height)
                pen.goto(radar_x, radar_y)
                pen.shape(sprite.shape)
                pen.color(sprite.color)
                pen.setheading(sprite.heading)
                pen.shapesize(0.2, 0.2, None)

                # make sure the sprite is close to be within radar
                distance = math.sqrt((player.x - sprite.x)**2 + (player.y - sprite.y)**2)
                if distance < player.radar:
                    # show on screen
                    pen.stamp()

# create game object
game = Game(700, 500)
# create radar
radar = Radar(400, -200, 200, 200)
# create sprites
player = Player(0, 0, "triangle", "white")
# create camera
camera = Camera(player.x, player.y)
# create missile objects
missiles = []
for _ in range(3):
    missiles.append(Missile(0, 100, "circle", "yellow"))
# create enemy missiles
enemy_missiles = []
for _ in range(1):
    enemy_missiles.append(EnemyMissile(0, 100, "circle", "red"))
# sprites list
sprites = []

# setup the level
game.start_level()

def endgame():
    global running
    running = False
 
# keyboard bindings
wn.listen()
# rotations
wn.onkeypress(player.rotate_left, "a")
wn.onkeypress(player.rotate_right, "d")
# stop rotations
wn.onkeyrelease(player.stop_rotation, "a")
wn.onkeyrelease(player.stop_rotation, "d")
# acceleration
wn.onkeypress(player.accelerate, "w")
wn.onkeyrelease(player.deccelerate, "w")
# shoot
wn.onkeypress(player.fire, "space")
wn.onkeypress(game.start, "s")
wn.onkeypress(game.start, "S")
# quit
wn.onkey(endgame, "q")

# main loop
running = True
while running:
    if game.state == "splash":
        wn.update()
    elif game.state == "playing":
        # clear screen
        pen.clear()

        # do game stuff
        # fire enemy missiles
        for enemy_missile in enemy_missiles:
            if enemy_missile.state == "ready":
                # fire the missile
                # find all enemies
                enemies = []
                for sprite in sprites:
                    if isinstance(sprite, Enemy):
                        # list of currently active enemies
                        enemies.append(sprite)
                # gives 1 enemy
                enemy = random.choice(enemies)   
                # set heading
                heading = math.atan2(player.y - enemy.y, player.x - enemy.x)
                heading *= 180/math.pi
                enemy_missile.fire(enemy.x, enemy.y, heading, enemy.dx, enemy.dy)

        for sprite in sprites:
            # update sprites
            sprite.update()

            # check for collisions
            # check active enemy collisions with player and missile
            if isinstance(sprite, Enemy) and sprite.state == "active":
                if player.is_collision(sprite):
                    sprite.health -= 10
                    player.health -= 10
                    player.bounce(sprite)
                for missile in missiles:
                    if missile.state == "active" and missile.is_collision(sprite):
                        sprite.health -= 10
                        missile.reset()
            # check active powerup collisions with player and missile
            if isinstance(sprite, Powerup):
                if player.is_collision(sprite):
                    sprite.x = 100
                    sprite.y = 100
                for missile in missiles:
                    if missile.state == "active" and missile.is_collision(sprite):
                        sprite.x = 100 
                        sprite.y = -100
                        missile.reset()
            # check active enemy missile collisions with player
            if isinstance(sprite, EnemyMissile):
                if sprite.state == "active" and sprite.is_collision(player):
                    sprite.reset()
                    player.health -= 10

            # render sprite at camera (player pos)
            # gives relative coords to camera
            sprite.render(pen, camera.x + radar.width/2, camera.y)

        # draw border
        game.render_border(pen, camera.x + radar.width/2, camera.y)

        # check for end of level, assume level is over
        end_of_level = True
        for sprite in sprites:
            # look for an active enemy
            if isinstance(sprite, Enemy) and sprite.state == "active":
                # if enemy still active, level is not over
                end_of_level = False
        # if skip for loop, then level is over and restart
        if end_of_level:
            game.level += 1
            game.start_level()

        # update the camera with player's x and y coords
        camera.update(player.x, player.y)

        # draw the text
        game.render_info(pen, 0, 0)

        # render the radar
        radar.render(pen, sprites)

        # update the screen
        wn.update()
