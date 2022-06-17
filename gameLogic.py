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
  #run through all the tiles and make sure that its a) in the same y val, and b) 
    #this is the buggiest thing i've had the displeasure of working with, i'm just leaving it in so that i can actually look at it after finals are completed
  """def movementCollisionCheck(self, tileCollision, movementChange, pos, collisionBound, movementNumber):
    collisionCheck = False
    #movement change might have to be negative just to account for this being both pos and negative values
    newTranslation = movementChange
    for collisions in tileCollision:
      for settledCoords in collisions:
        for collisionCord in collisionBound:
          collisionCord += movementChange
          rightSettleCoord = settledCoords[0][0] + settledCoords[0][2]
          
          leftSettleCoord = settledCoords[0][0]
          
          if collisionCord <= leftSettleCoord and pos[0] <= settledCoords[0][0] and movementNumber == 1:
            collisionCheck = True
            newTranslation = pos[0] + (settledCoords[0][0] - pos[0])
            print(newTranslation)
            return collisionCheck, newTranslation
            
          elif collisionCord <= rightSettleCoord and pos[0] >= settledCoords[0][0] and movementNumber == 2:
            collisionCheck = True
            #returns a negative value
            newTranslation = pos[0] + (settledCoords[0][0] - pos[0])
            print(newTranslation)
            return collisionCheck, newTranslation
          
          else:
            continue
    return collisionCheck, newTranslation"""

    
  
  def downMovement(self, pos, screenWidth, screenRect):
    pos[1] += self.ySpeed
    bottomYPos = pos[1] + screenRect[3]
    yChange = self.ySpeed

    if bottomYPos >= screenWidth:
          pos[1] = screenWidth - screenRect[3]
          yChange = 0
    return pos[1], yChange
    
  def generalMovement(self, pos, event, screenLength, rectWidth, tileCollision, currentBlockCollision):
    #try handling all of the movement here?
    """
    Priorities for collision
    find the right and left bound of the image and then say that the right bound can't exceed the funny thing, left bound has already been defined and can work though. prob just use the get_rect() command to get a rectangle and then add its length for the right wall
    """
    leftXBounds = []
    rightXBounds = []
    topYBounds = []
    xChange = self.xSpeed
    #gets the x and y bounds of the image, you can compare this with the 
    for collisions in currentBlockCollision:
      for coords in collisions:
        leftXBounds.append(coords[0])
        rightXBounds.append(coords[0] + coords[2])
        topYBounds.append(coords[1])
        
    if event == pygame.K_RIGHT or event == pygame.K_d:
      #also position is going to be a tuple
      pos[0] += self.xSpeed
      rightXPos = rectWidth[2] + pos[0]

      if rightXPos >= screenLength[1]:
        pos[0] = screenLength[1] - rectWidth[2]
        xChange = 0
      
    elif event == pygame.K_LEFT or event == pygame.K_a:
      pos[0] -= self.xSpeed
      #make xChange a negative value because we're referring to a general equation
      
      if pos[0] <= screenLength[0]:
        pos[0] = screenLength[0]
        xChange = 0

    return pos[0], xChange
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
      for tileCoordinateList in tiles:
        for cords in tileCoordinateList:
          pygame.draw.rect(screen, GRAY, (cords[0], cords[1], cords[2],cords[3]))
    """if collisionCheck == True:
      pass"""