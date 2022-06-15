#handle the L block here
"""
to determine collision bounds, declare a bunch of rectangles to represent the bounds"""
from BlockHandling.generalBlock import blockMethods as BM
import pygame
class LBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize):
    super().__init__(screen,image, imageRect, tileSize)
  
  def collisionBounds(self, pos):
    """
    Define the new collision bounds for this guy instead of just a giant rectangle, you could try making two smaller rectangles that call on general movement
    """

    height = 0
    width = 0

    #the tile used in this case shouldn't matter cause its a 3x3 as a L
    #in other shapes like the canteen block this becomes self.xTile * 2 because its two tiles not 3(at least for height)
    height = width = self.xTile *3 
    """
    For now i plan on making the bounds a red rectangle that just prove that they exist, but ideally i don't draw them at all but rather store them as just rectangles, probably with coordinates tbh.
    what i can also do is make the settled blocks these rectangles but filled in, they'd be a monochrome color and would render in between the background fill statement and the grid being made
    """
    #vertical bound
    verticalCollision = (pos[0],pos[1], self.xTile, height)
    #horizontal bound
    horizontalCollision = (pos[0],pos[1]+(2*self.xTile),width, self.yTile)
  #might not be necessary because of what i did in main to generalize everythnig
    return verticalCollision, horizontalCollision
  def settleLogic(self):
    pass