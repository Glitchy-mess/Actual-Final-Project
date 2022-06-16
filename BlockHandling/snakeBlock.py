#handle both snake blcoks here
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class SBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize, blockType):

    super().__init__(screen,image, imageRect, tileSize)
    self.blockType = blockType


  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
    tileList = super().tileDraw(repetitions, pos, width, height, sideNumber, xTrans, yTrans)
    return tileList

  def collisionBounds(self, pos):

    topCollisionList = []
    middleCollisionList = []
    bottomCollisionList = []
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
    #middle line
    #bottom line
    width = self.xTile
    height = self.yTile
    if self.blockType == 1:
      #make sure to actually translate everything properly when copying down values cause otherwise it gets odd
      topCollisionList = self.tileDraw(2, pos, width, height, 1, width, 0)
      bottomCollisionList = self.tileDraw(2, pos, width, height, 1, 0, height*2)
      """for i in range(1,3):
        tileIncriment = incriment(width, i)
        topCollisionTile = (pos[0] + tileIncriment, pos[1], width, height)
        topCollisionList.append(topCollisionTile)"""

      """for i in range(2):
        tileIncriment = incriment(width, i)
        bottomCollisionTile = (pos[0] + tileIncriment, pos[1], width, height)
        bottomCollisionList.append(bottomCollisionTile)"""
    
    else:
      #top bound      
      topCollisionList = self.tileDraw(2, pos, width, height, 1, 0, 0)
      #bottom bound
      bottomCollisionList = self.tileDraw(2, pos, width, height, 1, width, height*2)
    
      

    middleCollisionList = self.tileDraw(1, pos, width, height, 1, width, height)
    #middleCollision = (pos[0] + self.xTile, pos[1] + height, width2, height)
  
    collisionList = (topCollisionList, middleCollisionList, bottomCollisionList)
    RED = [255, 0, 0]

    for collisionShapes in collisionList:
      for rect in collisionShapes:
        pygame.draw.rect(self.screen, RED, (rect[0], rect[1], rect[2], rect[3]), 1)
  
    return collisionList

  def settleLogic(self):

    pass
  