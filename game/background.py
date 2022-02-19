import pygame
from stars import Star
import random
from constants import DISPLAY_SIZE


class Background(pygame.sprite.Sprite):
  def __init__(self):
    super(Background, self).__init__()
    self.image = pygame.Surface(DISPLAY_SIZE)
    self.color = (0, 0, 0)
    self.image.fill(self.color)
    self.rect = self.image.get_rect()
    self.stars = pygame.sprite.Group()
    self.timer = random.randrange(1, 10)


# while the game loops, timer decreases and a new star is added when it hits zero
  def update(self):
    self.star.update()
    if self.timer == 0:
        new_star = Star()
        self.stars.add(new_star)
        self.timer = random.randrange(1, 10)
    self.image.fill(self.color)
    self.stars.draw(self.image)
    self.timer -= 1

# self.image.fill(self.color) will fill the background color every frame so stars do not overlap each other

# self.stars.draw(self.image) will draw the background surface which is self.image in the init