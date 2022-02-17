import pygame, sys
from sprite import Sprite
from enemies import Enemy
import random

YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

class Game:
    def __init__(self):
        player_sprite = Sprite(YELLOW, 20, 20, (300, 600)) 
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.laser = player_sprite.laser
        self.enemy = pygame.sprite.Group()

    def run(self):
        self.player.update()
        self.player.draw(screen)
        self.laser.draw(screen)

    def run_enemy(self):
        random_x = random.randint(0, 600)
        sprite_enemy = Enemy(BLUE, 30, 30, (random_x, 0))
        spawn_time = pygame.time.get_ticks()
        if len(self.enemy) < 5:
            self.enemy.add(sprite_enemy)
        self.enemy.draw(screen)
        self.enemy.update()    

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Lazer Python")
    clock = pygame.time.Clock()
    game = Game()

    moving = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                moving = False

        screen.fill((10, 10, 10))
        game.run()
        game.run_enemy()

        pygame.display.flip()

        clock.tick(60)
