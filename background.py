import pygame
"""
Figure out how to draw a grid that can stay to scale w/the tiles
"""
def backgroundDraw(screenSize, screen):
  intervalNum = 32
  height = 2
  yinterval = screenSize[1]/ intervalNum
  xInterval = screenSize[0]/ intervalNum
  yVal = 0
  xVal = 0
  scale = 60
  tileSize = screenSize[0]/28

  GRAY = [scale] * 3
  #screen.fill(GRAY)
  LGRAY = [scale+90] * 3
  BORDERBLACK = [5]*3
  for i in range(intervalNum):
    #draw the grid
    pygame.draw.rect(screen, GRAY, (0, yVal, screenSize[0], height))
    pygame.draw.rect(screen,GRAY, (xVal, 0, height, screenSize[1]))
    #draw the border
  
    pygame.draw.rect(screen, BORDERBLACK, (0, yVal, screenSize[0], 10), 1)
    pygame.draw.rect(screen,BORDERBLACK, (xVal, 0, 10, screenSize[1]), 1)
    
    yVal += yinterval
    xVal += xInterval
  #override the edges to make a border around the screen
  edgeIntervalScale = intervalNum // 1.5
  edgeXVal = (0, screenSize[0] - edgeIntervalScale)
  #draws left, right and bottom respectively
  pygame.draw.rect(screen, LGRAY, (edgeXVal[0], 0, edgeIntervalScale, screenSize[1]))
  pygame.draw.rect(screen, LGRAY, (edgeXVal[1], 0, edgeIntervalScale, screenSize[1]))
  pygame.draw.rect(screen, LGRAY, (0, screenSize[1] - edgeIntervalScale, screenSize[0], edgeIntervalScale))
  #fix this to only be two values
  return tileSize, edgeIntervalScale

#draws the instructions for the player 
def textDraw(screen, edgeIntervalScale):
  GRAY = [200,200,200]
  #credits to https://www.geeksforgeeks.org/python-display-text-to-pygame-window/ for being better at documenting how font rendering works than the actual documentation
  #sysfont grabs a font from the system, beats me why its not the same as the general font command
  font = pygame.font.SysFont("arial", 14)
  text = font.render("Press A or D to move left or right respectively; Arrow keys work as well for this", True, GRAY)
  pygame.Surface.blit(screen, text, [edgeIntervalScale,40])