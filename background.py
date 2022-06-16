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
  return tileSize, tileSize, edgeIntervalScale
    
  