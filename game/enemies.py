import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,height, width, pos):
        super().__init__()

        self.image = pygame.Surface([width, height])
        ## Change picture to mongoose
        self.en_image = pygame.image.load("/assets/snake.png")
        self.enemy = pygame.transform.scale(self.en_image,(width, height))
        self.image.blit(self.enemy,(0,0))

        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.y += 1
