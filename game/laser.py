import pygame
import constants as c

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(c.RED)
        self.image = pygame.Surface([2,15])
        self.image.fill()
        self.rect = self.image.get_rect(center = pos)

    def update(self):
        self.rect.y += -8
        if self.rect.y < 0:
            self.kill()