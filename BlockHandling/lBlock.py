#handle the L block here
"""
to determine collision bounds, declare a bunch of rectangles to represent the bounds"""
from BlockHandling import generalBlock as GB
class LBlock(GB.blockMethods):
  def __init__(self, screen, image, imageRect, tileSize):
    super().__init__(screen,image, imageRect)
    self.tileSize = tileSize
  
  def collisionBounds(self):
    """
    Define the new collision bounds for this guy instead of just a giant rectangle, you could try making two smaller rectangles that call on general movement
    """
    tile = imageRect/tileSize
    height = 0
    width = 0
    verticalCollision = []
    horizontalCollision = []
    #vertical bound
    for i in range(3):
      verticalCollision.append(pygame.draw.rect(0,height,tileSize, tileSize))
      height += tile
    #horizontal bound
    for i in range(3):
      horizontalCollision.append(pygame.draw.rect(width, self.imageRect - tileSize, tileSize, tileSize))
      width += tileSize
  def settleLogic(self):
    pass