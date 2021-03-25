import pygame, sys, random
from settings import *
from menu import *
from practice_exercise import *
from create_exercise_GUI import *

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.credit_showing = False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.display = pygame.Surface((DISPLAY_W, DISPLAY_H))
        self.window = pygame.display.set_mode(((DISPLAY_W, DISPLAY_H)))
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)
        self.initialize_snow()
        pygame.display.set_caption(TITLE)
        self.main_menu = MainMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.BACK_KEY:
                self.playing = False
            self.display.fill(BLACK)
            self.snoweffect_helper()
            self.draw_text('Thanks for playing', 20, DISPLAY_W/2, DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing, self.curr_menu.run_display = False, False, False
                self.credit_showing = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
            
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(FONT_1,size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)

    def draw_text_2(self, text, size, x, y):
        font = pygame.font.Font(FONT_2,size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)

    def start_exercise(self):
        waiting = True
        while waiting:
            p = PracticeExercise()
            p.main()
            self.check_events()
            if self.BACK_KEY:
                waiting = False
            self.reset_keys()
        

    def import_exercise(self):
        pass

    def create_exercise(self):
        matrix_editor = MatrixEditor()
        matrix_editor.main()


    def rankings():
        pass

    def credits(self):
        waiting = True
        while waiting:
            self.display.fill(BLACK)
            self.draw_text('Thanks for playing', 20, DISPLAY_W/2, DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.check_events()
            if self.BACK_KEY:
                waiting = False
            self.reset_keys()

    def initialize_snow(self):
        self.snowflakes = []
        for i in range(200):
            self.snowflakes.append(snow(self))

    def snoweffect(self):
        for s in self.snowflakes:
            s.y += 1
            if (s.y > DISPLAY_H):
                s.x = random.randrange(0,DISPLAY_W)
                s.y = random.randrange(-50,-10)
            s.drawSnow()

    def snoweffect_helper(self):
        for s in self.snowflakes:
            s.y += 0.2
            if (s.y > DISPLAY_H):
                s.x = random.randrange(0,DISPLAY_W)
                s.y = random.randrange(-50,-10)
            s.drawSnow()

class snow:
    def __init__(self, game):
        self.game = game
        self.x = random.randrange(0, DISPLAY_W)
        self.y = random.randrange(0, DISPLAY_W)

    def drawSnow(self):
        pygame.draw.rect(self.game.display, WHITE, (self.x, self.y, 2, 2))