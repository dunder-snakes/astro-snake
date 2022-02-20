import random

#screen
DISPLAY_X = 600
DISPLAY_Y = 600
DISPLAY_SIZE = (DISPLAY_X, DISPLAY_Y)
FPS = 60

#sprite speeds
SNAKE_SPEED = 5
LASER_SPEED = -8

#scoring
POINTS = 1000

#color RGB
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255,0,0)
GREEN = (0,128,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255,215,0)
RANDOM_COLOR = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
