
from BlockHandling.generalBlock import blockMethods as BM
import pygame
#handle the L block/yellow block here
#refer to canteenBlock.py for definitions
class LBlock(BM):
  def __init__(self, screen, image, imageRect):
    super().__init__(screen,image, imageRect)
    
  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
    tileList = super().tileDraw(repetitions, pos, width, height, sideNumber, xTrans, yTrans)
    return tileList
    
  def collisionBounds(self, pos):
    #initialize everything    
    width = self.xTile
    height = self.yTile
    verticalCollisionList = []
    horizontalCollisionList = []
    RED = [255, 0,0]
    collisionList = (None, None)
    #vertical bound of 1x3 tiles
    verticalCollisionList = self.tileDraw(3, pos, width, height, 2 ,0,0)
    
    #horizontal bound of 3x1 tiles
    horizontalCollisionList = self.tileDraw(3,pos,width,height,1,0, 2*height)
    
    collisionList = (verticalCollisionList, horizontalCollisionList)
    
    
    for collisionShapes in collisionList:
      for rect in collisionShapes:
        pygame.draw.rect(self.screen, RED, (rect[0], rect[1], rect[2], rect[3]), 1)
    
    return collisionList
