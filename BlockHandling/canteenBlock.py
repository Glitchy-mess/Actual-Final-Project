#Handle both canteen blocks here
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class CBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize, blockType):

    super().__init__(screen,image, imageRect, tileSize)
    self.blockType = blockType
    
  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
    tileList = super().tileDraw(repetitions, pos, width, height, sideNumber, xTrans, yTrans)
    return tileList
    
  def collisionBounds(self, pos):

    #acts as the 1x3 rectangle
    #acts as the 1x2 rectangle
    #use 3/2 because y is segmented into two sections and so you need the halfway point
    #nvm this did not help but at least it makes the red block convineant
    height = self.yTile * 3/2
    width = self.xTile 


    #Two bounds

    
    if self.blockType == 4:
      topCollisionList = self.tileDraw(2, pos, width, height, 1, width, 0)
      bottomCollisionList = self.tileDraw(3, pos, width, height, 1, 0, height)
      

    else:

      topCollisionList = self.tileDraw(3, pos, width, height, 1, 0,0)
      bottomCollisionList = self.tileDraw(2, pos, width, height, 1, 0, height)
        
      #bottomCollision = (pos[0], pos[1] + height2, width2, height2)
    collisionList = (topCollisionList, bottomCollisionList)
    RED = [255, 0, 0]

    for collisionShapes in collisionList:
      for rect in collisionShapes:
        pygame.draw.rect(self.screen, RED, (rect[0], rect[1], rect[2], rect[3]), 1)

    return collisionList

  def settleLogic(self):
    pass
  