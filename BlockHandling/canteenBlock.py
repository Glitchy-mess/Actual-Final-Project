#Handle both canteen blocks here
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class CBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize, blockType):

    super().__init__(screen,image, imageRect, tileSize)
    self.blockType = blockType
  def collisionBounds(self, pos):

    #acts as the 1x3 rectangle
    width1 = self.xTile*3
    #acts as the 1x2 rectangle
    #use 3/2 because y is segmented into two sections and so you need the halfway point
    #nvm this did not help but at least it makes the red block convineant
    height2 = self.yTile * 3/2
    width2 = self.xTile * 2

    #Two bounds

    
    if self.blockType == 4:
      topCollision = (pos[0] + self.xTile, pos[1], width2, height2)
      bottomCollision = (pos[0],pos[1] + height2, width1, height2)
    else:
      topCollision = (pos[0],pos[1], width1, height2)
      bottomCollision = (pos[0], pos[1] + height2, width2, height2)

    return topCollision, bottomCollision

  def settleLogic(self):
    pass
  