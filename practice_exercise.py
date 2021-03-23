import tkinter
import tkinter.filedialog
import pygame
import numpy
import ast
from functools import reduce
from operator import add
from pygame._freetype import *
from exercise import Exercise
from settings import *

GRIDBOX_H, GRIDBOX_W = 50, 50
MARGIN = 5
RED = (255, 0, 0)
TEXTBOX_ACTIVE = (137, 209, 254)
TEXTBOX_MAX_LENGTH = 40

pygame.init()
window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
clock = pygame.time.Clock()
filePath = ""
matrixList = []

# init buttons and textbox
loadButton = pygame.Rect(DISPLAY_W/2-50, DISPLAY_H/2, 100, 50)
smallLoadButton = pygame.Rect(20, 20, 80, 40)
prevButton = pygame.Rect(DISPLAY_W/2-210, 40, 120, 40)
nextButton = pygame.Rect(DISPLAY_W/2+50, 40, 120, 40)
answerInputTextBox = pygame.Rect(350, 445, 400, 30)
submitButton = pygame.Rect(DISPLAY_W/2-60, 520, 120, 40)

# init fonts
customFont = pygame.font.SysFont('comicsans', 35)
smallFont = pygame.font.SysFont('comicsans', 25)
answerFont = pygame.font.SysFont('Calibri', 17)

# init text with corresponding fonts
loadText = customFont.render("Load", True, WHITE)
smallLoadText = smallFont.render("Load", True, WHITE)
prevText = smallFont.render("Previous", True, WHITE)
nextText = smallFont.render("Next", True, WHITE)
answerText = smallFont.render("Answer: ", True, BLACK)
submitText = smallFont.render("Submit", True, WHITE)


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


# helper function to get rows x cols of matrix
def getMatrixDimensions(matrix):
    return numpy.array(matrix).shape


def roundTo2Decimals(answer):
    return [round(x, 2) if not isinstance(x, list) else roundTo2Decimals(x) for x in answer]

def submitAnswer(inputText, matrix):
    lst = ast.literal_eval(inputText)
    answer = reduce(add, matrix.get_answer())
    rounded = roundTo2Decimals(answer)
    print(lst)
    print(answer)
    print(rounded)
    if lst == rounded:
        return True
    else:
        return rounded


# display question text on screen
def drawMatrixQuestion(matrix):
    numFont = pygame.font.SysFont('Arial', 15)
    questionText = matrix.get_text()
    pygame.draw.rect(window, WHITE, (DISPLAY_W/2-120, 110, 210, 40))
    text = numFont.render(questionText, True, BLACK)
    window.blit(text, (DISPLAY_W/2-110, 120))


# display matrix data on screen
def drawMatrix(matrix):
    matrix1, matrix2 = matrix.get_matrices()[0], matrix.get_matrices()[1]
    numFont = pygame.font.SysFont('Arial', 15)

    # display matrix at centre
    if matrix2 is None:
        rows, cols = getMatrixDimensions(matrix1)
        for row in range(rows):
            for col in range(cols):
                gridX = (MARGIN+GRIDBOX_W)*col+MARGIN+DISPLAY_W/2-100
                gridY = (MARGIN+GRIDBOX_H)*row+MARGIN+200
                pygame.draw.rect(window, WHITE, [gridX, gridY,GRIDBOX_W,GRIDBOX_H])
                text = numFont.render(str(matrix1[row][col]), True, BLACK)
                window.blit(text, (gridX+(GRIDBOX_W/2 - text.get_width()/2), gridY+(GRIDBOX_H/2 - text.get_height()/2)))

    # display both matrices side by side
    else:
        rows1, cols1 = getMatrixDimensions(matrix1)
        rows2, cols2 = getMatrixDimensions(matrix2)

        for row in range(rows1):
            for col in range(cols1):
                gridX = (MARGIN+GRIDBOX_W)*col+MARGIN+DISPLAY_W/4-50
                gridY = (MARGIN+GRIDBOX_H)*row+MARGIN+180
                pygame.draw.rect(window, WHITE, [gridX, gridY,GRIDBOX_W,GRIDBOX_H])
                text = numFont.render(str(matrix1[row][col]), True, BLACK)
                window.blit(text, (gridX+(GRIDBOX_W/2 - text.get_width()/2), gridY+(GRIDBOX_H/2 - text.get_height()/2)))

        for row in range(rows2):
            for col in range(cols2):
                gridX = (MARGIN+GRIDBOX_W)*col+MARGIN+3*DISPLAY_W/4-120
                gridY = (MARGIN+GRIDBOX_H)*row+MARGIN+180
                pygame.draw.rect(window, WHITE, [gridX, gridY,GRIDBOX_W,GRIDBOX_H])
                text = numFont.render(str(matrix2[row][col]), True, BLACK)
                window.blit(text, (gridX+(GRIDBOX_W/2 - text.get_width()/2), gridY+(GRIDBOX_H/2 - text.get_height()/2)))

