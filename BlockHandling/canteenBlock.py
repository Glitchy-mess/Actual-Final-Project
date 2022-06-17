#Handle both canteen blocks here
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class CBlock(BM):
  def __init__(self, screen, image, imageRect, blockType):

    super().__init__(screen,image, imageRect)
    self.blockType = blockType
    
  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
    tileList = super().tileDraw(repetitions, pos, width, height, sideNumber, xTrans, yTrans)
    return tileList
    
  def collisionBounds(self, pos):
    
    #acts as the 1x2 rectangle
    height = self.yTile * 3/2
    #acts as the 1x3 rectangle
    width = self.xTile 


    #checks to see if we're dealign with the red or orange block
    if self.blockType == 4:
      topCollisionList = self.tileDraw(2, pos, width, height, 1, width, 0)
      bottomCollisionList = self.tileDraw(3, pos, width, height, 1, 0, height)
      

    else:

      topCollisionList = self.tileDraw(3, pos, width, height, 1, 0,0)
      bottomCollisionList = self.tileDraw(2, pos, width, height, 1, 0, height)

    #initializes the tiles that can be collided with onto a list
    collisionList = (topCollisionList, bottomCollisionList)
    RED = [255, 0, 0]
    #draws the collision bounds for the tile
    for collisionShapes in collisionList:
      for rect in collisionShapes:
        pygame.draw.rect(self.screen, RED, (rect[0], rect[1], rect[2], rect[3]), 1)
    return collisionList
  