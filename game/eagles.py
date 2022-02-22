import pygame
import random
import constants as c
from eaglaser import Eaglaser

class Eagles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([150, 150], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()

        self.en_image = pygame.image.load('../assets/pngegg.png')
        self.enemy = pygame.transform.scale(self.en_image,(150, 150))

        self.image.blit(self.enemy,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_X-self.rect.width)
        self.rect.y = 10
        self.speed_x = 5
        self.edge = True
        self.loaded = True
        self.eg_laser = pygame.sprite.Group()
        self.recharge_time = 0

    def enemy_fire(self):
        self.eg_laser.add(Eaglaser(self.rect.midbottom))
        self.loaded = False
        self.recharge_time = pygame.time.get_ticks()

    # def blitRotateCenter(surf, image, topleft, angle):
    #     rotated_image = pygame.transform.rotate(image, angle)
    #     new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    #     surf.blit(rotated_image, new_rect.topleft)
    
    def recharge(self):
        if pygame.time.get_ticks() - self.recharge_time > 750:
            self.loaded = True

    def update(self):
        self.eg_laser.update()
        if self.loaded:
            self.enemy_fire()
        if self.loaded is False:
            self.recharge()
        if self.rect.x < 10:
            self.edge = True
        if self.rect.x > 450:
            self.edge = False
        if self.edge:
            self.rect.x += self.speed_x
        else:
            self.rect.x -= self.speed_x

