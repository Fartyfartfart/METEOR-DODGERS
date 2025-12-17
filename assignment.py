'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:

(put a link to your reference here but also add a comment in the code below where you used the reference)

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
pygame.init()

# *********SETUP**********

windowWidth = 600
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  #will allow us to set framerate


egg1 = 0
egg2 = windowWidth
speed = 2
RocketX= 250
RocketY= 250
Player1ROCKETSPEED = 5

RedRocket = pygame.transform.scale(pygame.image.load("RedRocket.png"), (200, 200))
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
    
    

    key = pygame.key.get_pressed()
    egg1 -= speed
    egg2 -= speed

    if egg1 <= -windowWidth:
        egg1 = windowWidth
    if egg2 <= -windowWidth:
        egg2 = windowWidth
    
    RocketY += (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * Player1ROCKETSPEED
    RocketX += (key[pygame.K_DOWN] - key[pygame.K_UP]) * Player1ROCKETSPEED

    window.blit(background, (egg1, 0))
    window.blit(background2, (egg2, 0))
    window.blit(RedRocket ,(RocketX, RocketY))

   
    #PUT YOUR GAME LOGIN HERE FOR EACH GAMESTATE
   
    # *********DRAW THE FRAME**********

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE'''

    # *********SHOW THE FRAME TO THE USER**********
    pygame.display.flip()
    clock.tick(60) #Force frame rate to 60fps or lower


pygame.quit()