# display texts related to answer
def drawMatrixAnswer(matrix):
    matrixType = matrix.get_question_type()
    window.blit(answerText, (250, 450))
    pygame.draw.rect(window, WHITE, answerInputTextBox)
    pygame.draw.rect(window, RED, submitButton)
    window.blit(submitText, (DISPLAY_W/2-35, 530))

# display answer textfield
def drawAnswerText(inputText):
    displayText = answerFont.render(inputText, True, BLACK)
    window.blit(displayText, (355, 450))
    pygame.display.update()

# draw start screen
def draw_window():

    window.fill(pygame.color.Color("grey"))
    pygame.draw.rect(window, RED, loadButton)
    window.blit(loadText, (DISPLAY_W/2-50 + 23, DISPLAY_H/2 + 15))
    pygame.display.set_caption("Load Matrix From File")
    pygame.display.update()

# draw matrix to screen
def draw_matrix_window(matrix):
    window.fill(pygame.color.Color("grey"))
    pygame.draw.rect(window, RED, smallLoadButton)
    pygame.draw.rect(window, RED, prevButton)
    pygame.draw.rect(window, RED, nextButton)

    window.blit(smallLoadText, (20 + 21, 20 + 13))
    window.blit(prevText, (DISPLAY_W/2-210 + 21, 40 + 12))
    window.blit(nextText, (DISPLAY_W/2+50 + 40, 40 + 12))

    drawMatrixQuestion(matrix)
    drawMatrix(matrix)
    drawMatrixAnswer(matrix)
    pygame.display.set_caption("Practice Questions")
    pygame.display.flip()

# main window
def main():
    running = True
    global matrixList
    exerciseIndex = 0
    inputText = ""
    inputBoxActive = False
    answerSubmitted = False

    draw_window()
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos       # get mouse position

                # checks if mouse position is over button
                if loadButton.collidepoint(mouse_pos) or smallLoadButton.collidepoint(mouse_pos):
                    prompt_file()
                    matrixList = loadData(filePath)
                    draw_matrix_window(matrixList[0])
                    inputText = ""
                    answerSubmitted = False

                elif nextButton.collidepoint(mouse_pos):
                    try:
                        exerciseIndex += 1
                        draw_matrix_window(matrixList[exerciseIndex])
                        inputText = ""
                        answerSubmitted = False
                    except IndexError:
                        exerciseIndex -= 1
                        #print("No matrix to read!")

                elif prevButton.collidepoint(mouse_pos) and exerciseIndex > 0:
                    try:
                        exerciseIndex -= 1
                        draw_matrix_window(matrixList[exerciseIndex])
                        inputText = ""
                        answerSubmitted = False
                    except IndexError:
                        exerciseIndex += 1
                        #print("No matrix to read!")

                elif answerInputTextBox.collidepoint(mouse_pos) and not answerSubmitted:
                    pygame.draw.rect(window, TEXTBOX_ACTIVE, answerInputTextBox)
                    inputBoxActive = True

                elif submitButton.collidepoint(mouse_pos):
                    pygame.draw.rect(window, WHITE, answerInputTextBox)
                    drawAnswerText(inputText)
                    submitAnswer(inputText, matrixList[exerciseIndex])
                    inputBoxActive = False
                    answerSubmitted = True

            # if key pressed and input box has been clicked
            elif event.type == pygame.KEYDOWN and inputBoxActive:
                if event.key == pygame.K_RETURN:
                    pygame.draw.rect(window, WHITE, answerInputTextBox)
                    drawAnswerText(inputText)
                    submitAnswer(inputText, matrixList[exerciseIndex])
                    inputBoxActive = False
                    answerSubmitted = True

                elif event.key == pygame.K_BACKSPACE:
                    inputText = inputText[:-1]
                    if len(inputText) >= TEXTBOX_MAX_LENGTH:
                        trimmedText = inputText[-TEXTBOX_MAX_LENGTH:]
                        pygame.draw.rect(window, TEXTBOX_ACTIVE, answerInputTextBox)
                        drawAnswerText(trimmedText)
                    else:
                        pygame.draw.rect(window, TEXTBOX_ACTIVE, answerInputTextBox)
                        drawAnswerText(inputText)

                else:
                    inputText += event.unicode
                    if len(inputText) >= TEXTBOX_MAX_LENGTH:
                        trimmedText = inputText[-TEXTBOX_MAX_LENGTH:]
                        pygame.draw.rect(window, TEXTBOX_ACTIVE, answerInputTextBox)
                        drawAnswerText(trimmedText)
                    else: drawAnswerText(inputText)


        pygame.display.update()
        # limit frames
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
