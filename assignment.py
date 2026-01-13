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

# *********SETUP**********

windowWidth = 600
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Meteor Dodgers")
ScoreFont= pygame.font.Font("PublicPixel-rv0pA.ttf", 30 )
clock = pygame.time.Clock()  #will allow us to set framerate

MeteorDelay = 0

ScoreFont = pygame.font.Font("PublicPixel-rv0pA.ttf", 30)
TitleFont = pygame.font.Font("PublicPixel-rv0pA.ttf", 40)
ButtonFont = pygame.font.Font("PublicPixel-rv0pA.ttf", 20)
CreditFont = pygame.font.Font("PublicPixel-rv0pA.ttf", 20)

Single = pygame.Rect(200, 220, 200, 50)
Double = pygame.Rect(200, 290, 200, 50)
TutorialButton = pygame.Rect(200, 360, 200, 50)
Return = pygame.Rect(200, 360, 200, 50)

pygame.mixer.music.load('background.mp3')
BackgroundMenu = pygame.transform.scale(

    pygame.image.load("Drawing.sketchpad.png"), (600, 500))

RocketX3 = 250  # starting position for double first player
RocketY3 = 250
RocketX2 = 350  # starting position for Player 2
RocketY2 = 250
RocketX= 250    # starting position for single
RocketY= 250
score = 0

