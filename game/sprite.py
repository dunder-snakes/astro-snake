import pygame
from laser import Laser
import constants as c

class Sprite(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.image = pygame.Surface([75, 75], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.sp_image = pygame.image.load("assets/cartoon_snake.png")
        self.sprite_img = pygame.transform.scale(self.sp_image,(75, 75))
        self.image.blit(self.sprite_img,(0,0))
        self.loaded = True
        self.recharge_time = 0
        self.laser = pygame.sprite.Group()
        self.rect = self.image.get_rect(midbottom = pos)
        self.dist = c.SNAKE_SPEED

    def inputs(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            if self.rect.x != c.DISPLAY_X - self.rect.width:
                self.rect.x += self.dist

        if key[pygame.K_LEFT]:
            if self.rect.x != 0:
                self.rect.x -= self.dist

        if key[pygame.K_UP]:
            if self.rect.y != 0:
                self.rect.y -= self.dist

        if key[pygame.K_DOWN]:
            if self.rect.y != c.DISPLAY_Y - self.rect.height:
                self.rect.y += self.dist
                
        if key[pygame.K_SPACE] & self.loaded:
            self.fire()
            

    def fire(self):
        self.laser.add(Laser(self.rect.midtop))
        self.loaded = False
        self.recharge_time = pygame.time.get_ticks()
    
    def recharge(self):
        if pygame.time.get_ticks() - self.recharge_time > 150:
            self.loaded = True

    def update(self):
        self.inputs()
        self.recharge()
        self.laser.update()


