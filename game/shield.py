import pygame
import random
import constants as c

class Shield(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.image = pygame.Surface([120, 3], pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect(midtop = pos)
        self.dist = c.SNAKE_SPEED
        self.spawn_time = pygame.time.get_ticks()
        self.duration = 30

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

    def update(self):
        self.color_changer()
        self.inputs()
        if (pygame.time.get_ticks() - self.spawn_time) / 1000 > self.duration:
            self.kill()

    def color_changer(self):
        self.image.fill((random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)))
