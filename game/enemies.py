import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, height, width, pos):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.y += 1
