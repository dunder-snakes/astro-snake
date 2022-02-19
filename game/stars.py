import pygame
import random
from constants import DISPLAY_Y


class Star(pygame.sprite.Sprite):
  def __init__(self):
    super(Star, self).__init__()

    self.width = random.randrange(1, 4)
    self.height = self.width
    self.image = pygame.Surface((self.width, self.height))
    self.color = (255, 255, 255)
    self.image.fill(self.color)
    self.rect = self.image.get_rect()
    self.rect.x = random.randrange(0, DISPLAY_Y)
    self.velocity_x = 0
# play with this tuple to set speed of stars
    self.velocity_y = random.randrange(4, 22)

# updates every frame
  def update(self):
# updates position, each frame takes the coordinate and adds the star's velocity
    self.rect.x += self.velocity_x
    self.rect.y += self.velocity_y