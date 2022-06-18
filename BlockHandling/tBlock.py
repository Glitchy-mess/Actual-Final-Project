#handle the T block here
from BlockHandling.generalBlock import blockMethods as BM
import pygame
#handle the t block/cyan block
#refer to canteenBlock.py for definitions
class TBlock(BM):
  def __init__(self, screen, image, imageRect):

    super().__init__(screen,image, imageRect)

  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
    
    tileList = super().tileDraw(repetitions, pos, width, height, sideNumber, xTrans, yTrans)
    return tileList

  def collisionBounds(self, pos):
    width = self.xTile
    height = self.yTile
    collisionList = (None, None)
    RED = [255, 0, 0]
    topCollisionList = []
    middleCollisionList = []
    #3x1 rect at the top
    topCollisionList = self.tileDraw(3, pos, width, height, 1, 0, 0)

    #1x3 rectangle in the middle of the screen
    middleCollisionList = self.tileDraw(3, pos, width, height, 2, width, 0)

    collisionList = (topCollisionList, middleCollisionList)

    for collisionShapes in collisionList:
      for rect in collisionShapes:

        pygame.draw.rect(self.screen, RED, (rect[0], rect[1], rect[2], rect[3]), 1)
  
    return collisionList
