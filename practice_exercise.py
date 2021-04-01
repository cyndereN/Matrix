import sys
import tkinter
import tkinter.filedialog
import pygame
import game
from MatrixCalculator import calculator
from Exercise import Exercise
from settings import *


pygame.init()

# init buttons and textbox
loadButton = pygame.Rect(DISPLAY_W/2-70, DISPLAY_H/2-100, 140, 50)
generateButton = pygame.Rect(DISPLAY_W/2-130, DISPLAY_H/2+100, 260, 50)
smallLoadButton = pygame.Rect(20, 20, 80, 40)
smallGenerateButton = pygame.Rect(20, 70, 150, 40)
prevButton = pygame.Rect(DISPLAY_W/2-220, 40, 150, 40)
nextButton = pygame.Rect(DISPLAY_W/2+60, 40, 140, 40)
answerInputTextBox = pygame.Rect(330, 442, 390, 30)
submitButton = pygame.Rect(DISPLAY_W/2-60, 520, 120, 40)
endButton = pygame.Rect(DISPLAY_W-160, 80, 150, 40)
mainMenuButton = pygame.Rect(DISPLAY_W/2-100, DISPLAY_H/2+200, 200, 50)
usernameInputTextBox = pygame.Rect(DISPLAY_W/2-150, DISPLAY_H/2+100, 300, 30)
saveButton = pygame.Rect(DISPLAY_W/2+188, DISPLAY_H/2+91, 100, 40)

# init fonts
customFont = pygame.font.Font(FONT_1, 30)
smallFont = pygame.font.Font(FONT_2, 17)
defaultFont = pygame.font.SysFont('comicsans', 25)
answerFont = pygame.font.SysFont('Calibri', 17)

# init text with corresponding fonts
loadText = customFont.render("Load", True, WHITE)
generateText = customFont.render("Generate", True, WHITE)
smallLoadText = smallFont.render("Load", True, WHITE)
smallGenerateText = smallFont.render("Generate", True, WHITE)
prevText = smallFont.render("Previous", True, WHITE)
nextText = smallFont.render("Next", True, WHITE)
answerText = defaultFont.render("Answer: ", True, BLACK)
submitText = smallFont.render("Submit", True, WHITE)
endText = smallFont.render("End Game", True, WHITE)
mainMenuText = smallFont.render("Main Menu", True, WHITE)
usernameText = defaultFont.render("Username: ", True, BLACK)
saveText = smallFont.render("Save", True, WHITE)


