import pygame
import sys
from exercise import Exercise
from View import View
WIDTH = 960
HEIGHT = 580

class Controller:

    def __init__(self):
        self.size = WIDTH, HEIGHT
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Matrix Game")
        self.exercise_generator = Exercise()
        self.exercise = []
        self.current_question = 0

    def get_new_exercise(self, set_size):
        self.exercise = self.exercise_generator.generate_exercise(set_size)

    def run(self):
        # Test Code Begin
        self.get_new_exercise(1)
        text = self.exercise[0]
        # Test Code End

        while True:
            view = View(self.screen, self)
            view.random_exercise_view(text)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
        pygame.quit()