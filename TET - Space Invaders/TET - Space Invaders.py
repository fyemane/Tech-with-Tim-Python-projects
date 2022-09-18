#https://www.youtube.com/playlist?list=PLlEgNdBJEO-lqvqL5nNNZC6KoRdSrhQwK
# with @TokyoEdTech
import turtle, math, random, os, platform

# if on Windows, you import winsound, or better yet, just use Linux
if platform.system() == "Windows":
    try:
        import winsound
    except:
        print("Winsound module not available")

# set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_background.gif")
wn.tracer(0)

# register shapes
wn.register_shape("player_spaceship.gif")
wn.register_shape("enemy_spaceship.gif")

# draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
# 3 pixels wide
border_pen.pensize(3)
# draw a square
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()

# set the score to 0
score = 0

# draw the score
score_pen = turtle.Turtle()
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = "Score: {}".format(score)
score_pen.write(score_string, False, align="left", 
                font=("Arial", 14, "normal"))
score_pen.hideturtle()

# create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player_spaceship.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
# rotate pen
player.setheading(90)
player.speed = 0

# chose a number of enemies
number_of_enemies = 30
# create an empty list of enemies
enemies = []
# add enemies to the list
for i in range(number_of_enemies):
    # create the enemy
    enemies.append(turtle.Turtle())

# position and number of each enemy
enemy_start_x = -225
enemy_start_y = 250
# track which enemy putting on screen
enemy_number = 0

# characteristics the enemy
for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy_spaceship.gif")
    enemy.shapesize(stretch_wid=0.05, stretch_len=0.05)
    enemy.penup()
    enemy.speed(0)
    # have enemies in rows
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    # update the enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemy_speed = 0.2

# create the player's bullets
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
# orientation of the bullet
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet_speed = 5

# define bullet states
# ready - bullet is ready to fire
# fire - bullet is firing
bullet_state = "ready"

# move the player left and right
def move_left():
    player.speed = -2
    
def move_right():
    player.speed = 2

def move_player():
    # takes current x value, subtracts player_speed and assigns value to x
    x = player.xcor()
    x += player.speed
    # boundary checking
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)

# function to fire the bullet
def fire_bullet():
    # declare bullet state as a global if it needs changing
    global bullet_state
    if bullet_state == "ready":
        play_sound("laser.wav")
        bullet_state = "fire"
        # move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

# check if collision takes place using pythagorean theorem math module
def is_collision(t1, t2):
    # pythagorean theorem
    distance = math.sqrt(math.pow(t2.xcor() - t1.xcor(), 2) + 
                         math.pow(t2.ycor() - t1.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

# cross-platform sound and repeats sound
def play_sound(sound_file, time=0):
    # Windows
    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    # Linux
    elif platform.system() == "Linux":
        os.system("aplay -q {}&".format(sound_file))
    # Mac
    else:
        os.system("afplay {}&".format(sound_file))

    # repeat sound, time is in seconds
    if time > 0:
        turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000))


# create keyboard bindings
wn.listen()
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")
wn.onkeypress(fire_bullet, "space")

# play background music
play_sound("bg-music.wav", 119)

# main game loop
while True:
    wn.update()

    move_player()

    for enemy in enemies:
        # move the enemy left/right
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # move the enemy back and down
        if enemy.xcor() > 280 or enemy.xcor() < -290:
            # moe all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # change enemy direction
            enemy_speed *= -1

        # check for collision between bullet and enemy
        if is_collision(bullet, enemy):
            play_sound("explosion.wav")
            # reset the bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            # reset the enemy
            #x = random.randint(-200, 200)
            #y = random.randint(100, 250)
            # enemy.setposition(x, y)
            enemy.setposition(0, 10000)
            # update the score
            score += 10
            score_string = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

        # check fo collision between player and enemy -> endgame
        if is_collision(player, enemy) or enemy.ycor() < -290:
            play_sound("explosion.wav")
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # check to see if bullet collides with boundary
    if bullet.ycor() > 200:
        bullet.hideturtle()
        bullet_state = "ready"
