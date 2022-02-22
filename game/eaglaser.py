import pygame
import constants as c

class Eaglaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([4,15])
        self.image.fill(c.BLUE)
        self.rect = self.image.get_rect(center = pos)

    def update(self):
        self.rect.y += 3
        if self.rect.y > 600:
            self.kill()