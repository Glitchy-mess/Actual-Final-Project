#handle the L block here
"""
to determine collision bounds, declare a bunch of rectangles to represent the bounds"""
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class LBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize):
    super().__init__(screen,image, imageRect, tileSize)
  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
      super().tileDraw(repetitions, pos, width, height, sideNumber, xTrans, yTrans)
  def collisionBounds(self, pos):
    width = self.xTile
    height = self.yTile
    verticalCollisionList = []
    horizontalCollisionList = []
    incriment = lambda side, i: side * i
    """
    Define the new collision bounds for this guy instead of just a giant rectangle, you could try making two smaller rectangles that call on general movement
    """
    #the tile used in this case shouldn't matter cause its a 3x3 as a L
    #in other shapes like the canteen block this becomes self.xTile * 2 because its two tiles not 3(at least for height)
    """
    For now i plan on making the bounds a red rectangle that just prove that they exist, but ideally i don't draw them at all but rather store them as just rectangles, probably with coordinates tbh.
    what i can also do is make the settled blocks these rectangles but filled in, they'd be a monochrome color and would render in between the background fill statement and the grid being made
    """
    #vertical bound
    tileIncriment = 0
    for i in range(3):
      tileIncriment = incriment(height, i)
      verticalCollisionTile = (pos[0], pos[1] + tileIncriment, width, height)
      verticalCollisionList.append(verticalCollisionTile)
    
    #horizontal bound
    for i in range(3):
      tileIncriment = incriment(width, i)
      horizontalCollisionTile = (pos[0] + tileIncriment, pos[1] + (2*height), width, height)
      horizontalCollisionList.append(horizontalCollisionTile)

  #might not be necessary because of what i did in main to generalize everythnig
    collisionList = (verticalCollisionList, horizontalCollisionList)
    
    return collisionList
  def settleLogic(self):
    pass