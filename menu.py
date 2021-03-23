import pygame
from settings import *

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = DISPLAY_W/2, DISPLAY_H/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 30, 30)
        self.offset = -300

    def draw_cursor(self):
        self.game.draw_text("*", 20, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.flip()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 40
        self.importx, self.importy = self.mid_w, self.mid_h + 80
        self.createx, self.createy = self.mid_w, self.mid_h + 120
        self.rankingx, self.rankingy = self.mid_w, self.mid_h + 160
        self.creditx, self.credity = self.mid_w, self.mid_h + 200
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(BLACK)
            self.game.snoweffect()
            self.game.draw_text('Matrix', 100, self.mid_w, self.mid_h - 120)
            self.game.draw_text_2("Start Exercise", 30, self.startx, self.starty)
            self.game.draw_text_2("Import Exercise", 30, self.importx, self.importy)
            self.game.draw_text_2("Create Exercise", 30, self.createx, self.createy)
            self.game.draw_text_2("Rankings", 30, self.rankingx, self.rankingy)
            self.game.draw_text_2("Credits", 30, self.creditx, self.credity)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.importx + self.offset, self.importy)
                self.state = 'Import'
            elif self.state == 'Import':
                self.cursor_rect.midtop = (self.createx + self.offset, self.createy)
                self.state = 'Create'
            elif self.state == 'Create':
                self.cursor_rect.midtop = (self.rankingx + self.offset, self.rankingy)
                self.state = 'Ranking'
            elif self.state == 'Ranking':
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = 'Credit'
            elif self.state == 'Credit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop =(self.creditx + self.offset, self.credity)
                self.state = 'Credit'
            elif self.state == 'Import':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Create':
                self.cursor_rect.midtop = (self.importx + self.offset, self.importy)
                self.state = 'Import'
            elif self.state == 'Ranking':
                self.cursor_rect.midtop = (self.createx + self.offset, self.createy)
                self.state = 'Create'
            elif self.state == 'Credit':
                self.cursor_rect.midtop = (self.rankingx + self.offset, self.rankingy)
                self.state = 'Ranking'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.start_exercise()
            elif self.state == 'Import':
                self.game.import_exercise()
            elif self.state == 'Create':
                self.game.create_exercise()
            elif self.state == 'Ranking':
                self.game.rankings()
            elif self.state == 'Credit':
                self.game.curr_menu = self.game.credits
            self.run_display = False

# Make credits inheritates from menu
class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(BLACK)
            self.game.snoweffect()
            self.game.draw_text("CREDITS", 60, self.mid_w, DISPLAY_H / 4 - 40)
            self.game.draw_text_2("Game made by", 22, self.mid_w, DISPLAY_H / 2 - 80)
            self.game.draw_text_2("Ce Cao, Darryl Ng, Leran Li, Yan Lai", 22, self.mid_w, DISPLAY_H / 2 - 20)
            self.game.draw_text_2("Press BACKSPACE to return", 22, self.mid_w, DISPLAY_H * 3 / 4 + 60)
            self.game.draw_text_2("Font: \"Press Start 2P\" by codeman38 ", 15, self.mid_w, DISPLAY_H / 2 + 50)
            self.game.draw_text_2("Font: \"8-bit wonder\" by Joiro Hatgaya ", 15, self.mid_w, DISPLAY_H / 2 + 80)
            self.game.draw_text_2("Music Created with BeepBox", 15, self.mid_w,DISPLAY_H / 2 + 110)
            self.game.draw_text_2("Sound Effects Created with Bfxr", 15, self.mid_w, DISPLAY_H / 2 + 140)
            self.blit_screen()