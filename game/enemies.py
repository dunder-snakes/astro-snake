import pygame
import random
import constants as c

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([50, 50], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.en_image = pygame.image.load("../assets/mongoose.png")
        self.enemy = pygame.transform.scale(self.en_image,(50, 50))
        self.image.blit(self.enemy,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_X-self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randrange(1, 5)



    def update(self):
        self.rect.y += self.speed
        if self.rect.y > c.DISPLAY_Y + self.rect.y:
            self.kill()
