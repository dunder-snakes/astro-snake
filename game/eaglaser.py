import pygame
import constants as c

class Eaglaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # self.image = pygame.Surface([4,15])
        # self.image.fill(c.BLUE)
        self.image = pygame.Surface([30,30], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.las_image = pygame.image.load('../assets/orange.png')
        self.enemy_las = pygame.transform.scale(self.las_image,(30,30))
        self.image.blit(self.enemy_las,(0,0))
        self.rect = self.image.get_rect(center = pos)

    def update(self):
        self.rect.y += 3
        if self.rect.y > 600:
            self.kill()