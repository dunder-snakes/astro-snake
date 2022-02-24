import pygame
import random
import constants as c

class Power(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([15, 15])
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_X-self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 5

    def update(self):
        self.color_changer()
        self.rect.y += self.speed
        if self.rect.y > c.DISPLAY_Y + self.rect.y:
            self.kill()

    def color_changer(self):
        self.image.fill((random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)))