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

import pygame
from background import backgroundDraw, textDraw

from tileset import randomizer
from gameLogic import gameLogic

#initialize the program
pygame.init()

#changing the screen size does break the scaling of the blocks, so its not quite dynamic yet
screenSize = (600,600)
screen = pygame.display.set_mode(screenSize)

#draw the background and return the s
tileSize = backgroundDraw(screenSize, screen)

pygame.display.flip()

GL = gameLogic(tileSize)


gameState = False
newTile = True
BLACK = (0,0,0)
collisionList = []
#initializes the framerate class from pygame, which gets called in the loop
frameRate = pygame.time.Clock()

#runs the program forever until the user exits, will add another exit via the game's actual purpose
while not gameState:
  #resets the screen after the image moves, credits to the second answer in https://stackoverflow.com/questions/21516543/how-to-remove-draw-objects-from-pygame-window for giving that idea
  screen.fill(BLACK)
  backgroundDraw(screenSize, screen)
  #checks to see if a new tile needs to be made, if so then initialize a bunch of variables and functions
  if newTile == True:
    yVal = 0
    xVal = screenSize[0]/2
    #pos is initialized twice so that currentBlockCollision can actually run
    pos = [xVal, yVal]
    file = randomizer(screen, tileSize)
    image = file[0]
    blockType = file[2] + 1
    imageRect = image.get_rect()
    sideBoundSize = [tileSize[1], screenSize[1] - tileSize[1]]
    #initializes the current block's collision so that it can be compared with the ones that have settled already
    currentBlockCollision = GL.settleCollision(screen, image, imageRect, pos, blockType)
    counter = 0
  #runs the program at 15 fps which was a pretty good speed for gameplay
  frameRate.tick(15)
  #draws the text on the screen
  textDraw(screen, tileSize[1])
  #initialize relevant values and draw the block on the screen
  xChange = 0
  yChange = 0
  newTile = False
  pos = [xVal, yVal]
  pygame.Surface.blit(screen, image, pos)
  #checks for events before doing any translations or drawings
  for event in pygame.event.get():
    
    #checks to see if the usesr is still holding down a key every 100 milliseconds
    intervalSet = pygame.key.set_repeat(100)
    
    # leave this as the first thing in case the user quits
    if event.type == pygame.QUIT:
     gameState = True
    #checks to see if a key is held down
    elif event.type == pygame.KEYDOWN:
      #handles the change in x values
      xMovement = GL.generalMovement(pos, event.key, sideBoundSize, imageRect, collisionList)
      xVal = xMovement[0]
      xChange = xMovement[1]
      counter = 0

    
    
  #handles the change in y values
  yMovement = GL.downMovement(pos, sideBoundSize[1] ,imageRect)
  yVal = yMovement[0]
  yChange = yMovement[1]
  #checks to see if the player has stopped moving
  if yChange == 0 and xChange == 0:
    counter += 1
    
    #draws a red box around the tiles that act as the block's collision
    collisionTile = (GL.settleCollision(screen, image, imageRect, pos, blockType))
    
    
    #checks to see if the player has stopped moving for 10 ticks, if they haven't then continue on w/the program
    if counter == 10:  
      #adds the collision bounds of the block that has been placed and gets a new block
      collisionList.append(collisionTile)
      newTile = True
      
  #draws the block collisions, doesn't require also looking at collision cause the movement covers that
  GL.lineClear(collisionList, screen)
  pygame.display.flip()
  
pygame.quit()