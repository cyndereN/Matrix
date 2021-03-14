import pygame
WIDTH = 960
HEIGHT = 580

class ButtonObject:

    def __init__(self,surface):
        self.surface = surface
        pass

class MatrixObject:

    def __init__(self,surface,width = 300, height = 300):
        self.width = width
        self.height = height
        self.surface = surface
  
    def draw(self,x,y):
        pygame.draw.rect(self.surface,(255,255,255),(x,y,self.width,self.height))

class TextObject:

    def __init__(self, surface, text, size):
        # Make change here to change the font
        self.font = 'arial'
        self.surface = surface
        font1 = pygame.font.SysFont(self.font, size)
        self.text = font1.render(text, True, (0,0,0))
    
    def draw(self, x, y):
        self.surface.blit(self.text, (x, y))

class View:

    def __init__(self,surface,controller):
        self.surface = surface
        self.controller = controller
        self.mid_x = self.controller.size[0] / 2
        self.mid_y = self.controller.size[1] / 2
        # Fill the screen with white
        self.surface.fill((245,245,245))
        self.button = []
        self.matrix = []
        self.text = []

    def random_exercise_view(self,text):
        matrix1 = MatrixObject(self.surface)
        # Not complete, only draw a square at this point
        matrix1.draw(   self.mid_x - matrix1.width / 2,
                        self.mid_y - matrix1.height / 2)
        question_text = TextObject(self.surface, text, 24)
        question_text.draw(self.mid_x - 150, self.mid_y - 150)