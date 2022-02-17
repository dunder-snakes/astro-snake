import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, height, width, pos):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect(midbottom=pos)
