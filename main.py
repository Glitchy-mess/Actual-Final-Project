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
screenSize = (600,600)
screen = pygame.display.set_mode(screenSize)

#draw the background and return the s
tileSize = backgroundDraw(screenSize, screen)
#generalBlockFunct = generalBlock.blockMethods(screen, 0)

#generalBlockFunct.blockDraw()
pygame.display.flip()

GL = gameLogic(tileSize)
#yVal can't be resetted every frame as that would send the picture back to the top

#can't really turn this into a class because i have to do stuff every frame and handling it from main makes life v e r y easy
"""
Use a list to store the vals of all the blocks after they settle, and then draw them in and activate the collisions
"""
gameState = False
newTile = True
BLACK = (0,0,0)
#what if collision list actually held every single individual tile that has dropped so that i can actually impliment clearing lines?
collisionList = []
#pygame.Surface.blit(screen, file[0], (screenSize[0]/2,yVal))



frameRate = pygame.time.Clock()

while not gameState:
  #resets the screen after the image moves, credits to the second answer in https://stackoverflow.com/questions/21516543/how-to-remove-draw-objects-from-pygame-window for giving that idea
  screen.fill(BLACK)
  backgroundDraw(screenSize, screen)
  #checks to see if a new tile needs to be made
  #screen.draw.text("Press A or D to move, arrow keys also work", (10,20), color = "black")

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
    currentBlockCollision = GL.settleCollision(screen, image, imageRect, pos, blockType)
    counter = 0

  frameRate.tick(15)
  textDraw(screen, tileSize[1])
  xChange = 0
  yChange = 0
  newTile = False
  pos = [xVal, yVal]
  pygame.Surface.blit(screen, image, pos)
  
  for event in pygame.event.get():
    #investigate why xVal doesn't get changed at all
    #checks to see if the usesr is still holding down a key every 100 milliseconds
    intervalSet = pygame.key.set_repeat(100)
    #better leave this as the first thing in case the user quits
    if event.type == pygame.QUIT:
     gameState = True
    #checks to see if a key is held down
    elif event.type == pygame.KEYDOWN:
      
      xMovement = GL.generalMovement(pos, event.key, sideBoundSize, imageRect, collisionList)
      xVal = xMovement[0]
      xChange = xMovement[1]
      counter = 0

    
    
  
  yMovement = GL.downMovement(pos, sideBoundSize[1] ,imageRect)
  yVal = yMovement[0]
  yChange = yMovement[1]
  if yChange == 0 and xChange == 0:
    counter += 1
    if counter != 10:
      collisionTile = (GL.settleCollision(screen, image, imageRect, pos, blockType))

    else:
      collisionList.append(collisionTile)
      newTile = True
  GL.lineClear(collisionList, screen)
  pygame.display.flip()
  
pygame.quit()