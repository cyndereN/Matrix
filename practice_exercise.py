import tkinter
import tkinter.filedialog
import pygame
import numpy
from pygame._freetype import *
from exercise import Exercise
from settings import *

GRIDBOX_H, GRIDBOX_W = 50,50
MARGIN = 5

pygame.init()
window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
clock = pygame.time.Clock()
filePath = ""
matrixList = []
button = pygame.Rect(100,100,100,50)
customFont = pygame.font.SysFont('comicsans', 35)
text = customFont.render("Load", True, WHITE)

grid = []
for row in range(3):
    grid.append([])
    for col in range(3):
        grid[row].append(0)


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
    return questionList


def getMatrixDimensions(matrix):
    return numpy.array(matrix).shape

def drawMatrix(matrix1):
    rows, cols = getMatrixDimensions(matrix1)
    numFont = pygame.font.SysFont('Arial', 15)
    for row in range(rows):
        for col in range(cols):
            color = WHITE
            gridX = (MARGIN+GRIDBOX_W)*col+MARGIN+DISPLAY_W/2-100
            gridY = (MARGIN+GRIDBOX_H)*row+MARGIN+200
            pygame.draw.rect(window, color, [gridX, gridY,GRIDBOX_W,GRIDBOX_H])
            text = numFont.render(str(matrix1[row][col]), True, BLACK)
            window.blit(text, (gridX+(GRIDBOX_W/2 - text.get_width()/2), gridY+(GRIDBOX_H/2 - text.get_height()/2)))


def draw_window():
    # draw surface - fill background
    window.fill(pygame.color.Color("grey"))
    pygame.draw.rect(window, (255, 0, 0), button)
    window.blit(text, (100+23,100+15))

    for x in matrixList:
        drawMatrix(x.get_matrices()[0])
    ## update title to show filename
    pygame.display.set_caption("Load file")
    # show surface
    pygame.display.update()

def main():
    frames = 0
    running = True
    global matrixList

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
                    matrixList = loadData(filePath)

        draw_window()
        # limit frames
        clock.tick(FPS)
        frames += 1
    pygame.quit()

if __name__ == "__main__":
    main()
