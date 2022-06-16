#make the general block logic here
import pygame
from abc import ABC, abstractmethod
class blockMethods(ABC):
  @abstractmethod
  def __init__(self,screen, image, imageRect, tileSize):
    #initialize the spritesheet
    self.screen = screen
    #loads and stores the image as a variable
    self.image = image
    self.imageRect = imageRect
    self.xTile = self.imageRect[2]/3
    self.yTile = self.imageRect[3]/3
    self.tileSize = tileSize
    #self.imageBound = pygame.get_rect(self.image)
        
    
  @abstractmethod
  def collisionBounds(self):
    pass
    #gonna be looking at 2-3 rectangles for the collision, they are going to be 10x10 pixels
    """
    What if i were to make 2-3 rectangles for collision and then input their height and width which then get combined to make the things 
    rectangleParams1, rectangleParams2, rectangleParams3 = None)
    nah it wont' work for generalizing everything
    """

  @abstractmethod
  def settleLogic(self):
    pass

  @abstractmethod
  def tileDraw(self, repetitions, pos, width, height, sideNumber, xTrans, yTrans):
    tileList = []
    incriment = lambda side, i: side*i
    if sideNumber == 1:
      for i in range(repetitions):
        tileIncriment = incriment(width, i)
        tile = (pos[0] + xTrans + tileIncriment, pos[1] + yTrans,width, height)
        tileList.append(tile)
    else:
      for i in range(repetitions):
        tileIncriment = incriment(height, i)
        tile = (pos[0] + xTrans, pos[1] + yTrans + tileIncriment, width, height)
        tileList.append(tile)
    return tileList
  
    """
    To get the individual images we would need to make an interval of 32 pixels and then send those blocks over to the block classes, because at this point they need their own classes to handle collision
    """ #https://pygame.readthedocs.io/en/latest/3_image/image.html
    
    #try saying something like 
    """
    find a way to log all of the black pixels and base the collision around that
    block width = could be 3 or 2, honestly you could just declare it as you call the block because it's well defined
    block length is the max of the bottom and top lengths
    solved this by just not giving a crap about the black pixels or whatever, and instead just slicing the image into a grid
    """
  