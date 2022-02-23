import pygame

class Button():
  def __init__(self, pos, text_input):
    self.image = pygame.image.load('../assets/triangle.png')
    self.pos_x = pos[0]
    self.pos_y = pos[1]
    self.text_input = text_input
    self.font = pygame.font.Font("../assets/ARCADECLASSIC.TTF", 75)
    self.base_color, self.hovering_color = "#d7fcd4", (255, 255, 255)
    self.text = self.font.render(self.text_input, True, self.base_color)
    self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
    self.text_rect = self.text.get_rect(center=(self.pos_x, self.pos_y))

  def update(self, screen):
    screen.blit(self.text, self.text_rect)

  def checkForInput(self, position):
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
      return True
    return False
      
  def changeColor(self, position):
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
      self.text = self.font.render(self.text_input, True, self.hovering_color)
    else:
      self.text = self.font.render(self.text_input, True, self.base_color)
  