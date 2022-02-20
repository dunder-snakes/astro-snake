import pygame, sys
from eagles import Eagles
from sprite import Sprite
from enemies import Enemy
import constants as c
import random

class Game:
    def __init__(self):
        player_sprite = Sprite((c.DISPLAY_X // 2, c.DISPLAY_Y))
        self.eagle_enemy = Eagles()
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.player_score = 0
        self.hit_cnt = 0
        self.laser = player_sprite.laser
        self.eagle_laser = self.eagle_enemy.eg_laser
        self.enemy = pygame.sprite.Group()
        self.eagle = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 60)

    def run(self):
        #players
        self.player.update()
        self.player.draw(screen)
        self.laser.draw(screen)
        
        #enemies
        self.spawn_enemy()
        self.enemy.draw(screen)
        self.enemy.update()
        self.eagle.draw(screen)
        self.eagle_laser.draw(screen) 
        self.eagle.update()
        self.kill_out_of_bounds()
        #collision
        self.collision()
        self.game_over()

    def spawn_enemy(self):
        sprite_enemy = Enemy()
        if self.spawn_timer == 0:
            self.enemy.add(sprite_enemy)
            self.spawn_timer = random.randrange(30, 60)
        else:
            self.spawn_timer -= 1
        if self.player_score == 5000 and len(self.eagle) < 1:
            self.eagle.add(self.eagle_enemy)
    
    def kill_out_of_bounds(self):
        if self.enemy:
            for enemy in self.enemy:
                if enemy.rect.y > c.DISPLAY_Y + enemy.rect.y:
                    enemy.kill()

    def collision(self):
        
        if self.laser:
            for laser in self.laser:
                if pygame.sprite.spritecollide(laser, self.enemy, True):
                    laser.kill()
                    self.player_score += 1000
                if pygame.sprite.spritecollide(laser, self.eagle, False):
                    self.hit_cnt += 1
                    laser.kill()
                    if self.hit_cnt == 50:
                        pygame.sprite.spritecollide(laser, self.eagle, True)
                        laser.kill()
                        self.player_score += 2500

        if self.eagle_laser:
            for laser in self.eagle_laser:
                if pygame.sprite.spritecollide(laser, self.player, True):
                    laser.kill()
                    self.player_score += 1000
                if len(self.eagle) == 0:
                    laser.kill()


        if self.enemy:
            for enemy in self.enemy:
                if pygame.sprite.spritecollide(enemy, self.player, True):
                    enemy.kill()

        if self.eagle:
            for eagle in self.eagle:
                if pygame.sprite.spritecollide(eagle, self.player, True):
                    eagle.kill()
                
        if not self.player:
            for laser in self.eagle_laser:
                laser.kill()
            for laser in self.laser:
                laser.kill()

    def draw_text(self, surf, text, size, x, y):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, c.BLUE)
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
    back_image = pygame.image.load("assets/1781.jpg")
    back_image = pygame.transform.scale(back_image, c.DISPLAY_SIZE)
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(back_image, (0,0))

        game.draw_text(screen, str(game.player_score), 18, c.DISPLAY_X//2, 10)

        game.run()

        pygame.display.flip()

        clock.tick(60)
