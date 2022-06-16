#handle the T block here
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class TBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize):

    super().__init__(screen,image, imageRect, tileSize)

  def collisionBounds(self, pos):
    width = self.xTile
    height = self.yTile
    incriment = lambda side, i: side * i

    topCollisionList = []
    middleCollisionList = []
    #first rectangle is 3x1
    #xplore having a list of all the tiles that you could collide with and saying that every tile on a specific x line would get deleted if its filled
    #to accomplish this you wanna log everything in a for loop and customize the stuff bc you can't make it one giant rectangle
    for i in range(3):
      tileIncriment = incriment(width,i)
      topCollisionTile = (pos[0] + tileIncriment, pos[1], width, height)
      topCollisionList.append(topCollisionTile)
      

    #second rectangle is 1x3

    for i in range(3):
      tileIncriment = incriment(height,i)
      middleCollisionTile = (pos[0] + width, pos[1] + tileIncriment, width, height)
      middleCollisionList.append(middleCollisionTile)

    collisionList = (topCollisionList, middleCollisionList)
    RED = [255, 0, 0]

    for collisionShapes in collisionList:
      for rect in collisionShapes:
        pygame.draw.rect(self.screen, RED, (rect[0], rect[1], rect[2], rect[3]))
  
    return collisionList

  def settleLogic(self):

    pass
  