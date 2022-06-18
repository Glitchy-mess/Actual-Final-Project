#https://pygame.readthedocs.io/en/latest/tiles/tiles.html is the source for the idea of tilesets
import pygame
from random import randrange
#randomizes the block that will be given to the player
def randomizer(screen, scale):
  #takes a random num from 0-6 and takes the appropriate file depending on the result
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
  
  fileRect[2] = scale[1] * 3
  #handles y scaling and makes sure that two tile objects are scaled properly
  if randNum == 3 or randNum == 4 or randNum == 5:
    fileRect[3] = scale[1] * 2
  else:
    fileRect[3] = scale[1] * 3
  #basically scales the file up to the new length and width to fit the grid
  file = pygame.transform.scale(file, (fileRect[2],fileRect[3]))
  newFileRect = file.get_rect()
  return file, newFileRect, randNum
    
    