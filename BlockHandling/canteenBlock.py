#Handle both canteen blocks here
from BlockHandling.generalBlock import blockMethods as BM
import pygame
#inherits the abstract class block methods to make collision bounds
#handls the canteen blocks/red and orange blocks here
class CBlock(BM):
  def __init__(self, screen, image, imageRect, blockType):

    super().__init__(screen,image, imageRect)
    self.blockType = blockType
    
  #runs through a general function that returns all of the rectangles required for an image, a little clunky in my opinion but it serves its purpose quite well
  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
    tileList = super().tileDraw(repetitions, pos, width, height, sideNumber, xTrans, yTrans)
    return tileList
    
  #makes the collision bounds for the block
  def collisionBounds(self, pos):
    #initialize everything
    #makes sure that there's only 2 tiles for height
    height = self.yTile * 3/2
    RED = [255, 0, 0]
    width = self.xTile
    topCollisionList = []
    bottomCollisionList = []
    collisionList = (None, None)
    
    #checks to see if we're dealing with the red or orange block
    
    if self.blockType == 4:
      #top bound of 2x1 tiles
      topCollisionList = self.tileDraw(2, pos, width, height, 1, width, 0)

      #bottom bound of 3x1 tiles
      bottomCollisionList = self.tileDraw(3, pos, width, height, 1, 0, height)
      
    else:
      #top bound of 3x1 
      topCollisionList = self.tileDraw(3, pos, width, height, 1, 0,0)
      #bottom bound of 2x1
      bottomCollisionList = self.tileDraw(2, pos, width, height, 1, 0, height)

    #initializes the tiles that can be collided with onto a list
    collisionList = (topCollisionList, bottomCollisionList)    
    #draws the collision bounds for the tiles in the object
    for collisionShapes in collisionList:
      for rect in collisionShapes:
        pygame.draw.rect(self.screen, RED, (rect[0], rect[1], rect[2], rect[3]), 1)
        
    return collisionList
  