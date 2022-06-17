

#https://pygame.readthedocs.io/en/latest/tiles/tiles.html is the source for tilesets
#randomizer would have to pick randomly from the different types of blocks that you can pick
import pygame
from random import randrange
def randomizer(screen, scale):
  randNum = randrange(7)
  if randNum == 0:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/blueBlock.png")
  elif randNum == 1:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/limeBlock.png")
  elif randNum == 2:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/cyanBlock.png")
  elif randNum == 3:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/orangeBlock.png")
  elif randNum == 4:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/redBlock.png")
  elif randNum == 5:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/purpleBlock.png")
  else:
    file = pygame.image.load("/home/runner/Final-project/BlockHandling/new sprites/yellowBlock.png")
    #make sure to use this command to get collision bounds
  fileRect = file.get_rect()
  #handles x scaling, dunno why 2 works but it does so let's go with that
  #try making this dynamic so that you can support any resolution
  print(scale)
  fileRect[2] = scale[1] * 3
  #handles y scaling
  if randNum == 3 or randNum == 4 or randNum == 5:
    fileRect[3] = scale[1] * 2
  else:
    fileRect[3] = scale[1] * 3
  #nasocally scales the file up to the new length and width to fit the grid
  file = pygame.transform.scale(file,( fileRect[2],fileRect[3]))
  newFileRect = file.get_rect()
  return file, newFileRect, randNum
    
    