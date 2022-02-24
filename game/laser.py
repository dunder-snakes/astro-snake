import pygame
import constants as c
from pygame import mixer


def crash():
    crash_sound = mixer.Sound("../assets/explosion.wav")
    crash_sound.play()


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([2, 15])
        self.image.fill(c.RED)
        self.rect = self.image.get_rect(center=pos)
        laser_sound = mixer.Sound("../assets/laser.mp3")
        laser_sound.play()


    def update(self):
        self.rect.y += c.LASER_SPEED
        if self.rect.y < 0:
            self.kill()
