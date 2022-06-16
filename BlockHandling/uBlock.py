#handle the u block
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class UBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize):

    super().__init__(screen,image, imageRect, tileSize)


  def collisionBounds(self, pos):
    width = self.xTile *3 
    height = self.yTile *3/2

    #this block is :sparkles: special :sparkles: because it has that gap in the middle, so make two rectangles to account for that
    #rectangles respectively handle the 1st and 2nd rectangle in the top layer
    topCollision1 = (pos[0], pos[1], self.xTile, height) 
    topCollision2 = (pos[0] + (self.xTile*2), pos[1], self.xTile, height)
    #forms a 3x1 rect
    bottomCollision = (pos[0], pos[1] + height, width, height)
    collisionList = (topCollision1, topCollision2, bottomCollision)
    RED = [255, 0, 0]

    for rect in collisionList:
      pygame.draw.rect(self.screen, RED, (rect[0], rect[1], rect[2], rect[3]))
    return collisionList

  def settleLogic(self):

    pass
  