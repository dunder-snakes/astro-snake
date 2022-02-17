import pygame
from laser import Laser

class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, width, height, pos):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.loaded = True
        self.recharge_time = 0
        self.laser = pygame.sprite.Group()
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
                
        if key[pygame.K_SPACE] & self.loaded:
            self.fire()
            


    def fire(self):
        self.laser.add(Laser(self.rect.center))
        self.loaded = False
        self.recharge_time = pygame.time.get_ticks()
    
    def recharge(self):
        if pygame.time.get_ticks() - self.recharge_time > 250:
            self.loaded = True

    def update(self):
        self.inputs()
        self.recharge()
        self.laser.update()


