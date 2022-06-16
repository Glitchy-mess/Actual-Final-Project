#handle both snake blcoks here
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class SBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize, blockType):

    super().__init__(screen,image, imageRect, tileSize)
    self.blockType = blockType

  def collisionBounds(self, pos):
    """
    TODO TOMORROW
    FIX UP THIS AND UBLOCK SO THAT IT MATCHES THE OTHER BLOCKS
    DUMP ALL OF THE TILES INTO MAIN
    USE TILES TO CHECK FOR COLLISION
    HOPEFULLY YOU CAN ALSO DO A BIT OF TROLLING BY CLEARING LINES, DRAW THE STORED TILES AT LEAST THO
    """

    #divide this into 3 blocks
    height = self.yTile
    #top line
    width1 = self.xTile*2
    #middle line
    width2 = self.xTile
    #bottom line
    width3 = self.xTile*2
    print(self.blockType)
    if self.blockType == 1:
      #make sure to actually translate everything properly when copying down values cause otherwise it gets odd
      topCollision = (pos[0] + self.xTile, pos[1], width3, height)
      bottomCollision = (pos[0], pos[1] + (height*2), width1, height)
    else: 
      #top bound
      topCollision = (pos[0], pos[1], width1, height)
      #bottom bound
      bottomCollision = (pos[0] + self.xTile, pos[1] + (height*2), width3, height)
      

    
    middleCollision = (pos[0] + self.xTile, pos[1] + height, width2, height)
    collisionList = (topCollision, middleCollision, bottomCollision)
    return collisionList

  def settleLogic(self):

    pass
  