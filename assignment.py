'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:

(put a link to your reference here but also add a comment in the code below where you used the reference)

https://www.youtube.com/watch?v=kEEgFNz_SHU
https://www.youtube.com/watch?v=fylVGdGBKYA

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

(put a list of required extensions so that the user knows that they need to download extra features)

-----------------------------------------------------------------------------

Known bugs:

(put a list of known bugs here, if you have any)

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level XXXXXX because ...

 Level 3 Requirements Met:
• 
•  
•  
•  
•  
• 

Features Added Beyond Level 3 Requirements:
• 
•  
•  
•  
•  
• 
-----------------------------------------------------------------------------
'''

import pygame
import random
pygame.init()

gamestate = "menu"
gameover = False
PlayerOneLost = False
PlayerTwoLost = False
Start = False
Twoplayer = False
Tutorial = False

# *********SETUP**********

windowWidth = 600
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  #will allow us to set framerate

egg1 = 0
egg2 = -windowHeight
speed = 2.7
RocketX= 250
RocketY= 250
Player1ROCKETSPEED = 5
MeteorX1= random.randint(0, 600)
MeteorY1= -10
meteorspeed1 = random.randint(3,5)

MeteorX2= random.randint(0, 600)
MeteorY2= -150
meteorspeed2 = random.randint(3,5)

MeteorX3= random.randint(0, 600)
MeteorY3= -200
meteorspeed3 = random.randint(3,5)

MeteorX4= random.randint(0, 600)
MeteorY4= -100
meteorspeed4 = random.randint(3,5)

MeteorX5= random.randint(0, 600)
MeteorY5= -270
meteorspeed5 = random.randint(3,5)

MeteorX6= random.randint(0, 600)
MeteorY6= -370
meteorspeed6 = random.randint(3,5)

MeteorX7= random.randint(0, 600)
MeteorY7= -470
meteorspeed7 = random.randint(3,5)

Tutorial = pygame.transform.scale(pygame.image.load("Tutorial.png"), (600, 500))
Player1Lost = pygame.transform.scale(pygame.image.load("Player1Lost.png"), (600, 500))
Player2Lost = pygame.transform.scale(pygame.image.load("Player2Lost.png"), (600, 500))
GameOver = pygame.transform.scale(pygame.image.load("GAME OVER.png"), (600, 500))
Meteor = pygame.transform.scale(pygame.image.load("Meteor.png"), (200, 200))
RedRocket = pygame.transform.scale(pygame.image.load("RedRocket.png"), (100, 100))
background = pygame.transform.scale(pygame.image.load("1.webp"),(600, 500))
background2= pygame.transform.scale(pygame.image.load("e.webp"),(600, 500))



# *********GAME LOOP**********
while True:
    # *********EVENTS**********
    ev = pygame.event.poll()    # Look for any event
    if ev.type == pygame.QUIT:  # windowow close button clicked?
        break                   #   ... leave game loop
   
    #PUT YOUR MOUSE/KEYBOARD EVENTS HERE
   
    # *********GAME LOGIC**********

    if gameover:
        window.blit(GameOver, (0, 0))
        pygame.display.flip()
        continue

    if PlayerOneLost:
        window.blit(Player1Lost, (0, 0))
        pygame.display.flip()
        continue

    if PlayerTwoLost:
        window.blit(Player2Lost, (0, 0))
        pygame.display.flip()
        continue

    key = pygame.key.get_pressed()
    egg1 += speed
    egg2 += speed

    if egg1 >= windowHeight:
        egg1 = -windowHeight
    if egg2 >= windowHeight:
        egg2 = -windowHeight
    
    RocketY += (key[pygame.K_DOWN] - key[pygame.K_UP]) * Player1ROCKETSPEED
    RocketX += (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * Player1ROCKETSPEED
    

    window.blit(background, (0, egg1))
    window.blit(background2, (0, egg2))
    window.blit(RedRocket ,(RocketX, RocketY))

    MeteorY1 += meteorspeed1
    window.blit(Meteor, (MeteorX1, MeteorY1))
    if MeteorY1 > windowHeight:
        MeteorX1= random.randint(0, 600)
        MeteorY1= -250
        meteorspeed1 = random.randint(3,5)

    MeteorY2 += meteorspeed2
    window.blit(Meteor, (MeteorX2, MeteorY2))
    if MeteorY2 > windowHeight:
        MeteorX2= random.randint(0, 600)
        MeteorY2= -100
        meteorspeed2 = random.randint(3,5)

    MeteorY3 += meteorspeed3
    window.blit(Meteor, (MeteorX3, MeteorY3))
    if MeteorY3 > windowHeight:
        MeteorX3= random.randint(0, 600)
        MeteorY3= -400
        meteorspeed3 = random.randint(3,5)

    MeteorY4 += meteorspeed4
    window.blit(Meteor, (MeteorX4, MeteorY4))
    if MeteorY4 > windowHeight:
        MeteorX4= random.randint(0, 600)
        MeteorY4= -300
        meteorspeed4 = random.randint(3,5)

    MeteorY5 += meteorspeed5
    window.blit(Meteor, (MeteorX5, MeteorY5))
    if MeteorY5 > windowHeight:
        MeteorX5= random.randint(0, 600)
        MeteorY5= -200
        meteorspeed5 = random.randint(3,5)

    MeteorY6 += meteorspeed6
    window.blit(Meteor, (MeteorX6, MeteorY6))
    if MeteorY6 > windowHeight:
        MeteorX6= random.randint(0, 600)
        MeteorY6= -700
        meteorspeed6 = 6

    MeteorY7 += meteorspeed7
    window.blit(Meteor, (MeteorX7, MeteorY7))
    if MeteorY7 > windowHeight:
        MeteorX7= random.randint(0, 600)
        MeteorY7= -300
        meteorspeed7 = 6

    rocketRect = pygame.Rect(RocketX, RocketY, 20, 20)

    if RocketX < 0: #this code makes it so that the rocket cant exit the screen
        RocketX = 0 #this checks if the rocket go to the left so it blocks it by reseting the x
    if RocketX > windowWidth - 100:  
        RocketX = windowWidth - 100 #this checks if the rocket goes from the right of the screen and stops it so it stays visible

    if RocketY < 0:
        RocketY = 0 #this checks if the rocket go to the top so it blocks it by reseting the x
    if RocketY > windowHeight - 100: 
        RocketY = windowHeight - 100 #this checks if the rocket goes from the bottom of the screen and stops it so it stays visible


    if rocketRect.colliderect(pygame.Rect(MeteorX1, MeteorY1, 100, 100)):
        gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX2, MeteorY2, 100, 100)):
        gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX3, MeteorY3, 100, 100)): 
        gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX4, MeteorY4, 100, 100)): 
         gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX5, MeteorY5, 100, 100)):
        gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX6, MeteorY6, 100, 100)):
        gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX7, MeteorY7, 100, 100)):
        gameover = True
        
   
    #PUT YOUR GAME LOGIN HERE FOR EApy -3.13 -m pip install pygameCH GAMESTATE
   
    # *********DRAW THE FRAME**********

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE'''

    # *********SHOW THE FRAME TO THE USER**********
    pygame.display.flip()
    clock.tick(60) #Force frame rate to 60fps or lower


pygame.quit()