class PracticeExercise:
    def __init__(self):
        self.window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
        self.clock = pygame.time.Clock()
        self.filePath = ""
        self.matrixList = []
        self.score = 0
        self.calculator = calculator()
        self.my_game = game.Game()


    # file dialog to pick a file
    def prompt_file(self):
        """Create a Tk file dialog and cleanup when finished"""
        top = tkinter.Tk()
        top.withdraw()  # hide window
        file_name = tkinter.filedialog.askopenfilename(parent=top)
        top.destroy()
        self.filePath = file_name

    # load data from file
    def loadData(self):
        return Exercise().import_exercise(self.filePath)

    # generate random matrix data
    def generateData(self):
        return Exercise().generate_exercise(5)

    def saveScore(self, username):
        self.update_hs_file(username, str(self.score))

    
    def update_hs_file(self, name, score):
        text = name + ' ' + score
        scores = []
        texts = []
        with open(HS_FILE, 'r') as file_to_read:
            while True:
                line = file_to_read.readline()
                if not line:
                    break
                line = line.strip('\n')
                texts.append(line)
        pos = 0
        for item in texts:
            lst = item.split()
            scores.append(int(lst[1]))
        for s in scores:
            if int(score) >= s:
                break
            else:
                pos += 1
        texts.insert(pos, text)
        x = len(texts)
        if x > 10:
            x = 10
        with open(HS_FILE, 'a') as file_to_change:
            file_to_change.seek(0)	
            file_to_change.truncate()
            for i in range(x-1):
                file_to_change.write(texts[i]+'\n')
            file_to_change.write(texts[x-1])



    # helper function to get rows x cols of matrix
    def getMatrixDimensions(self, matrix):
        return len(matrix), len(matrix[0])

    # round numpy answers to 2 dp
    def roundTo2Decimals(self, answer):
        return [round(x, 2) if not isinstance(x, list) else self.roundTo2Decimals(x) for x in answer]

    # check if submitted answer matches correct answer
    def submitAnswer(self, inputText, matrix):
        lst = eval(inputText)
        if type(lst) == int:
            lst = [lst]
        # return boolean and correct answer
        return self.checkSubmitAnswer(lst, matrix)

    def checkSubmitAnswer(self, submit_answers, matrix):
        answer = matrix.get_answer()
        if(type(answer) == int):
            answer = [answer]
        if matrix.get_question_type() == 6:
            rounded = answer
        else:
            rounded = self.roundTo2Decimals(answer)
        if len(rounded) != len(submit_answers):
            return False, rounded
        if matrix.get_question_type() == 3:
            eigenvector_answers = []
            for rounded_vector in rounded:
                eigenvector_answers.append(rounded_vector[:])
            for i in range(0, len(eigenvector_answers)):
                self.calculator.normalised(eigenvector_answers[i])
            for submit_answer in submit_answers:
                self.calculator.normalised(submit_answer)
                norm = submit_answer.copy()
                self.calculator.nagetive(submit_answer)
                nagetive_norm = submit_answer
                if norm in eigenvector_answers:
                    eigenvector_answers.remove(norm)
                elif nagetive_norm in eigenvector_answers:
                    eigenvector_answers.remove(nagetive_norm)
                else:
                    return False, rounded
            return True, rounded

        elif matrix.get_question_type() == 4:
            if len(rounded) != len(submit_answers):
                return False, rounded
            eigenvalue_answer = rounded[:]
            for item in submit_answers:
                if item not in eigenvalue_answer:
                    return False, rounded
                else:
                    eigenvalue_answer.remove(item)
            return True, rounded
        else:
            return submit_answers == answer, rounded


    # display question text on screen
    def drawMatrixQuestion(self, matrix):
        numFont = pygame.font.SysFont('Arial', 15)
        questionText = matrix.get_text()
        pygame.draw.rect(self.window, WHITE, (DISPLAY_W/2-140, 110, 280, 40))
        text = numFont.render(questionText, True, BLACK)
        self.window.blit(text, (DISPLAY_W/2-120, 120))


    # display matrix data on screen
    def drawMatrix(self, matrix):
        matrix1, matrix2 = matrix.get_matrices()[0], matrix.get_matrices()[1]
        numFont = pygame.font.SysFont('Arial', 15)

        # display matrix at centre
        if matrix2 is None:
            rows, cols = self.getMatrixDimensions(matrix1)
            for row in range(rows):
                for col in range(cols):
                    gridX = (MARGIN+GRIDBOX_W)*col+MARGIN+DISPLAY_W/2-100
                    gridY = (MARGIN+GRIDBOX_H)*row+MARGIN+200
                    pygame.draw.rect(self.window, WHITE, [gridX, gridY, GRIDBOX_W, GRIDBOX_H])

                    text = numFont.render(str(matrix1[row][col]), True, BLACK)
                    self.window.blit(text, (gridX+(GRIDBOX_W/2 - text.get_width()/2),
                                            gridY+(GRIDBOX_H/2 - text.get_height()/2)))

        # display both matrices side by side
        else:
            rows1, cols1 = self.getMatrixDimensions(matrix1)
            rows2, cols2 = self.getMatrixDimensions(matrix2)

            for row in range(rows1):
                for col in range(cols1):
                    gridX = (MARGIN+GRIDBOX_W) * col+MARGIN+DISPLAY_W/4-50
                    gridY = (MARGIN+GRIDBOX_H) * row+MARGIN+180
                    pygame.draw.rect(self.window, WHITE, [gridX, gridY, GRIDBOX_W, GRIDBOX_H])

                    text = numFont.render(str(matrix1[row][col]), True, BLACK)
                    self.window.blit(text, (gridX+(GRIDBOX_W/2 - text.get_width()/2),
                                            gridY+(GRIDBOX_H/2 - text.get_height()/2)))

            for row in range(rows2):
                for col in range(cols2):
                    gridX = (MARGIN+GRIDBOX_W)*col+MARGIN+3*DISPLAY_W/4-120
                    gridY = (MARGIN+GRIDBOX_H)*row+MARGIN+180
                    pygame.draw.rect(self.window, WHITE, [gridX, gridY, GRIDBOX_W, GRIDBOX_H])

                    text = numFont.render(str(matrix2[row][col]), True, BLACK)
                    self.window.blit(text, (gridX+(GRIDBOX_W/2 - text.get_width()/2),
                                            gridY+(GRIDBOX_H/2 - text.get_height()/2)))


    # display texts related to answer
    def drawMatrixAnswer(self):
        # if we wish to add information regarding to the formatting of answers
        # matrixType = matrix.get_question_type()
        self.window.blit(answerText, (230, 450))
        pygame.draw.rect(self.window, WHITE, answerInputTextBox)
        pygame.draw.rect(self.window, RED, submitButton)
        self.window.blit(submitText, (DISPLAY_W/2-48, 530))


    # display answer textfield
    def drawAnswerText(self, inputText):
        displayText = answerFont.render(inputText, True, BLACK)
        self.window.blit(displayText, (335, 450))
        pygame.display.update()

    # display username textfield
    def drawUsernameText(self, inputText):
        displayText = answerFont.render(inputText, True, BLACK)
        self.window.blit(displayText, (DISPLAY_W/2-150+8, DISPLAY_H/2+100+7))
        pygame.display.update()

    # display result and handle score
    def drawResult(self, result, answer):
        if result:
            text = "Your answer is correct!"
            self.score += 100
            displayText = answerFont.render(text, True, BLACK)
            self.window.blit(displayText, (355, 490))
        else:
            text = "Wrong. The correct answer is: " + str(answer)
            displayText = answerFont.render(text, True, BLACK)
            self.window.blit(displayText, (300, 490))

        pygame.display.update()

    # draw start screen
    def draw_window(self):

        self.window.fill(pygame.color.Color("grey"))
        pygame.draw.rect(self.window, RED, loadButton)
        pygame.draw.rect(self.window, RED, generateButton)
        self.window.blit(loadText, (DISPLAY_W/2-70 + 17, DISPLAY_H/2-100 + 10))
        self.window.blit(generateText, (DISPLAY_W/2-130 + 12, DISPLAY_H/2+100 + 10))
        pygame.display.set_caption("Load Matrix From File")
        pygame.display.update()


    # draw matrix to screen
    def draw_matrix_window(self, matrix):
        self.window.fill(pygame.color.Color("grey"))
        pygame.draw.rect(self.window, RED, smallLoadButton)
        pygame.draw.rect(self.window, RED, smallGenerateButton)
        pygame.draw.rect(self.window, RED, prevButton)
        pygame.draw.rect(self.window, RED, nextButton)
        pygame.draw.rect(self.window, RED, endButton)

        scoreText = answerFont.render("Score: " + str(self.score), True, BLACK)
        self.window.blit(smallLoadText, (20 + 8, 20 + 10))
        self.window.blit(smallGenerateText, (20 + 8, 70 + 10))
        self.window.blit(prevText, (DISPLAY_W/2-220 + 8, 40 + 10))
        self.window.blit(nextText, (DISPLAY_W/2+60 + 40, 40 + 10))
        self.window.blit(scoreText, (DISPLAY_W-130, 50))
        self.window.blit(endText, (DISPLAY_W-150, 90))

        self.drawMatrixQuestion(matrix)
        self.drawMatrix(matrix)
        self.drawMatrixAnswer()
        pygame.display.set_caption("Practice Questions")
        pygame.display.flip()

    # display summary page
    def drawEndScreen(self):
        self.window.fill(pygame.color.Color("grey"))
        scoreText = defaultFont.render("Score: " + str(self.score), True, BLACK)
        self.window.blit(scoreText, (DISPLAY_W/2-50, DISPLAY_H/2-100))
        correctText = defaultFont.render("Number of correct questions: " + str(self.score//100), True, BLACK)
        self.window.blit(correctText, (DISPLAY_W/2-140, DISPLAY_H/2-30))
        self.window.blit(usernameText, (DISPLAY_W/2-50, DISPLAY_H/2+50))
        pygame.draw.rect(self.window, WHITE, usernameInputTextBox)
        pygame.draw.rect(self.window, RED, saveButton)
        self.window.blit(saveText, (DISPLAY_W/2+200, DISPLAY_H/2+100))
        pygame.draw.rect(self.window, RED, mainMenuButton)
        self.window.blit(mainMenuText, (DISPLAY_W/2-100+22, DISPLAY_H/2+200+15))

        pygame.display.set_caption("Summary Page")
        pygame.display.flip()

    # main window
    def main(self):
        running = True
        exerciseIndex = 0
        inputText = ""
        usernameInputText = ""
        answerInputBoxActive = False
        usernameInputBoxActive = False
        mainMenuActive = True
        practiceScreenActive = False
        answerSubmitted = False
        USERNAME_TEXTBOX_MAX_LENGTH = 30
        clock = pygame.time.Clock()

        self.draw_window()
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos       # get mouse position

                    # checks if mouse position is over buttons

                    if loadButton.collidepoint(mouse_pos) and mainMenuActive \
                            or smallLoadButton.collidepoint(mouse_pos) and practiceScreenActive:
                        try:
                            self.prompt_file()
                            self.matrixList = self.loadData()
                            self.draw_matrix_window(self.matrixList[0])
                            mainMenuActive = False
                            practiceScreenActive = True
                        except IndexError:
                            pass
                        finally:
                            exerciseIndex = 0
                            inputText = ""
                            answerSubmitted = False


                    elif generateButton.collidepoint(mouse_pos) and mainMenuActive \
                            or smallGenerateButton.collidepoint(mouse_pos) and practiceScreenActive:
                        self.matrixList = self.generateData()
                        if(DEBUG):
                            question_number = 1
                            print("=============Question Answers=============")
                            for question in self.matrixList:
                                print("Question number %d, answer: %s" % (question_number, question.get_answer()))
                                question_number += 1
                            print("================== END ==================")
                        self.draw_matrix_window(self.matrixList[0])
                        inputText = ""
                        exerciseIndex = 0
                        answerSubmitted = False
                        mainMenuActive = False
                        practiceScreenActive = True

                    elif nextButton.collidepoint(mouse_pos):
                        try:
                            exerciseIndex += 1
                            self.draw_matrix_window(self.matrixList[exerciseIndex])
                            inputText = ""
                            answerSubmitted = False
                        except IndexError:
                            exerciseIndex -= 1

                    elif prevButton.collidepoint(mouse_pos) and exerciseIndex > 0:
                        try:
                            exerciseIndex -= 1
                            self.draw_matrix_window(self.matrixList[exerciseIndex])
                            inputText = ""
                            answerSubmitted = False
                        except IndexError:
                            exerciseIndex += 1

                    elif answerInputTextBox.collidepoint(mouse_pos) and not answerSubmitted and practiceScreenActive:
                        pygame.draw.rect(self.window, TEXTBOX_ACTIVE, answerInputTextBox)
                        answerInputBoxActive = True

                    elif usernameInputTextBox.collidepoint(mouse_pos) and not practiceScreenActive:
                        pygame.draw.rect(self.window, TEXTBOX_ACTIVE, usernameInputTextBox)
                        usernameInputBoxActive = True

                    elif submitButton.collidepoint(mouse_pos) and practiceScreenActive:
                        pygame.draw.rect(self.window, WHITE, answerInputTextBox)
                        if inputText == "":
                            break
                        self.drawAnswerText(inputText)
                        try:
                            result, answer = self.submitAnswer(inputText, self.matrixList[exerciseIndex])
                            self.drawResult(result, answer)
                        except TypeError:
                            print("Input must be of type list")
                        answerInputBoxActive = False
                        answerSubmitted = True

                    elif endButton.collidepoint(mouse_pos) and practiceScreenActive:
                        practiceScreenActive = False
                        self.drawEndScreen()

                    elif saveButton.collidepoint(mouse_pos) and not mainMenuActive and not practiceScreenActive:
                        self.saveScore(usernameInputText)
                        pygame.display.set_caption(TITLE)
                        running = False

                    elif mainMenuButton.collidepoint(mouse_pos) and not mainMenuActive and not practiceScreenActive:
                        pygame.display.set_caption(TITLE)
                        running = False
                        

                # if key pressed and input box has been clicked
                elif event.type == pygame.KEYDOWN and answerInputBoxActive:
                    # ENTER key pressed
                    if event.key == pygame.K_RETURN:
                        pygame.draw.rect(self.window, WHITE, answerInputTextBox)
                        if inputText == "":
                            break
                        self.drawAnswerText(inputText)
                        try:
                            result, answer = self.submitAnswer(inputText, self.matrixList[exerciseIndex])
                            self.drawResult(result, answer)
                        except TypeError:
                            print("Input must be of type list")
                        answerInputBoxActive = False
                        answerSubmitted = True

                    # BACKSPACE key pressed
                    elif event.key == pygame.K_BACKSPACE:
                        inputText = inputText[:-1]
                        if len(inputText) >= TEXTBOX_MAX_LENGTH:
                            trimmedText = inputText[-TEXTBOX_MAX_LENGTH:]
                            pygame.draw.rect(self.window, TEXTBOX_ACTIVE, answerInputTextBox)
                            self.drawAnswerText(trimmedText)
                        else:
                            pygame.draw.rect(self.window, TEXTBOX_ACTIVE, answerInputTextBox)
                            self.drawAnswerText(inputText)

                    else:
                        inputText += event.unicode
                        if len(inputText) >= TEXTBOX_MAX_LENGTH:
                            trimmedText = inputText[-TEXTBOX_MAX_LENGTH:]
                            pygame.draw.rect(self.window, TEXTBOX_ACTIVE, answerInputTextBox)
                            self.drawAnswerText(trimmedText)
                        else:
                            self.drawAnswerText(inputText)

                # if key pressed and username input box has been clicked
                elif event.type == pygame.KEYDOWN and usernameInputBoxActive:
                    # ENTER key pressed
                    if event.key == pygame.K_RETURN:
                        pygame.draw.rect(self.window, WHITE, usernameInputTextBox)
                        if usernameInputText == "":
                            break
                        self.drawUsernameText(usernameInputText)
                        usernameInputBoxActive = False
                        answerSubmitted = True
                    # BACKSPACE key pressed
                    elif event.key == pygame.K_BACKSPACE:
                        usernameInputText = usernameInputText[:-1]
                        if len(usernameInputText) >= USERNAME_TEXTBOX_MAX_LENGTH:
                            trimmedText = usernameInputText[-USERNAME_TEXTBOX_MAX_LENGTH:]
                            pygame.draw.rect(self.window, TEXTBOX_ACTIVE, usernameInputTextBox)
                            self.drawUsernameText(trimmedText)
                        else:
                            pygame.draw.rect(self.window, TEXTBOX_ACTIVE, usernameInputTextBox)
                            self.drawUsernameText(usernameInputText)

                    else:
                        usernameInputText += event.unicode
                        if len(usernameInputText) >= USERNAME_TEXTBOX_MAX_LENGTH:
                            trimmedText = usernameInputText[-USERNAME_TEXTBOX_MAX_LENGTH:]
                            pygame.draw.rect(self.window, TEXTBOX_ACTIVE, usernameInputTextBox)
                            self.drawUsernameText(trimmedText)
                        else:
                            self.drawUsernameText(usernameInputText)

            pygame.display.update()
            # limit frames
            clock.tick(FPS)
