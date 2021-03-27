import pygame, sys, random
from settings import *
from menu import *
from practice_exercise import *
from create_exercise_GUI import *
from rankings import *


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
        self.load_sound()
        self.on_play = 1
        self.muted = 0
        pygame.display.set_caption(TITLE)
        self.r = Rankings(self)
        self.main_menu = MainMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

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
                if event.key == pygame.K_p:
                    if self.on_play == 1:
                        pygame.mixer.music.pause()
                        self.on_play = 0
                    elif self.on_play == 0:
                        pygame.mixer.music.unpause()
                        self.on_play = 1
                if event.key == pygame.K_m:
                    if self.muted == 1:
                        for sound in self.sounds:
                            sound.set_volume(.1)
                            pygame.mixer.music.set_volume(1)
                        self.muted = 0
                    elif self.muted == 0:
                        for sound in self.sounds:
                            sound.set_volume(0)
                            pygame.mixer.music.set_volume(0)
                        self.muted = 1
                            
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
        p = PracticeExercise()
        p.main()
        

    def create_exercise(self):
        matrix_editor = MatrixEditor()
        matrix_editor.main()

    def rankings(self):
        waiting = True
        while waiting:
            self.display.fill(BLACK)
            self.snoweffect()
            self.r.show_rankings()
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.check_events()
            if self.BACK_KEY:
                self.fill_sound.play()
                waiting = False
            self.reset_keys()

    def load_sound(self):
        pygame.mixer.music.load("assets/sounds/theme.wav")
        pygame.mixer.music.play(-1)
        self.sounds = []
        self.select_sound = pygame.mixer.Sound("assets/sounds/select.wav")
        self.select_sound.set_volume(.1)
        self.sounds.append(self.select_sound)
        self.fill_sound = pygame.mixer.Sound("assets/sounds/fill.wav")
        self.fill_sound.set_volume(.1)
        self.sounds.append(self.fill_sound)
        self.lose_sound = pygame.mixer.Sound("assets/sounds/lose.wav")
        self.lose_sound.set_volume(.1)
        self.sounds.append(self.lose_sound)
        self.right_sound = pygame.mixer.Sound("assets/sounds/right.wav")
        self.right_sound.set_volume(.1)
        self.sounds.append(self.right_sound)

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
            s.y += 1.5
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