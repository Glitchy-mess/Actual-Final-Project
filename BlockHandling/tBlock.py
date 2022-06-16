#handle the T block here
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class TBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize):

    super().__init__(screen,image, imageRect, tileSize)
  
  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
    tileList = super().tileDraw(repetitions, pos, width, height, sideNumber, xTrans, yTrans)
    return tileList
    

  def collisionBounds(self, pos):
    width = self.xTile
    height = self.yTile

    topCollisionList = []
    middleCollisionList = []
    #first rectangle is 3x1
    #xplore having a list of all the tiles that you could collide with and saying that every tile on a specific x line would get deleted if its filled
    #to accomplish this you wanna log everything in a for loop and customize the stuff bc you can't make it one giant rectangle
    #3x1 rect at the top
    topCollisionList = self.tileDraw(3, pos, width, height, 1, 0, 0)

    #1x3 rectangle in the middle of the screen
    middleCollisionList = self.tileDraw(3, pos, width, height, 2, width, 0)
      

    #second rectangle is 1x3


    collisionList = (topCollisionList, middleCollisionList)
    RED = [255, 0, 0]

    for collisionShapes in collisionList:
      for rect in collisionShapes:
        pygame.draw.rect(self.screen, RED, (rect[0], rect[1], rect[2], rect[3]), 1)
  
    return collisionList

  def settleLogic(self):

    pass
  