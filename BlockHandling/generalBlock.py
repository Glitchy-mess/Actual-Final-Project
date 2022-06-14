#make the general block logic here
import pygame
from abc import ABC, abstractmethod
class blockMethods(ABC):
  @abstractmethod
  def __init__(self,screen, image, imageRect):
    #initialize the spritesheet
    self.screen = screen
    #loads and stores the image as a variable
    self.image = image
    self.imageRect = imageRect
    #self.imageBound = pygame.get_rect(self.image)
        
    
  @abstractmethod
  def collisionBounds(self):
    #gonna be looking at 2-3 rectangles for the collision, they are going to be 10x10 pixels
    pass

  @abstractmethod
  def settleLogic(self):
    pass


  

    
    """
    To get the individual images we would need to make an interval of 32 pixels and then send those blocks over to the block classes, because at this point they need their own classes to handle collision
    """ #https://pygame.readthedocs.io/en/latest/3_image/image.html
    
    #try saying something like 
    """
    find a way to log all of the black pixels and base the collision around that
    block width = could be 3 or 2, honestly you could just declare it as you call the block because it's well defined
    block length is the max of the bottom and top lengths
    
    """
  