import pygame
import random
import constants as c


class Star(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()

    self.width = random.randrange(1, 4)
    self.height = self.width
    self.image = pygame.Surface((self.width, self.height))
    self.image.fill((255,255,255))
    self.rect = self.image.get_rect()
    self.rect.x = random.randrange(0, c.DISPLAY_X - self.rect.width)
    self.rect.y = self.rect.height
# play with this tuple to set speed of stars
    self.velocity_y = random.randrange(4, 22)

# updates every frame
  def update(self):
    self.rect.y += self.velocity_y
    if self.rect.y < 0 - self.rect.y:
      self.kill()