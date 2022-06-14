#handle the L block here
"""
to determine collision bounds, declare a bunch of rectangles to represent the bounds"""
from BlockHandling import generalBlock as GB
class LBlock(GB.blockMethods):
  def __init__(self, screen, image, imageRect):
    super().__init__(screen,image, imageRect)
  def collisionBounds(self):
    pass
  def settleLogic(self):
    pass