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
    #initialize incriments and the speed values
    self.incriment = tileSize[0]
    self.xSpeed = self.incriment
    self.ySpeed = self.incriment / 1.5
    
  #movementCollisionCheck is the buggiest thing i've had the displeasure of working with, i'm just leaving it in so that i can actually look at it after finals are completed
  """
  def movementCollisionCheck(self, tileCollision, movementChange, pos, collisionBound, movementNumber):
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
    return collisionCheck, newTranslation
  """
    
  #handles moveing down every tick
  def downMovement(self, pos, screenWidth, screenRect):
    pos[1] += self.ySpeed
    bottomYPos = pos[1] + screenRect[3]
    yChange = self.ySpeed
    #makes sure the user isn't clipping inside of the bottom bound
    if bottomYPos >= screenWidth:
          pos[1] = screenWidth - screenRect[3]
          yChange = 0
    return pos[1], yChange
  #handles movement left and right whenever the user presses the respective buttons
  def generalMovement(self, pos, event, screenLength, rectWidth, tileCollision):
    """
    Priorities for collision
    find the right and left bound of the image and then say that the right bound can't exceed the right border, left bound has already been defined and can work though.
    use the get_rect() command to get a rectangle and then add its length for the right wall
    """
    xChange = self.xSpeed
    #gets the bounds that would collide with the settled blocks, commented out as they are only used for the collision check with the settled blocks  
    """for collisions in currentBlockCollision:
      for coords in collisions:
        leftXBounds.append(coords[0])
        rightXBounds.append(coords[0] + coords[2])
        topYBounds.append(coords[1])"""
        
    if event == pygame.K_RIGHT or event == pygame.K_d:
      
      pos[0] += self.xSpeed
      #gets the right side of the rectangle
      rightXPos = rectWidth[2] + pos[0]
      #checks for colliding with the right bound, sets xChange to 0 so that the logic for handling getting a new block can work
      if rightXPos >= screenLength[1]:
        pos[0] = screenLength[1] - rectWidth[2]
        xChange = 0
    #collision for whenever the player moves left
    elif event == pygame.K_LEFT or event == pygame.K_a:
      pos[0] -= self.xSpeed
      #checks for the right bound
      if pos[0] <= screenLength[0]:
        pos[0] = screenLength[0]
        xChange = 0

    return pos[0], xChange
    """
    Try to make something like
    if there's a rectangle in the screen that stretches throughout the thing
    clear out the middle
    translate everything in the dictionary for x positions to be one tile down"""
  #handles displaying the collision tiles for the blocks that have settled, its more useful for when block collision is added
  def settleCollision(self, screen, image, imageRect, pos, blockType):
    #run through every block type and initilaize the respective class
    if blockType == 1 or blockType == 2:
      blockSettle = SB(screen, image, imageRect, blockType)
    elif blockType == 3:
      blockSettle = TB(screen, image, imageRect)
    elif blockType == 4 or blockType == 5:
      blockSettle = CB(screen, image, imageRect, blockType)
    elif blockType == 6:
      blockSettle = UB(screen, image, imageRect)
    else:
      blockSettle = LB(screen, image,imageRect)
      
    #get the collision bounds
    collisionList = blockSettle.collisionBounds(pos)
    return collisionList
  #draw the collision bounds of all the previous blocks that have dropped  
  def lineClear(self, collisionList, screen):
    GRAY = [189,189,189]
    for tiles in collisionList:
      for tileCoordinateList in tiles:
        for cords in tileCoordinateList:
          pygame.draw.rect(screen, GRAY, (cords[0], cords[1], cords[2],cords[3]))