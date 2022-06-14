"""
Make an abstract class for all of the blocks so that they can collide with each other and fall down the screen


"""
import pygame
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
    
    print(bottomYPos, yPos, screenWidth, self.ySpeed)
    if bottomYPos >= screenWidth:
      yPos = screenWidth - screenRect[3]
    return yPos
    
  def generalMovement(self, xPos, event, screenLength, rectWidth):
    #try handling all of the movement here?
    """
    Priorities for collision
    find the right and left bound of the image and then say that the right bound can't exceed the funny thing, left bound has already been defined and can work though. prob just use the get_rect() command to get a rectangle and then add its length for the right wall
    """
    if event == pygame.K_RIGHT or event == pygame.K_d:
      #also position is going to be a tuple
      xPos += self.xSpeed
      rightXPos = rectWidth[2] + xPos
      if rightXPos >= screenLength[1]:
        xPos = screenLength[1] - rectWidth[2]
      
    elif event == pygame.K_LEFT or event == pygame.K_a:
      xPos -= self.xSpeed
      if xPos <= screenLength[0]:
        xPos = screenLength[0]
    return xPos
      #find a way to get the lower bounds
    #also make a check to see if the player is holding down left or right, if so then don't drop the block yet
  def lineClear(self, screen):
    pass
    """
    Try to make something like
    if there's a rectangle in the screen that stretches throughout the thing
    clear out the middle
    translate everything in the dictionary for x positions to be one tile down"""
    
