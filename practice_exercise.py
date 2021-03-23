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
loadButton = pygame.Rect(100, 100, 100, 50)
smallLoadButton = pygame.Rect(50, 50, 100, 50)
prevButton = pygame.Rect(DISPLAY_W/2-290, 100, 120, 50)
nextButton = pygame.Rect(DISPLAY_W/2+120, 100, 100, 50)
customFont = pygame.font.SysFont('comicsans', 35)
loadText = customFont.render("Load", True, WHITE)
prevText = customFont.render("Previous", True, WHITE)
nextText = customFont.render("Next", True, WHITE)

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
    return questionList


def getMatrixDimensions(matrix):
    return numpy.array(matrix).shape

def drawMatrix(matrix1, matrix2=None):
    numFont = pygame.font.SysFont('Arial', 15)
    if matrix2 is None:
        rows, cols = getMatrixDimensions(matrix1)
        for row in range(rows):
            for col in range(cols):
                gridX = (MARGIN+GRIDBOX_W)*col+MARGIN+DISPLAY_W/2-100
                gridY = (MARGIN+GRIDBOX_H)*row+MARGIN+200
                pygame.draw.rect(window, WHITE, [gridX, gridY,GRIDBOX_W,GRIDBOX_H])
                text = numFont.render(str(matrix1[row][col]), True, BLACK)
                window.blit(text, (gridX+(GRIDBOX_W/2 - text.get_width()/2), gridY+(GRIDBOX_H/2 - text.get_height()/2)))
    else:
        rows1, cols1 = getMatrixDimensions(matrix1)
        rows2, cols2 = getMatrixDimensions(matrix2)
        for row in range(rows1):
            for col in range(cols1):
                gridX = (MARGIN+GRIDBOX_W)*col+MARGIN+DISPLAY_W/4-50
                gridY = (MARGIN+GRIDBOX_H)*row+MARGIN+200
                pygame.draw.rect(window, WHITE, [gridX, gridY,GRIDBOX_W,GRIDBOX_H])
                text = numFont.render(str(matrix1[row][col]), True, BLACK)
                window.blit(text, (gridX+(GRIDBOX_W/2 - text.get_width()/2), gridY+(GRIDBOX_H/2 - text.get_height()/2)))
        for row in range(rows2):
            for col in range(cols2):
                gridX = (MARGIN+GRIDBOX_W)*col+MARGIN+3*DISPLAY_W/4-120
                gridY = (MARGIN+GRIDBOX_H)*row+MARGIN+200
                pygame.draw.rect(window, WHITE, [gridX, gridY,GRIDBOX_W,GRIDBOX_H])
                text = numFont.render(str(matrix1[row][col]), True, BLACK)
                window.blit(text, (gridX+(GRIDBOX_W/2 - text.get_width()/2), gridY+(GRIDBOX_H/2 - text.get_height()/2)))


def draw_window():
    # draw surface - fill background
    window.fill(pygame.color.Color("grey"))
    pygame.draw.rect(window, (255, 0, 0), loadButton)
    window.blit(loadText, (100 + 23, 100 + 15))

    pygame.display.set_caption("Import matrix file")
    # show surface
    pygame.display.update()

def draw_matrix_window(matrix):
    window.fill(pygame.color.Color("grey"))
    pygame.draw.rect(window, (255, 0, 0), smallLoadButton)
    pygame.draw.rect(window, (255, 0, 0), prevButton)
    pygame.draw.rect(window, (255, 0, 0), nextButton)
    window.blit(loadText, (50 + 23, 50 + 15))
    window.blit(prevText, (DISPLAY_W/2-300 + 20, 100 + 15))
    window.blit(nextText, (DISPLAY_W/2+120 + 23, 100 + 15))
    drawMatrix(matrix.get_matrices()[0], matrix.get_matrices()[1])
    pygame.display.set_caption("Import matrix file")
    pygame.display.flip()

def main():
    running = True
    global matrixList
    exerciseIndex = 0

    draw_window()
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos       # gets mouse position

                # checks if mouse position is over button
                if loadButton.collidepoint(mouse_pos) or smallLoadButton.collidepoint(mouse_pos):
                    prompt_file()
                    matrixList = loadData(filePath)
                    draw_matrix_window(matrixList[0])
                if nextButton.collidepoint(mouse_pos):
                    try:
                        exerciseIndex += 1
                        draw_matrix_window(matrixList[exerciseIndex])
                    except IndexError:
                        exerciseIndex -= 1
                        #print("No matrix to read!")
                if prevButton.collidepoint(mouse_pos) and exerciseIndex > 0:
                    try:
                        exerciseIndex -= 1
                        draw_matrix_window(matrixList[exerciseIndex])
                    except IndexError:
                        exerciseIndex += 1
                        #print("No matrix to read!")


        pygame.display.update()
        # limit frames
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
