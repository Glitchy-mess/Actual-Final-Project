#Handle both canteen blocks here
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class CBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize, blockType):

    super().__init__(screen,image, imageRect, tileSize)
    self.blockType = blockType
  def collisionBounds(self, pos):

    #acts as the 1x3 rectangle
    #acts as the 1x2 rectangle
    #use 3/2 because y is segmented into two sections and so you need the halfway point
    #nvm this did not help but at least it makes the red block convineant
    height = self.yTile * 3/2
    width = self.xTile 
    topCollisionList = []
    bottomCollisionList = []
    incriment = lambda side, i: side * (i)
    #Two bounds

    
    if self.blockType == 4:
      #topCollision = (pos[0] + self.xTile, pos[1], width, height)
      for i in range(1,3):
        tileIncriment = incriment(width, i)
        topCollisionTile = (pos[0] + tileIncriment, pos[1], width, height)
        topCollisionList.append(topCollisionTile)
      
      #bottomCollision = (pos[0],pos[1] + height, width, height)
      for i in range(3):
        tileIncriment = incriment(width, i)
        bottomCollisionTile = (pos[0] + tileIncriment, pos[1] + height, width, height)
        bottomCollisionList.append(bottomCollisionTile)
    else:
      #topCollision = (pos[0],pos[1], width1, height2)
      for i in range(3):
        tileIncriment = incriment(width, i)
        topCollisionTile = (pos[0] + tileIncriment, pos[1], width, height)
        topCollisionList.append(topCollisionTile)
        
      #bottomCollision = (pos[0], pos[1] + height2, width2, height2)
      for i in range(2):
        tileIncriment = incriment(width, i)
        bottomCollisionTile = (pos[0] + tileIncriment, pos[1] + height, width, height)
        bottomCollisionList.append(bottomCollisionTile)
    collisionList = (topCollisionList, bottomCollisionList)

    return collisionList

  def settleLogic(self):
    pass
  