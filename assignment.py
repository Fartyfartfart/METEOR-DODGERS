'''
-----------------------------------------------------------------------------
Program Name: Meteor Dodgers
Program Description:This game is a simple game where you move ur rokcet down and attempt to beat ur own score. You can play with Freinds and Family in an attempt to beat them or team up and survive the longest. Player 1 has WASD key and Player 2 has the arrow keys

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

N/A

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level +4 because It has met all the level 3 requirments while also going beyond having a 2 player mode, no bugs, delay for the metor, showes score for 2 player and single player, comments, and many more. Commitments were made EVERYDAY IN CLASS execpt for the half day which I wasnt here for because I went on vacation and the snowday. The Interview personally I think I did well in because I was able to explain my code from top to bottom and was able to answer the questions that you provided for me. 

 Level 3 Requirements Met:

 ***WINDOW SIZE LESS THAN 1280 (WIDE) X 720 (HIGH) PLEASE***
***MUST GET PERMISSION FROM TEACHER TO USE CODING TECHNIQUES THAT WERE NOT TAUGHT IN VIDEOS***
The game uses user events (keyboard and/or mouse input from the user)
All user input is sanitized (ie, won’t crash your program)
The program must use a variable.
Use appropriate data types (int, String, long).
Use conditional structures (if-statement, boolean operators).
Use loop structures (for, while).
Create and use custom functions.
Encapsulate the final program to include multiple screens with a menu system to move between them. (For example: an intro screen, main screen, and end screen).
The program should have clear instructions on how to use/play.
The program must have a soundtrack and sounds.
The program uses images
Coding decisions should make sense and not include grossly inefficient code.
The program must have collision detection
The program must have a custom downloaded font


Features Added Beyond Level 3 Requirements:
• 2 Player mode with a WASD key fully working
• Custom background made by me for the menu
• No bugs in the code 
• Game is neat and organized and displays ur score at the end 
• Smooth
• Has a delay of 5 seconds for the meteor to come when you press play both in 2 player and single player so you have time to prepaare
-----------------------------------------------------------------------------
'''

import pygame
import random
pygame.init()

gamestate = "menu" #gamestate for the menu
gameover = False #Gameover is set to false so it dosnt show right away when it needs to 
PlayerOneLost = False  #PlayerOneLost is set to false so it dosnt show right away when it needs to 
PlayerTwoLost = False  #PlayerTwoLost is set to false so it dosnt show right away when it needs to 

# *********SETUP**********

windowWidth = 600 #Width of the Window
windowHeight = 500 #Height of the window
window = pygame.display.set_mode((windowWidth, windowHeight)) #setting the window to 600 by 500
pygame.display.set_caption("Meteor Dodgers") #showes the name of the assignment on the top left of the screen
clock = pygame.time.Clock()  #will allow us to set framerate

MeteorDelay = 0 #sets the meteor delay to 0 so that later on in the code the meteors will delay by 5 seconds

ScoreFont = pygame.font.Font("PublicPixel-rv0pA.ttf", 30) #the same font for the score for each of the different parts this is for score
TitleFont = pygame.font.Font("PublicPixel-rv0pA.ttf", 40) #the same font for the score for each of the different parts this is for title
ButtonFont = pygame.font.Font("PublicPixel-rv0pA.ttf", 20) #the same font for the score for each of the different parts this is for button
CreditFont = pygame.font.Font("PublicPixel-rv0pA.ttf", 20) #the same font for the score for each of the different parts this is for Credits (The font for TerrenceT inc)

Single = pygame.Rect(200, 220, 200, 50) 
Double = pygame.Rect(200, 290, 200, 50)
TutorialButton = pygame.Rect(200, 360, 200, 50)
Return = pygame.Rect(200, 420, 200, 50) 

pygame.mixer.music.load('background.mp3') #background music in mind dosnt change it when I preload this in the game
BackgroundMenu = pygame.transform.scale(

    pygame.image.load("Drawing.sketchpad.png"), (600, 500))  #Image for my background image keeps this in mind for me to preload this (Background was made by me)

RocketX3 = 250  # starting position for double first player
RocketY3 = 250
RocketX2 = 350  # starting position for Player 2
RocketY2 = 250
RocketX= 250    # starting position for single
RocketY= 250
score = 0 #score set to 0 everytime when we click play or 2 player

egg1 = 0
egg2 = -windowHeight
speed = 2.7
Player1ROCKETSPEED = 5
Player2ROCKETSPEED = 5

