import pygame, sys
from eagles import Eagles
from sprite import Sprite
from enemies import Enemy
from stars import Star
from disintegrate import Disintegrate
import constants as c
import random
from stars import Star
from power_up import Power
from double import Double
from shield import Shield
from pygame import mixer


class Game:
    def __init__(self):
        # background
        self.stars = pygame.sprite.Group()
        self.star_timer = random.randrange(1, 10)
        # player
        self.player_sprite = Sprite((c.DISPLAY_X // 2, c.DISPLAY_Y))
        self.player = pygame.sprite.Group()
        self.player.add(self.player_sprite)
        self.player_score = 0
        self.health = 100
        #power up
        self.power = pygame.sprite.Group()
        self.buddy_sprite = ""
        self.buddy = pygame.sprite.Group()
        self.shield_sprite = ""
        self.shield = pygame.sprite.Group()
        # laser
        self.laser = self.player_sprite.laser
        self.buddy_laser = ""
        # enemy
        self.eagle_enemy = Eagles()
        self.boss = False
        self.hit_cnt = 0
        self.eagle_laser = self.eagle_enemy.eg_laser
        self.enemy = pygame.sprite.Group()
        self.eagle = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 60)
        # disintegrate
        self.disintegrate = pygame.sprite.Group()
        # powerup

    def run(self):

        self.render_background()
        self.stars.draw(screen)
        self.stars.update()
        # players
        self.player.update()
        self.player.draw(screen)
        self.laser.draw(screen)
        #player power up
        if self.power:
            self.power.draw(screen)
            self.power.update()
        if self.buddy:
            self.buddy.draw(screen)
            self.buddy.update()
            self.buddy_laser.draw(screen)
        if self.shield:
            self.shield.draw(screen)
            self.shield.update()
        #enemies
        self.spawn_enemy()
        if self.enemy:
            self.enemy.draw(screen)
            self.enemy.update()
        if self.eagle:
            self.eagle.draw(screen)
            self.eagle_laser.draw(screen) 
            self.eagle.update()

        #collision
        self.collision()
        self.game_over()
        # boom boom
        if self.disintegrate:
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

        if self.player_score == 10000  and len(self.eagle) < 1:
            self.boss = True
            self.eagle.add(self.eagle_enemy)
    
    def spawn_power_up(self):
        new_power = Power()
        self.power.add(new_power)

    def double_power(self):
        self.buddy_sprite = Double((self.player_sprite.rect.x + 90, self.player_sprite.rect.y + 75))
        self.buddy_laser = self.buddy_sprite.laser
        self.buddy.add(self.buddy_sprite)

    def shield_power(self):
        self.shield_sprite = Shield((self.player_sprite.rect.x + 45, self.player_sprite.rect.y - 10))
        self.shield.add(self.shield_sprite)

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
                    exp_sound = mixer.Sound("../assets/explosion.wav")
                    exp_sound.play()
                    laser.kill()
                    self.player_score += 1000

                    if self.player_score % 20000 == 0:
                        self.spawn_power_up()

                if pygame.sprite.spritecollide(laser, self.eagle, False):
                    self.hit_cnt += 1
                    laser.kill()
                    if self.hit_cnt == 50:
                        pygame.sprite.spritecollide(laser, self.eagle, True)
                        laser.kill()
                        self.player_score += 2500
                        self.spawn_power_up()
        
        if self.buddy_laser:
            for laser in self.buddy_laser:
                if pygame.sprite.spritecollide(laser, self.enemy, True):
                    self.enemy_go_boom((laser.rect.x, laser.rect.y))
                    exp_sound = mixer.Sound("../assets/explosion.wav")
                    exp_sound.play()
                    laser.kill()
                    self.player_score += 1000
                    if self.player_score % 20000 == 0:
                        self.spawn_power_up()

                if pygame.sprite.spritecollide(laser, self.eagle, False):
                    self.hit_cnt += 1
                    laser.kill()
                    if self.hit_cnt == 50:
                        pygame.sprite.spritecollide(laser, self.eagle, True)
                        laser.kill()
                        self.player_score += 2500
                        self.spawn_power_up()

        if self.eagle_laser:
            for laser in self.eagle_laser:
                if pygame.sprite.spritecollide(laser, self.player, False):
                    self.health -= 10
                    laser.kill()
                    if self.health <= 10:
                        pygame.sprite.spritecollide(laser, self.player, True)
                        laser.kill()
                if len(self.eagle) == 0:
                    laser.kill()


                    self.player_score += c.POINTS

        if self.enemy:
            for enemy in self.enemy:
                if pygame.sprite.spritecollide(enemy, self.player, False):
                    self.health -= 20
                    self.enemy_go_boom((enemy.rect.x, enemy.rect.y))
                    exp_sound = mixer.Sound("../assets/explosion.wav")
                    exp_sound.play()
                    enemy.kill()
                    if self.health <= 20:
                        pygame.sprite.spritecollide(enemy, self.player, True)
                        enemy.kill()
                    
                    
                    
        if self.eagle:
            for eagle in self.eagle:
                if pygame.sprite.spritecollide(eagle, self.player, True):
                    eagle.kill()

        if self.power:
            for power in self.power:
                if pygame.sprite.spritecollide(power, self.player, False):
                    power.kill()
                    random.choice([self.double_power, self.shield_power])()

        if self.shield:
            for shield in self.shield:
                if pygame.sprite.spritecollide(shield, self.enemy, True):
                    self.enemy_go_boom((shield.rect.x + 45, shield.rect.y))
                    exp_sound = mixer.Sound("../assets/explosion.wav")
                    exp_sound.play()
                    self.player_score += 1000
                if self.eagle_laser:
                    for laser in self.eagle_laser:
                        if pygame.sprite.spritecollide(laser, shield, False):
                            laser.kill()
                
        if not self.player:
            for laser in self.eagle_laser:
                laser.kill()
            for laser in self.laser:
                laser.kill()
        
# scoreboard
    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font("../assets/ARCADECLASSIC.TTF", size)
        text_surface = font.render(text, True, c.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

# heatlth
    def draw_health(self, x, y,health):
        bar_width = 100
        bar_height = 10
        bar_fill = (health / 100) * bar_width
        bar_rect = pygame.Rect(x, y, bar_width, bar_height)
        fill_rect = pygame.Rect(x, y, bar_fill, bar_height)
        pygame.draw.rect(screen, c.BLUE, fill_rect)
        pygame.draw.rect(screen, c.GOLD, bar_rect, 1)


    def game_over(self):
        if not self.player:
            pygame.quit()


if __name__ == "__main__":
    pygame.init()
    
    screen = pygame.display.set_mode(c.DISPLAY_SIZE)
    pygame.display.set_caption("Lazer Python")
    clock = pygame.time.Clock()

    mixer.music.load("../assets/background.wav")
    mixer.music.set_volume(0.1)
    mixer.music.play()


    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(c.BLACK)
        
        game.draw_text(screen, str(game.player_score), 30, c.DISPLAY_X // 2, 10)

        game.draw_health(15,540,game.health)

        game.run()

        pygame.display.flip()

        clock.tick(c.FPS)
