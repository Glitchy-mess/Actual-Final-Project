#handle the u block
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class UBlock(BM):
  def __init__(self, screen, image, imageRect):

    super().__init__(screen,image, imageRect)

  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
    tileList = super().tileDraw(repetitions, pos, width, height, sideNumber, xTrans, yTrans)
    return tileList
    
  def collisionBounds(self, pos):
    #forms a 3x1 rect
    width = self.xTile
    height = self.yTile * 3/2

    #this block is :sparkles: special :sparkles: because it has that gap in the middle, so make two rectangles to account for that
    #rectangles respectively handle the 1st and 2nd rectangle in the top layer
    topCollisionList1 = self.tileDraw(1, pos, width, height, 1, 0,0)
    
    topCollisionList2 = self.tileDraw(1,pos,width,height,1, width*2, 0)
    
    bottomCollisionList = self.tileDraw(3, pos, width, height, 1, 0, height)
    collisionList = (topCollisionList1, topCollisionList2, bottomCollisionList)
    
    RED = [255, 0, 0]
    #same documentation as 
    for rect in collisionList:
      for i in rect:
        pygame.draw.rect(self.screen, RED, (i[0], i[1], i[2], i[3]), 1)
    return collisionList
