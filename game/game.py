import pygame, sys
from sprite import Sprite

YELLOW = (255,255,0)

class Game:
    def __init__(self):
        player_sprite = Sprite(YELLOW, 20, 20, (300, 600))
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.laser = player_sprite.laser

    def run(self):
        self.player.update()
        self.player.draw(screen)
        self.laser.draw(screen)
        

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600,600))
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

        screen.fill((10,10,10))
        game.run()

        pygame.display.flip()

        clock.tick(60)
