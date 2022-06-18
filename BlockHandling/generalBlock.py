#make the general block logic here

from abc import ABC, abstractmethod
#abstract class that every block class inherits from for functions
class blockMethods(ABC):
  @abstractmethod
  def __init__(self,screen, image, imageRect):
    #initialize the spritesheet
    self.screen = screen
    #loads and stores the image as a variable
    self.image = image
    self.imageRect = imageRect
    #acts as a generalization of the image as most of the images are 3x3
    self.xTile = self.imageRect[2]/3
    self.yTile = self.imageRect[3]/3
        
  #makes an abstract method to ensure that classes actually make a collision bound method
  @abstractmethod
  def collisionBounds(self):
    pass

  #acts as the abstract method for drawing tiles, and returns a list of all of the tiles that are in the block for collision purposes
  @abstractmethod
  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
    tileList = []
    incriment = lambda side, i: side*i
    
    #acts as the width incriments
    if sideNumber == 1:
      for i in range(repetitions):
        tileIncriment = incriment(width, i)
        tile = (pos[0] + xTrans + tileIncriment, pos[1] + yTrans,width, height)
        tileList.append(tile)
    #acts as the height incriments
    else:
      for i in range(repetitions):
        tileIncriment = incriment(height, i)
        tile = (pos[0] + xTrans, pos[1] + yTrans + tileIncriment, width, height)
        tileList.append(tile)
    return tileList
#credits to https://pygame.readthedocs.io/en/latest/3_image/image.html for some of the ideas 