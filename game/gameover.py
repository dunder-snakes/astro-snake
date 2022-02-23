from os import system
import pygame
import constants as c

class Gameover(pygame.sprite.Sprite):
  def __init__(self):
    super(self).__init__()

    display_gameover = pygame.display.set_mode((c.DISPLAY_SIZE))
    bg_image = pygame.image.load('../assets/1781.jpg')
    bg_image = pygame.transform.scale(bg_image, (c.DISPLAY_SIZE))


    # running = True
    # while running:
    #   for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #       pygame.quit()
    #       system.exit()
    #       running = False
    display_gameover.blit(bg_image, (0, 0))
    pygame.display.flip()



    # restart_button = 
    # quit_button = 


# button for quit and restart
# font from Min's push for buttons

# will button be pressed or handled by a key


# when player dies, activate gameover
# gameover will bring up gameover space image 


# determine what events to check for in order for game over screen to appear




