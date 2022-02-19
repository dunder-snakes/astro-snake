from distutils.spawn import spawn
import pygame, sys
from sprite import Sprite
from enemies import Enemy
import random

YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
possible_x = random.sample(range(15, 586), 30)

class Game:
    def __init__(self):
        player_sprite = Sprite(50, 50, (300, 600)) 
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.player_score = 0
        self.laser = player_sprite.laser
        self.enemy = pygame.sprite.Group()
        self.enemy_cooldown = 1000
        self.spawn_time = 0

    def run(self):
        #players
        self.player.update()
        self.player.draw(screen)
        self.laser.draw(screen)
        #enemies
        self.spawn_enemy()
        self.enemy.draw(screen)
        self.enemy.update() 
        self.kill_out_of_bounds()
        #collision
        self.collision()
        self.game_over()

    def spawn_enemy(self):
        spawn_x = random.randint(0, len(possible_x)-1)
        sprite_enemy = Enemy(30, 30, (possible_x[spawn_x], 0))
        if self.player_score == 10:
            self.enemy_cooldown = 750
        if self.player_score == 15:
            self.enemy_cooldown = 500
        if self.player_score == 30:
            self.enemy_cooldown = 250
        
        if pygame.time.get_ticks() - self.spawn_time > self.enemy_cooldown:
            self.enemy.add(sprite_enemy)
            self.spawn_time = pygame.time.get_ticks()
    
    def kill_out_of_bounds(self):
        if self.enemy:
            for enemy in self.enemy:
                if enemy.rect.y > 610:
                    enemy.kill()

    def collision(self):
        if self.laser:
            for laser in self.laser:
                if pygame.sprite.spritecollide(laser, self.enemy, True):
                    laser.kill()
                    self.player_score += 1
        if self.enemy:
            for enemy in self.enemy:
                if pygame.sprite.spritecollide(enemy, self.player, True):
                    enemy.kill()
        if not self.player:
            for laser in self.laser:
                laser.kill()

    def draw_text(self, surf, text, size, x, y):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, BLUE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def game_over(self):
        if not self.player:
            pygame.quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Lazer Python")
    clock = pygame.time.Clock()
    back_image = pygame.image.load("../domain_model.jpg")
    back_image = pygame.transform.scale(back_image, (600,600))
    game = Game()

    moving = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                moving = False

        screen.blit(back_image, (0,0))

        game.draw_text(screen, str(game.player_score), 18, 300, 10)

        game.run()

        pygame.display.flip()

        clock.tick(60)