MeteorX1= random.randint(0, 600) #meteor spawn from the width of 0 to 600 randomly
MeteorY1= -10 #starting valye is -10 for the meteor
meteorspeed1 = random.randint(3,5) #speed from 3-5

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


Tutorial = pygame.transform.scale(pygame.image.load("Tutorial.png"), (600, 500)) #this code keeps the image in mind so i can preload it later
Player1Lost = pygame.transform.scale(pygame.image.load("Player1Lost.png"), (600, 500)) #this code keeps the image in mind so i can preload it later
Player2Lost = pygame.transform.scale(pygame.image.load("Player2Lost.png"), (600, 500)) #this code keeps the image in mind so i can preload it later
GameOver = pygame.transform.scale(pygame.image.load("GAME OVER.png"), (600, 500)) #this code keeps the image in mind so i can preload it later
Meteor = pygame.transform.scale(pygame.image.load("Meteor.png"), (200, 200)) #this code keeps the image in mind so i can preload it later
RedRocket = pygame.transform.scale(pygame.image.load("RedRocket.png"), (100, 100)) #this code keeps the image in mind so i can preload it later
TwoRedRocket = pygame.transform.scale(pygame.image.load("RedRocket.png"), (100, 100)) #this code keeps the image in mind so i can preload it later
BlueRocket = pygame.transform.scale(pygame.image.load("a-rocket-in-pixel-art-style-vector-removebg-preview.png"), (145, 145)) #this code keeps the image in mind so i can preload it later
background = pygame.transform.scale(pygame.image.load("1.webp"),(600, 500)) #this code keeps the image in mind so i can preload it later
background2= pygame.transform.scale(pygame.image.load("e.webp"),(600, 500)) #this code keeps the image in mind so i can preload it later
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
    if gamestate == "menu": #ensures the code only runs when the game is in the menu
        window.blit(BackgroundMenu, (0,0))# the background screen is displayed

        title = TitleFont.render("METEOR DODGERS", True, (255, 255, 255)) #title design (white) and what it says 
        pygame.draw.rect(window, (0, 0, 0), (10, 70, 580, 70))#Black border for the title
        window.blit(title, (20, 80)) #title is displayed 

        credit = CreditFont.render("Credits: TerrenceT Inc™", True, (255, 255, 255)) #The next three code is the same as the one on top while displaying the credit 
        pygame.draw.rect(window, (0, 0, 0), (70, 155, 490, 50))
        window.blit(credit, (80, 165)) 

        pygame.draw.rect(window, (0, 0, 0), Single) #Displays the button black rectange for these three lines
        pygame.draw.rect(window, (0, 0, 0), Double)
        pygame.draw.rect(window, (0, 0, 0), TutorialButton)

        window.blit(ButtonFont.render("Single", True, (255, 255, 255)), (240, 235)) #displays the Buttonfont, what it says, the white color of it
        pygame.draw.rect(window, (255, 255, 255), Single, 3) #showes the white outline around the rectange
        window.blit(ButtonFont.render("Double", True, (255, 255, 255)), (237, 305))
        pygame.draw.rect(window, (255, 255, 255), Double, 3)
        window.blit(ButtonFont.render("Tutorial", True, (255, 255, 255)), (215, 375))
        pygame.draw.rect(window, (255, 255, 255), TutorialButton, 3)

        DelayMeteor = pygame.time.get_ticks()



        if ev.type == pygame.MOUSEBUTTONDOWN:
            
            if Single.collidepoint(ev.pos):
                score = 0
                gameover = False
                gamestate = "game"
                RocketX = 250
                RocketY = 250

                MeteorY1 = -10
                MeteorY2 = -150
                MeteorY3 = -200
                MeteorY4 = -100
                MeteorY5 = -270
                MeteorY6 = -370
                MeteorY7 = -470
                DelayMeteor = pygame.time.get_ticks()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if TutorialButton.collidepoint(ev.pos):
                gamestate = "tutorial"

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if Double.collidepoint(ev.pos):
                score = 0
                PlayerOneLost = False
                PlayerTwoLost = False
                gamestate = "Double"
                RocketX = 250
                RocketY = 250
                
                MeteorY1 = -10
                MeteorY2 = -150
                MeteorY3 = -200
                MeteorY4 = -100
                MeteorY5 = -270
                MeteorY6 = -370
                MeteorY7 = -470
                DelayMeteor = pygame.time.get_ticks()

        
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if Return.collidepoint(ev.pos):
                gamestate = "Return"
               
            
        pygame.display.flip()
        clock.tick(60)
        continue


    if gamestate == "tutorial":
            window.blit(Tutorial, (0, 0))
            pygame.draw.rect(window, (0, 0, 0), Return)
            window.blit(ButtonFont.render("Return", True, (255, 255, 255)), (240, 435))
            pygame.draw.rect(window, (255, 255, 255), Return, 3)

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if Return.collidepoint(ev.pos):
                    gamestate = "menu"
                    gameover = False
                    PlayerOneLost = False
                    PlayerTwoLost = False

            pygame.display.flip()
            continue
                     

    if gameover:
        window.blit(GameOver, (0, 0))
        ShowingDaScore = ScoreFont.render("Score: " + str(round(score)), True, (255, 255, 255)) 
        window.blit(ShowingDaScore, (170, 260))
        pygame.draw.rect(window, (0, 0, 0), Return)
        window.blit(ButtonFont.render("Return", True, (255, 255, 255)), (240, 435))
        pygame.draw.rect(window, (255, 255, 255), Return, 3)
        pygame.display.flip()

        if ev.type == pygame.MOUSEBUTTONDOWN:
                if Return.collidepoint(ev.pos):
                    gamestate = "menu"
                    gameover = False

        continue

    if PlayerOneLost:
        window.blit(Player1Lost, (0, 0))
        ShowingDaScore = ScoreFont.render("Score: " + str(round(score)), True, (255, 255, 255)) 
        window.blit(ShowingDaScore, (175, 45))
        pygame.draw.rect(window, (0, 0, 0), Return)
        window.blit(ButtonFont.render("Return", True, (255, 255, 255)), (240, 435))
        pygame.draw.rect(window, (255, 255, 255), Return, 3)

        if ev.type == pygame.MOUSEBUTTONDOWN:
                if Return.collidepoint(ev.pos):
                    gamestate = "menu"
                    PlayerOneLost = False

        pygame.display.flip()
        continue

    if PlayerTwoLost:
        window.blit(Player2Lost, (0, 0))
        ShowingDaScore = ScoreFont.render("Score: " + str(round(score)), True, (255, 255, 255)) 
        window.blit(ShowingDaScore, (175, 45))
        pygame.draw.rect(window, (0, 0, 0), Return)
        window.blit(ButtonFont.render("Return", True, (255, 255, 255)), (240, 435))
        pygame.draw.rect(window, (255, 255, 255), Return, 3)

        if ev.type == pygame.MOUSEBUTTONDOWN:
                if Return.collidepoint(ev.pos):
                    gamestate = "menu"
                    PlayerTwoLost = False

        pygame.display.flip()
        continue

    key = pygame.key.get_pressed()
    if gamestate == "game":

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
            #Refrence: https://www.youtube.com/watch?v=kEEgFNz_SHU



        ScorePlacement = ScoreFont.render(str(round(score)), True, (255,255,255))
        window.blit(ScorePlacement, (300, 15))
            
