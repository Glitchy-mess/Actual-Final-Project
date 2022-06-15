#handle the u block
from BlockHandling.generalBlock import blockMethods as BM

class UBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize):

    super().__init__(screen,image, imageRect)

    self.tileSize = tileSize

  def collisionBounds(self, pos):

    height = 0

    width = 0

    height = width = self.xTile *3 

    #vertical bound

    verticalCollision = (pos[0],pos[1], self.xTile, height)

    #horizontal bound

    horizontalCollision = (pos[0],pos[1]+(2*self.xTile),width, self.yTile)

    return verticalCollision, horizontalCollision

  def settleLogic(self):

    pass
  