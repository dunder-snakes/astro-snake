import pygame, sys
from sprite import Sprite
from enemies import Enemy
from stars import Star
from disintegrate import Disintegrate
import constants as c
import random

class Game:
    def __init__(self):
        # background
        self.stars = pygame.sprite.Group()
        self.star_timer = random.randrange(1, 10)
        # player
        player_sprite = Sprite((c.DISPLAY_X // 2, c.DISPLAY_Y)) 
        self.player = pygame.sprite.Group()
        self.player.add(player_sprite)
        self.player_score = 0
        # laser
        self.laser = player_sprite.laser
        # enemy
        self.enemy = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 60)
        # disintegration
        self.disintegrate = pygame.sprite.Group()
        

    def run(self):
        # stars
        self.render_background()
        self.stars.draw(screen)
        self.stars.update()
        #players
        self.player.update()
        self.player.draw(screen)
        self.laser.draw(screen)
        #enemies
        self.spawn_enemy()
        self.enemy.draw(screen)
        self.enemy.update() 
        #collision
        self.collision()
        self.game_over()
        #boom boom
        self.disintegrate.draw(screen)
        self.disintegrate.update()


    def render_background(self):
        new_star = Star()
        if self.star_timer == 0:
            self.stars.add(new_star)
            self.star_timer = random.randrange(1, 10)
        else:
            self.star_timer -= 1

    def spawn_enemy(self):
        sprite_enemy = Enemy()
        if self.spawn_timer == 0:
            self.enemy.add(sprite_enemy)
            self.spawn_timer = random.randrange(30, 60)
        else:
            self.spawn_timer -= 1

    def enemy_go_boom(self, pos):
        for _ in range(random.randrange(10, 30)):
            particle = Disintegrate()
            particle.rect.x = pos[0]
            particle.rect.y = pos[1]
            self.disintegrate.add(particle)
    
    def collision(self):
        if self.laser:
            for laser in self.laser:
                if pygame.sprite.spritecollide(laser, self.enemy, True):
                    self.enemy_go_boom((laser.rect.x, laser.rect.y))
                    laser.kill()
                    self.player_score += 1000
        if self.enemy:
            for enemy in self.enemy:
                if pygame.sprite.spritecollide(enemy, self.player, True):
                    enemy.kill()
        if not self.player:
            for laser in self.laser:
                laser.kill()

    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font("../assets/ARCADECLASSIC.TTF", size)
        text_surface = font.render(text, True, c.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def game_over(self):
        if not self.player:
            pygame.quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(c.DISPLAY_SIZE)
    pygame.display.set_caption("Lazer Python")
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0,0,0))

        game.draw_text(screen, str(game.player_score), 30, c.DISPLAY_X//2, 10)

        game.run()

        pygame.display.flip()

        clock.tick(60)
