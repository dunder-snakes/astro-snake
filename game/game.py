import pygame, sys
from sprite import Sprite
from enemies import Enemy
import constants as c
import random
from stars import Star

class Game:
    def __init__(self):
        player_sprite = Sprite((c.DISPLAY_X // 2, c.DISPLAY_Y)) 
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.player_score = 0
        self.laser = player_sprite.laser
        self.enemy = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 60)
        self.stars = pygame.sprite.Group()
        self.star_timer = random.randrange(1, 10)

    def run(self):
        # background
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
        self.kill_out_of_bounds()
        #collision
        self.collision()
        self.game_over()

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
    # back_image = pygame.image.load("../domain_model.jpg")
    # back_image = pygame.transform.scale(back_image, c.DISPLAY_SIZE)
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        # screen.blit(back_image, (0,0))

        game.draw_text(screen, str(game.player_score), 18, c.DISPLAY_X//2, 10)

        game.run()

        pygame.display.flip()

        clock.tick(60)
