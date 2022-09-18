#https://www.youtube.com/playlist?list=PLlEgNdBJEO-muprNCDYiKLZ-Kc3-p8thS
#TokyoEdTech
from classes import *

wn = turtle.Screen()
# change background color
wn.bgcolor("black")
# change background image
wn.bgpic("kbgame-bg.gif")
# change window title
wn.title("SpaceWar")
# updates for every # frames, speeds up animation
wn.tracer(0)

# check if turtle appeas on screen, required on macOS
turtle.fd(0)
# set animation speed of turtle to max
turtle.speed(0)
# hide default turtle
turtle.ht()
# limits turtle memory
turtle.setundobuffer(1)

# create game object
game = Game()
# draw game border
game.draw_border()
# show game status
game.show_status()

# create objects
# enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)
# ally = Ally("square", "blue", 100, 0)

enemies, allies, particles = [], [], []
for i in range(6):
    enemies.append(Enemy("circle", "red", -100, 0))
    allies.append(Ally("square", "blue", 100, 0))
for i in range(20):
    particles.append(Particle("circle", "orange", 0, 0))

# keyboard bindings
turtle.onkey(player.turn_left, "a")
turtle.onkey(player.turn_right, "d")
turtle.onkey(player.accelerate, "w")
turtle.onkey(player.deccelerate, "s")
turtle.onkey(missile.fire, "space")
turtle.listen()

# main game loop
while True:
    # manually update screen after all calcs done
    wn.update()
    time.sleep(0.02)
    # move objects
    player.move()
    # enemy.move()
    missile.move()
    # ally.move()

    for enemy in enemies:
        enemy.move()

        # detect player-enemy collision
        if player.is_collision(enemy):
            # play explosion sound
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score -= 100
            game.show_status()

        # check for missile-enemy collision
        if missile.is_collision(enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = "ready"
            # increase score
            game.score += 100
            game.show_status()
            # do explosion
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())

    for ally in allies:
        ally.move() 

        # detect player-ally collision
        if missile.is_collision(ally):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            missile.status = "ready"
            # decrease score
            game.score -= 50
            game.show_status()

    for particle in particles:
        particle.move()

wn.mainloop()
     