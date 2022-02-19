import pygame

class Eagles(pygame.sprite.Sprite):
    def __init__(self, width, height,pos):
        super().__init__()

        self.image = pygame.Surface([width, height], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.en_image = pygame.image.load("mongoose.png")
        self.enemy = pygame.transform.scale(self.en_image,(width, height))
        self.image.blit(self.enemy,(0,0))

        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.y += 1 