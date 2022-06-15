#handle both snake blcoks here
from BlockHandling.generalBlock import blockMethods as BM
class SBlock(BM):
  def __init__(self, screen, image, imageRect, tileSize):

    super().__init__(screen,image, imageRect)

    self.tileSize = tileSize

  def collisionBounds(self, pos, blockType):

    #divide this into 3 blocks
    height = self.yTile
    #top line
    width1 = self.xTile*2
    #middle line
    width2 = self.xTile
    #bottom line
    width3 = self.xTile*2
    if blockType == 1:
      
      #top bound
      topCollision = (pos[0], pos[1], width1, height)
      #middle bound
      #bottom bound
      bottomCollision = (pos[0] + self.xTile, pos[1] + (height*2), width3, height)
    else:
      topCollision = (pos[0] + self.xTile, pos[1] + (height*2), width3, height)
      bottomCollision = (pos[0], pos[1], width1, height)

    
    middleCollision = (pos[0] + self.xTile, pos[1] + height, width2, height)
    
    
    return topCollision, middleCollision, bottomCollision

  def settleLogic(self):

    pass
  