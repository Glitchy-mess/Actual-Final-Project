"""
Final project planning
tetris but horrible, sprites are badly made generally don't fit together

steps to take
1. make a tileset of possible blocks, they are going to use 5 blocks for maximum asymetry, screen size is going to be 200x400 so that the player can actually play the game
2. make a collision logic to handle blocks going to the right bound, bottom and the left bound, then if the player's block runs into a "settled" block then end the current block instance
3. make a check every time a block settles to see if a line is made, and if so then delete that line and move everything down

priorities for sunday:
figure out how to reset the background to only display one image at a time
make collision for boundries
maybe get started on making block collision if you can think of a way to use it correctly

priorities for next week:
make settled blocks a thing
make collision for those settled blocks - save them into memory to be drawn every frame
terminate the program if a block immidiately collides with another block? could also make it so that the placement can't be above the top bound
"""
"""import pygame
from background import backgroundDraw

screenSize = (600,600)

pygame.init()
screen = pygame.display.set_mode(screenSize)
"""

#this sure is random
import pygame
from background import backgroundDraw
from BlockHandling import lBlock as LB
from tileset import randomizer
from gameLogic import gameLogic
pygame.init()
screenSize = (600,600)
screen = pygame.display.set_mode(screenSize)

tileSize = backgroundDraw(screenSize, screen)
#generalBlockFunct = generalBlock.blockMethods(screen, 0)

#generalBlockFunct.blockDraw()
pygame.display.flip()

GL = gameLogic(tileSize)
#yVal can't be resetted every frame as that would send the picture back to the top
yVal = 0
xVal = screenSize[0]/2
#can't really turn this into a class because i have to do stuff every frame and handling it from main makes life v e r y easy
"""
Use a list to store the vals of all the blocks after they settle, and then draw them in and activate the collisions
"""
gameState = False
newTile = True
BLACK = (0,0,0)
#pygame.Surface.blit(screen, file[0], (screenSize[0]/2,yVal))

file = randomizer(screen, tileSize)
image = file[0]
imageRect = image.get_rect()
LBInit = LB.LBlock(screen, image, imageRect)
frameRate = pygame.time.Clock()
sideBoundSize = [tileSize[2], screenSize[1] - tileSize[2]]
while not gameState:
  screen.fill(BLACK)
  backgroundDraw(screenSize, screen)
  frameRate.tick(15)

  pygame.Surface.blit(screen, image, (xVal,yVal))
  
  for event in pygame.event.get():
    #investigate why xVal doesn't get changed at all
    #better leave this as the first thing in case the user quits
    intervalSet = pygame.key.set_repeat(100)
    if event.type == pygame.QUIT:
     gameState = True
    elif event.type == pygame.KEYDOWN:
      
      xVal = GL.generalMovement(xVal, event.key, sideBoundSize, imageRect)
    
    #print("xVal = " + str(xVal))
  
    #first thing in priorities would include drawing and animating the bloc to move down. so first draww with blit and then redraw it until it hits the ground. then make collision and then figure out how to save the stored blcoks. just default to red block for now
    #if newTile == True:
      #file = randomizer(screen, tileSize)
      #pygame.Surface.blit(screen, file[0], (screenSize[0]/2,yVal))
    
    """elif event.type == pygame.K_a or event.type == pygame.K_LEFT:
      #xVelocity += 10
      #put in an if block that says something like if block not collided then newtile will be false"""
    """collision = False
      if collision == True:
        newTile = True
      else:
        newTile = False"""
    #resets the screen after the image moves, credits to the second answer in https://stackoverflow.com/questions/21516543/how-to-remove-draw-objects-from-pygame-window for giving that idea
    
    #generalBlockFunct.collision(blockNumber)
  
  yVal = GL.downMovement(yVal, sideBoundSize[1] ,imageRect)

  pygame.display.flip()
  
pygame.quit()