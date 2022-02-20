import pygame
import constants as c

class Gameover(pygame.sprite.Sprite):
  def __init__(self):
    super(Gameover, self).__init__()
    self.font = pygame.font.Font()
    self.color = (0, 250, 0)
    self.message = "GAME OVER"


# button for quit and restart
# font from Min's push


# when player dies, activate gameover
# gameover will bring up 1781.jpg image 