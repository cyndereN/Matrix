import tkinter
import tkinter.filedialog
import pygame
from pygame_widgets import Button
from exercise import Exercise
from settings import *

pygame.init()
window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
clock = pygame.time.Clock()
filePath = ""
button = pygame.Rect(100,100,100,50)
customFont = pygame.font.SysFont('comicsans', 35)
text = customFont.render("Load", True, (0,0,0))

def prompt_file():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    global filePath
    filePath = file_name

def loadData(filePath):
    exercise = Exercise()
    questionList = exercise.import_exercise(filePath)
    print("==================== From File ======================")
    for x in questionList:
        print("Text:        " + str(x.get_text()))
        print("Type:        " + str(x.get_question_type()))
        print("Matrices:    " + str(x.get_matrices()))
        print("Answer:      " + str(x.get_answer()))
        print("-----------------------------------------\n")

def draw_window():
    # draw surface - fill background
    window.fill(pygame.color.Color("grey"))
    pygame.draw.rect(window, (255, 0, 0), button)
    window.blit(text, (100+25,100+15))
    ## update title to show filename
    pygame.display.set_caption("Load file")
    # show surface
    pygame.display.update()

def main():
    frames = 0
    running = True

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos       # gets mouse position

                # checks if mouse position is over button
                if button.collidepoint(mouse_pos):
                    prompt_file()
                    print(filePath)
                    loadData(filePath)

        draw_window()
        # limit frames
        clock.tick(FPS)
        frames += 1
    pygame.quit()

if __name__ == "__main__":
    main()