#The rest Of this code is the same thing above exept for the 2 player movement key which I have commented on it
    if gamestate == "Double":

            score += 1 / 60

            egg1 += speed
            egg2 += speed

            if egg1 >= windowHeight:
                egg1 = -windowHeight
            if egg2 >= windowHeight:
                egg2 = -windowHeight
            
                score += 1
                
            RocketY3 += (key[pygame.K_DOWN] - key[pygame.K_UP]) * Player1ROCKETSPEED #Up and down movement for the arrow keys of player 1
            RocketX3 += (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * Player1ROCKETSPEED #Left and Right movement for the arrow keys of player 1
            
            RocketY2 += (key[pygame.K_s] - key[pygame.K_w]) * Player2ROCKETSPEED #Up and down movement for the WASD of player 2
            RocketX2 += (key[pygame.K_d] - key[pygame.K_a]) * Player2ROCKETSPEED #Left and Right movement for the WASD of player 2
            
            #refrence https://www.youtube.com/watch?v=fylVGdGBKYA



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

            if RocketX2 < -20: 
                RocketX2 = -20 
            if RocketX2 > windowWidth - 119:  
                RocketX2 = windowWidth - 119 

            if RocketY2 < -20:
                RocketY2 = -20
            if RocketY2 > windowHeight - 125: 
                RocketY2 = windowHeight - 125

            currentTime = pygame.time.get_ticks() #Saumel Helped me on this Code this code delays the meteor
            if currentTime - DelayMeteor > 5000: #delays it by 5 seconds
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
