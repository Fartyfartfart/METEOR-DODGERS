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

windowWidth = 500
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  #will allow us to set framerate

# *********GAME LOOP**********
while True:
    # *********EVENTS**********
    ev = pygame.event.poll()    # Look for any event
    if ev.type == pygame.QUIT:  # windowow close button clicked?
        break                   #   ... leave game loop
   
    #PUT YOUR MOUSE/KEYBOARD EVENTS HERE
   
    # *********GAME LOGIC**********
   
    #PUT YOUR GAME LOGIN HERE FOR EACH GAMESTATE
   
    # *********DRAW THE FRAME**********

    #PUT YOUR DRAWING, IMAGE PLACEMENT, BLIT ETC.. COMMANDS HERE FOR EACH GAMESTATE'''

    # *********SHOW THE FRAME TO THE USER**********
    pygame.display.flip()
    clock.tick(60) #Force frame rate to 60fps or lower


pygame.quit()

egg1 = 0
egg2 = width
speed = 1


background = pygame.transform.scale(pygame.image.load("eee.jpg"),(1000, 800))
background2= pygame.transform.scale(pygame.image.load("ee.jpg"),(1000, 800))


run = True
while run:
    
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            quit()
    
    egg1 -= speed
    egg2 -= speed

    if egg1 <= -width:
        egg1 = width
    if egg2 <= -width:
        egg2 = width

    display.blit(background, (egg1, 0))
    display.blit(background2, (egg2, 0))

    
    pygame.display.update()

    pygame.display.flip ()