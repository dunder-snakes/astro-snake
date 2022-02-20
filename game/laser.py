import pygame
import constants as c

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image.fill(c.GREEN)
        self.rect = self.image.get_rect(center = pos)

    def update(self):
        self.rect.y += -8
        if self.rect.y < 0:
            self.kill()