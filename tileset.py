

#https://pygame.readthedocs.io/en/latest/tiles/tiles.html is the source for tilesets
#randomizer would have to pick randomly from the different types of blocks that you can pick
import pygame
from random import randrange
def randomizer(screen, scale):
  randNum = randrange(7)
  #randNum = 6
  if randNum == 0:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/blueBlock.png")
  elif randNum == 1:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/cyanBlock.png")
  elif randNum == 2:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/limeBlock.png")
  elif randNum == 3:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/orangeBlock.png")
  elif randNum == 4:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/purpleBlock.png")
  elif randNum == 5:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/redBlock.png")
  else:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/yellowBlock.png")
    #make sure to use this command to get collision bounds
  fileRect = file.get_rect()
  #handles x scaling, dunno why 2 works but it does so let's go with that
  fileRect[2] *= 2
  #handles y scaling
  fileRect[3] *= 2
  #nasocally scales the file up to the new length and width to fit the grid
  file = pygame.transform.scale(file,( fileRect[2],fileRect[3]))
  newFileRect = file.get_rect()
  return file, newFileRect
    
    