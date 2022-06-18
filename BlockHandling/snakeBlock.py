
from BlockHandling.generalBlock import blockMethods as BM
import pygame
#handles the snake blocks/lime and blue block
#refer to canteenBlock.py for definitions
class SBlock(BM):
  def __init__(self, screen, image, imageRect, blockType):

    super().__init__(screen,image, imageRect)
    self.blockType = blockType


  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
    tileList = super().tileDraw(repetitions, pos, width, height, sideNumber, xTrans, yTrans)
    return tileList

  def collisionBounds(self, pos):
    #initialize everything
    topCollisionList = []
    middleCollisionList = []
    bottomCollisionList = []
    width = self.xTile
    height = self.yTile
    RED = [255, 0, 0]
    collisionList = (None, None, None)

    #make top and bottom bounds of 2x1 tiles, they'll just be translated differently
    if self.blockType == 1:
      #make sure to actually translate everything properly when copying down values cause otherwise it gets odd 
      topCollisionList = self.tileDraw(2, pos, width, height, 1, width, 0)


      bottomCollisionList = self.tileDraw(2, pos, width, height, 1, 0, height*2)

    
    else:   
      topCollisionList = self.tileDraw(2, pos, width, height, 1, 0, 0)

      bottomCollisionList = self.tileDraw(2, pos, width, height, 1, width, height*2)
    

    #middle bound of 1 tile
    middleCollisionList = self.tileDraw(1, pos, width, height, 1, width, height)

  
    collisionList = (topCollisionList, middleCollisionList, bottomCollisionList)

    for collisionShapes in collisionList:
      for rect in collisionShapes:
        pygame.draw.rect(self.screen, RED, (rect[0], rect[1], rect[2], rect[3]), 1)
  
    return collisionList

  