"""
Make an abstract class for all of the blocks so that they can collide with each other and fall down the screen


"""
import pygame
from BlockHandling.lBlock import LBlock as LB
from BlockHandling.canteenBlock import CBlock as CB
from BlockHandling.snakeBlock import SBlock as SB
from BlockHandling.tBlock import TBlock as TB
from BlockHandling.uBlock import UBlock as UB
class gameLogic():
  def __init__(self,tileSize):
    #self.screen = screen
    #figure out how to scale everything to the tiles in the game
    self.incriment = tileSize
    self.xSpeed = self.incriment[0]
    self.ySpeed = self.incriment[1]/1.5
    #handles y movement every tick
  def downMovement(self, yPos, screenWidth, screenRect):
    yPos += self.ySpeed
    bottomYPos = yPos + screenRect[3]
    yChange = self.ySpeed
    #print(bottomYPos, yPos, screenWidth, self.ySpeed)
    if bottomYPos >= screenWidth:
      yPos = screenWidth - screenRect[3]
      yChange = 0
    return yPos, yChange
    
  def generalMovement(self, xPos, event, screenLength, rectWidth):
    #try handling all of the movement here?
    """
    Priorities for collision
    find the right and left bound of the image and then say that the right bound can't exceed the funny thing, left bound has already been defined and can work though. prob just use the get_rect() command to get a rectangle and then add its length for the right wall
    """
    xChange = self.xSpeed
    if event == pygame.K_RIGHT or event == pygame.K_d:
      #also position is going to be a tuple
      xPos += self.xSpeed
      rightXPos = rectWidth[2] + xPos
      if rightXPos >= screenLength[1]:
        xPos = screenLength[1] - rectWidth[2]
        xChange = 0
      
    elif event == pygame.K_LEFT or event == pygame.K_a:
      xPos -= self.xSpeed
      
      if xPos <= screenLength[0]:
        xPos = screenLength[0]
        xChange = 0
    return xPos, xChange
      #find a way to get the lower bounds
    #also make a check to see if the player is holding down left or right, if so then don't drop the block yet
    """
    Try to make something like
    if there's a rectangle in the screen that stretches throughout the thing
    clear out the middle
    translate everything in the dictionary for x positions to be one tile down"""

  def settleCollision(self, screen, image, imageRect, tileSize, pos, blockType):
    if blockType == 1 or blockType == 2:
      blockSettle = SB(screen, image, imageRect, tileSize, blockType)
    elif blockType == 3:
      blockSettle = TB(screen, image, imageRect, tileSize)
    elif blockType == 4 or blockType == 5:
      blockSettle = CB(screen, image, imageRect, tileSize, blockType)
    elif blockType == 6:
      blockSettle = UB(screen, image, imageRect, tileSize)
    else:
      blockSettle = LB(screen, image,imageRect, tileSize)
      
    
    collisionList = blockSettle.collisionBounds(pos)
    return collisionList
    
  def lineClear(self, collisionList, screen):
    GRAY = [189,189,189]
    for tiles in collisionList:
      for tileCoordinates in tiles:
        pygame.draw.rect(screen, GRAY, (tileCoordinates[0], tileCoordinates[1], tileCoordinates[2],tileCoordinates[3]))