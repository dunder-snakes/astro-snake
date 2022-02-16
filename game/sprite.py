import pygame

class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, width, height, pos):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  
        self.rect = self.image.get_rect(midbottom = pos)

    def inputs(self):
        dist = 5
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            if self.rect.x <= 570:
                self.rect.x += dist

        if key[pygame.K_LEFT]:
            if self.rect.x >= 10:
                self.rect.x -= dist

        if key[pygame.K_UP]:
            if self.rect.y >= 10:
                self.rect.y -= dist

        if key[pygame.K_DOWN]:
            if self.rect.y <= 570:
                self.rect.y += dist

        if key[pygame.K_SPACE]:
            print("pew")


    def update(self):
        self.inputs()