egg1 = 0
egg2 = -windowHeight
speed = 2.7
Player1ROCKETSPEED = 5
Player2ROCKETSPEED = 5
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
TwoRedRocket = pygame.transform.scale(pygame.image.load("RedRocket.png"), (100, 100))
BlueRocket = pygame.transform.scale(pygame.image.load("a-rocket-in-pixel-art-style-vector-removebg-preview.png"), (145, 145))
background = pygame.transform.scale(pygame.image.load("1.webp"),(600, 500))
background2= pygame.transform.scale(pygame.image.load("e.webp"),(600, 500))
# *********GAME LOOP**********
while True:
    # *********EVENTS**********
    ev = pygame.event.poll()    # Look for any event
    if ev.type == pygame.QUIT:  # windowow close button clicked?
        break                   #   ... leave game loop
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.get_busy()
    #PUT YOUR MOUSE/KEYBOARD EVENTS HERE
   
    # *********GAME LOGIC**********
    if gamestate == "menu":
        window.blit(BackgroundMenu, (0,0))

        title = TitleFont.render("METEOR DODGERS", True, (255, 255, 255))
        pygame.draw.rect(window, (0, 0, 0), (10, 70, 580, 70))
        window.blit(title, (20, 80))

        credit = CreditFont.render("Credits: TerrenceT Inc™", True, (255, 255, 255))
        pygame.draw.rect(window, (0, 0, 0), (70, 155, 480, 50))
        window.blit(credit, (80, 165))

        pygame.draw.rect(window, (0, 0, 0), Single)
        pygame.draw.rect(window, (0, 0, 0), Double)
        pygame.draw.rect(window, (0, 0, 0), TutorialButton)

        window.blit(ButtonFont.render("Single", True, (255, 255, 255)), (240, 235))
        pygame.draw.rect(window, (255, 255, 255), Single, 3)
        DelayMeteor = pygame.time.get_ticks()
        window.blit(ButtonFont.render("Double", True, (255, 255, 255)), (237, 305))
        pygame.draw.rect(window, (255, 255, 255), Double, 3)
        window.blit(ButtonFont.render("Tutorial", True, (255, 255, 255)), (215, 375))
        pygame.draw.rect(window, (255, 255, 255), TutorialButton, 3)



        if ev.type == pygame.MOUSEBUTTONDOWN:
            
            if Single.collidepoint(ev.pos):
                gamestate = "game"

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if TutorialButton.collidepoint(ev.pos):
                gamestate = "tutorial"

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if Double.collidepoint(ev.pos):
                gamestate = "Double"
               
            
        pygame.display.flip()
        clock.tick(60)
        continue
    
            
    if gamestate == "tutorial":
            window.blit(Tutorial, (0, 0))
            pygame.display.flip()
            continue
                     

    if gameover:
        window.blit(ButtonFont.render("Single", True, (255, 255, 255)), (240, 235))
        pygame.draw.rect(window, (255, 255, 255), Return, 3)
        window.blit(GameOver, (0, 0))
        pygame.display.flip()
        continue

    if PlayerOneLost:
        window.blit(ButtonFont.render("Single", True, (255, 255, 255)), (240, 235))
        pygame.draw.rect(window, (255, 255, 255), Return, 3)
        window.blit(Player1Lost, (0, 0))
        pygame.display.flip()
        continue

    if PlayerTwoLost:
        window.blit(ButtonFont.render("Return", True, (255, 255, 255)), (240, 235))
        pygame.draw.rect(window, (255, 255, 255), Return, 3)
        window.blit(Player2Lost, (0, 0))
        pygame.display.flip()
        continue

    key = pygame.key.get_pressed()

    score += 1 / 60

    egg1 += speed
    egg2 += speed

    if egg1 >= windowHeight:
        egg1 = -windowHeight
    if egg2 >= windowHeight:
        egg2 = -windowHeight
    
        score += 1
        
    RocketY += (key[pygame.K_DOWN] - key[pygame.K_UP]) * Player1ROCKETSPEED
    RocketX += (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * Player1ROCKETSPEED
    

    window.blit(background, (0, egg1))
    window.blit(background2, (0, egg2))
    window.blit(RedRocket ,(RocketX, RocketY))


    currentTime = pygame.time.get_ticks() #Saumel Helped me on this Code
    if currentTime - DelayMeteor > 5000:

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

    if rocketRect.colliderect(pygame.Rect(MeteorX1, MeteorY1, 95, 95)):
        gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX2, MeteorY2, 95, 95)):
        gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX3, MeteorY3, 95, 95)): 
        gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX4, MeteorY4, 95, 95)): 
        gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX5, MeteorY5, 95, 95)):
        gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX6, MeteorY6, 95, 95)):
        gameover = True
    if rocketRect.colliderect(pygame.Rect(MeteorX7, MeteorY7, 95, 95)):
        gameover = True


    if RocketX < 0: #this code makes it so that the rocket cant exit the screen
        RocketX = 0 #this checks if the rocket go to the left so it blocks it by reseting the x
    if RocketX > windowWidth - 100:  
        RocketX = windowWidth - 100 #this checks if the rocket goes from the right of the screen and stops it so it stays visible

    if RocketY < 0:
        RocketY = 0 #this checks if the rocket go to the top so it blocks it by reseting the x
    if RocketY > windowHeight - 100: 
        RocketY = windowHeight - 100 #this checks if the rocket goes from the bottom of the screen and stops it so it stays visible


    ScorePlacement = ScoreFont.render(str(round(score)), True, (255,255,255))
    window.blit(ScorePlacement, (300, 15))
        

    if gamestate == "Double":
            clock.tick(60)
            key = pygame.key.get_pressed()

            score += 1 / 60

            egg1 += speed
            egg2 += speed

            if egg1 >= windowHeight:
                egg1 = -windowHeight
            if egg2 >= windowHeight:
                egg2 = -windowHeight
            
                score += 1
                
            RocketY3 += (key[pygame.K_DOWN] - key[pygame.K_UP]) * Player1ROCKETSPEED
            RocketX3 += (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * Player1ROCKETSPEED
            
            RocketY2 += (key[pygame.K_s] - key[pygame.K_w]) * Player2ROCKETSPEED
            RocketX2 += (key[pygame.K_d] - key[pygame.K_a]) * Player2ROCKETSPEED


            window.blit(background, (0, egg1))
            window.blit(background2, (0, egg2))
            window.blit(TwoRedRocket ,(RocketX3, RocketY3))
            window.blit(BlueRocket ,(RocketX2, RocketY2))

            if RocketX3 < 0: 
                RocketX3 = 0 
            if RocketX3 > windowWidth - 100:  
                RocketX3 = windowWidth - 100 

            if RocketY3 < 0:
                RocketY3 = 0 
            if RocketY3 > windowHeight - 100: 
                RocketY3 = windowHeight - 100

            if RocketX2 < 0: 
                RocketX2 = 0 
                if RocketX2 > windowWidth - 119:  
                    RocketX2 = windowWidth - 119 

            if RocketY2 < 0:
                RocketY2 = 0 
            if RocketY2 > windowHeight - 125: 
                RocketY2 = windowHeight - 125

            currentTime = pygame.time.get_ticks() #Saumel Helped me on this Code
            if currentTime - DelayMeteor > 5000:
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

                Red = pygame.Rect(RocketX3, RocketY3, 20, 20)
                Blue = pygame.Rect(RocketX2, RocketY2, 20, 20)

                if RocketX3 < 0: 
                    RocketX3 = 0 
                if RocketX3 > windowWidth - 100:  
                    RocketX3 = windowWidth - 100 

                if RocketY3 < 0:
                    RocketY3 = 0 
                if RocketY3 > windowHeight - 100: 
                    RocketY3 = windowHeight - 100

                if RocketX2 < 0: 
                    RocketX2 = 0 
                if RocketX2 > windowWidth - 100:  
                    RocketX2 = windowWidth - 100 

                if RocketY2 < 0:
                    RocketY2 = 0 
                if RocketY2 > windowHeight - 100: 
                    RocketY2 = windowHeight - 100



                if Red.colliderect(pygame.Rect(MeteorX1, MeteorY1, 95, 95)):
                    PlayerOneLost = True
                    gameover = False
                if Red.colliderect(pygame.Rect(MeteorX2, MeteorY2, 95, 95)):
                    PlayerOneLost = True
                    gameover = False
                if Red.colliderect(pygame.Rect(MeteorX3, MeteorY3, 95, 95)): 
                    PlayerOneLost = True
                    gameover = False
                if Red.colliderect(pygame.Rect(MeteorX4, MeteorY4, 95, 95)): 
                    PlayerOneLost = True
                    gameover = False
                if Red.colliderect(pygame.Rect(MeteorX5, MeteorY5, 95, 95)):
                    PlayerOneLost = True
                    gameover = False
                if Red.colliderect(pygame.Rect(MeteorX6, MeteorY6, 95, 95)):
                    PlayerOneLost = True
                    gameover = False
                if Red.colliderect(pygame.Rect(MeteorX7, MeteorY7, 95, 95)):
                    PlayerOneLost = True
                    gameover = False

                if Blue.colliderect(pygame.Rect(MeteorX1, MeteorY1, 95, 95)):
                    PlayerTwoLost = True
                if Blue.colliderect(pygame.Rect(MeteorX2, MeteorY2, 95, 95)):
                    PlayerTwoLost = True
                if Blue.colliderect(pygame.Rect(MeteorX3, MeteorY3, 95, 95)): 
                    PlayerTwoLost = True
                if Blue.colliderect(pygame.Rect(MeteorX4, MeteorY4, 95, 95)): 
                    PlayerTwoLost = True
                if Blue.colliderect(pygame.Rect(MeteorX5, MeteorY5, 95, 95)):
                    PlayerTwoLost = True
                if Blue.colliderect(pygame.Rect(MeteorX6, MeteorY6, 95, 95)):
                    PlayerTwoLost = True
                if Blue.colliderect(pygame.Rect(MeteorX7, MeteorY7, 95, 95)):
                    PlayerTwoLost = True

                ScorePlacement = ScoreFont.render(str(round(score)), True, (255,255,255))
                window.blit(ScorePlacement, (300, 15))

    #PUT YOUR GAME LOGIN HERE FOR EApy -3.13 -m pip install pygameCH GAMESTATE
   
    # *********DRAW THE FRAME**********

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE'''

    # *********SHOW THE FRAME TO THE USER**********
    pygame.display.flip()
    clock.tick(60) #Force frame rate to 60fps or lower
pygame.quit()
