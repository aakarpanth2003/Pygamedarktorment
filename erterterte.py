from gamelib import*

game = Game(800, 800, "Delta Fighter")
#Create graphics variables
bk = Animation("field_5.png",5,game,1000,1000)
game.setBackground(bk)

title = Image("logo.png",game)
title.y -= 200

story = Image("story.png",game)
story.resizeBy(-40)
story.y += 100

howtoplay = Image("howtoplay.png",game)
howtoplay.resizeBy(-40)
howtoplay.y += 150
play = Image("play.png",game)
play.resizeBy(-40)
play.y += 200

hero = Image("hero.gif",game)
explosion = Animation("explosion1.png",20,game,1254/20,64)
explosion.visible = False#set the visiblity to false
#asteroids setup
asteroids = []#empty list
for index in range(100):#use a loop to add items
    asteroids.append( Animation( "asteroid1t.gif",41,game, 2173/41, 52))
for index in range(100):#use a loop to set the positions and speed
    x = randint(100,700)
    y = randint(100,4000)
    asteroids[index].moveTo(x, -y)
    #Zero degrees moves a graphics up
    asteroids[index].setSpeed(6,180)

#Ammo Setup
ammo = []
for index in range(20):
    ammo.append(Animation("plasmaball1.png",11,game,352/11,32))
    
for index in range(20):
    x = randint(100,700)
    y = randint(100,4000)
    ammo[index].moveTo(x, -y)
    ammo[index].setSpeed(6,180)

#Healthpod Setup
pods = []
for index in range(20):
    pods.append( Animation("healthpod.jpg",16,game,512/4,512/4,use_alpha=False))
    # NOTE: use_alpha value controls opaqueness of animation background
for index in range(20):
    x = randint(100,700)
    y = randint(100,4000)
    pods[index].moveTo(x, -y)
    pods[index].setSpeed(6,180)
    pods[index].resizeBy(-50)
    
#Title Screen - first game loop
while not game.over:
    game.processInput()

    game.scrollBackground("down",2)
    title.draw()
    story.draw()
    howtoplay.draw()
    play.draw()
    hero.draw()

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    
    game.update(30)

game.over = False#continue the game with a new game loop
#Level 1
asteroidPassed = 0#accumlator
ammocount = 0
while not game.over:
    game.processInput()
    
    game.scrollBackground("down",2)
    hero.draw()
    explosion.draw(False)
    #asteroids

    for index in range(100):#the loop will go through the list of asteroids
        asteroids[index].move()#each asteroid will move
        if asteroids[index].collidedWith(hero):#each asteroid is checked
            hero.health -= 1
            explosion.moveTo(asteroids[index].x,asteroids[index].y)
            explosion.visible = True
        if asteroids[index].isOffScreen("bottom") and asteroids[index].visible:
            asteroidPassed += 1
            asteroids[index].visible = False
            
        if asteroidPassed >= 100:
            game.over = True
        
        if hero.health <1:
            game.over = True

    #hero controls
    if keys.Pressed[K_UP]:
        hero.y -= 4#Up 4 pixels
    if keys.Pressed[K_DOWN]:
        hero.y += 4
    if keys.Pressed[K_RIGHT]:
        hero.x += 4
    if keys.Pressed[K_LEFT]:
        hero.x -= 4

    #Ammo
    for index in range(20):
        ammo[index].move()
        if ammo[index].collidedWith(hero):
            ammocount += 50
            ammo[index].visible = False
    #Healthpod
    for index in range(20):
        pods[index].move()
        if pods[index].collidedWith(hero):
            hero.health += 5
            pods[index].visible = False
            

    game.drawText("Health: " + str(hero.health), hero.x-20, hero.y+50)
    game.drawText("Ammo: " + str(ammocount),hero.x-10,hero.y+80)
    game.drawText("asteroidPassed: " + str(asteroidPassed), 600, 100)


    game.update(30)

game.quit()
