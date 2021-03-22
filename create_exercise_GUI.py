# create_exercise GUI

"""
BASIC STRUCTURE OF GUI:
- make a basic frame window - WIDTH: 960 ; HEIGHT: 580
- important components:
    - COVER PAGE
        - "CREATE EXERCISE" title
        - textbox for user input of file name
        - get number input from user for number of questions
        - "START CREATING" button - go to EDITOR page
    - EDITOR PAGE
        - todo | question number
        - todo | radio button for user input for type of question : eigenvector ; eigenvalue ; inverse ; determinant ; addition ; subtraction ; multiplication
        - todo | textbox spaces for number user input of matrix elements
        - todo | previous question button
        - todo | next question button
    - CONFIRM PAGE
        - todo | "questions confirmed? ready for export" title
        - todo | "yes" button - get pop-up notification to inform file exported, go to HOME page
        - todo | "no" button - go to (first?)/last question EDITOR page
- every (component)/(page) should be a class on its own (?) - pygame how to change pages
"""

import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 960, 580
WINDOW_TITLE = "Matrix Exercise Application"  # or whatever it is
WINDOW_BACKGROUND_COLOR = (0, 0, 0)  # black
TITLE_TEXT_COLOR = (255, 255, 255)  # white
INPUT_TEXTBOX_COLOR_INACTIVE = (255, 255, 255)  # white
INPUT_TEXTBOX_COLOR_ACTIVE = (137, 209, 254)  # light blue
INPUT_TEXT_COLOR = (0, 0, 0)  # black
QUESTION_BUTTON_COLOR = (34, 34, 34)  # dark grey
START_BUTTON_COLOR = (255, 255, 255)  # white
START_BUTTON_PRESSED_COLOR = (137, 209, 254)  # light blue


# this class handles drawing the objects on the window for COVER page (or including all functionality of cover page?)
class CoverPage:
    pass


class EditorPage:
    pass


class ConfirmPage:
    pass


class MatrixEditor:
    # not sure if need __init__

    # this main method should (handle user events &) moving between pages
    def main(self):
        pygame.init()

        # todo - this should remain in this main() function
        ''' initialise GUI window '''
        window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        pygame.display.set_caption(WINDOW_TITLE)

        ''' fill in background colour '''
        window.fill(WINDOW_BACKGROUND_COLOR)

        ''' print "CREATE EXERCISE" title onto window '''
        cover_page_header_font = pygame.font.SysFont("futura", 55)  # todo - temp font, change to 'wonder-bit'
        cover_page_header_text = cover_page_header_font.render("CREATE EXERCISE", True, TITLE_TEXT_COLOR)
        window.blit(cover_page_header_text, (60, 80))

        ''' create text input box for file name '''
        # print "name of file" title on window
        name_of_file_title_font = pygame.font.SysFont("futura", 35)  # todo - temp font, change to 'wonder-bit'
        name_of_file_title_text = name_of_file_title_font.render("NAME OF FILE:", True, TITLE_TEXT_COLOR)
        window.blit(name_of_file_title_text, (60, 190))
        # draw rectangle for text box
        file_input_textbox = pygame.Rect(350, 190, 500, 50)  # (x , y, width, height)
        pygame.draw.rect(window, INPUT_TEXTBOX_COLOR_INACTIVE, file_input_textbox)
        # format text & setup
        file_input_text = ""
        file_input_text_font = pygame.font.SysFont("courier new", 25)
        active = False

        ''' create 'number of questions' number box & buttons '''
        # print "number of questions" title on window
        no_of_question_title_font = pygame.font.SysFont("futura", 25)  # todo - temp font, change to 'wonder-bit'
        no_of_question_title_text = no_of_question_title_font.render("NUMBER OF QUESTIONS:", True, TITLE_TEXT_COLOR)
        window.blit(no_of_question_title_text, (60, 285))
        # draw rectangle for number box
        question_no_input_textbox = pygame.Rect(395, 275, 97, 53)
        pygame.draw.rect(window, INPUT_TEXTBOX_COLOR_INACTIVE, question_no_input_textbox)
        # format number in box & print initial number
        no_of_question = 1
        no_of_question_font = pygame.font.SysFont("courier new", 30)
        no_of_question_text = no_of_question_font.render(str(no_of_question), True, INPUT_TEXT_COLOR)
        window.blit(no_of_question_text, (409, 285))
        # create 'increase number of questions' triangle button
        pygame.draw.polygon(window, QUESTION_BUTTON_COLOR, [(457, 300), (467, 280), (477, 300)])
        increase_no_button_rect = pygame.Rect(455, 280, 25, 20)
        # create 'decrease number of questions' triangle button
        pygame.draw.polygon(window, QUESTION_BUTTON_COLOR, [(457, 304), (467, 324), (477, 304)])
        decrease_no_button_rect = pygame.Rect(455, 305, 25, 20)

        ''' create "START CREATING" button '''
        # print "START CREATING" title on window
        start_creating_title_font = pygame.font.SysFont("futura", 25)  # todo - temp font, change to 'wonder-bit'
        start_creating_title_clicked_text = start_creating_title_font.render("START CREATING", True, TITLE_TEXT_COLOR)
        window.blit(start_creating_title_clicked_text, (350, 410))
        # draw triangle for button
        pygame.draw.polygon(window, START_BUTTON_COLOR, [(585, 395), (585, 455), (645, 425)])
        # create rectangle for button
        start_creating_button = pygame.Rect(340, 385, 320, 80)

        ''' initial DISPLAY everything on window '''
        pygame.display.flip()

        running = True
        while running:
            pygame.time.Clock().tick(60)

            # handling events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # clicking events #
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # if input box is clicked
                    if file_input_textbox.collidepoint(event.pos):
                        pygame.draw.rect(window, INPUT_TEXTBOX_COLOR_ACTIVE, file_input_textbox)
                        file_input_text_display = file_input_text_font.render(file_input_text, True, INPUT_TEXT_COLOR)
                        window.blit(file_input_text_display, (365, 200))
                        active = True
                        pygame.display.update()

                    # if upper question button clicked
                    if increase_no_button_rect.collidepoint(event.pos):
                        no_of_question += 1
                        pygame.draw.rect(window, INPUT_TEXTBOX_COLOR_INACTIVE, question_no_input_textbox)
                        pygame.draw.polygon(window, QUESTION_BUTTON_COLOR, [(467, 280), (457, 300), (477, 300)])
                        pygame.draw.polygon(window, QUESTION_BUTTON_COLOR, [(457, 304), (467, 324), (477, 304)])
                        no_of_question_text = no_of_question_font.render(str(no_of_question), True, INPUT_TEXT_COLOR)
                        window.blit(no_of_question_text, (409, 285))
                        pygame.display.update()

                    # if lower question button clicked
                    if decrease_no_button_rect.collidepoint(event.pos):
                        # decrease only if the number is greater than 1
                        if no_of_question > 1:
                            no_of_question -= 1
                            pygame.draw.rect(window, INPUT_TEXTBOX_COLOR_INACTIVE, question_no_input_textbox)
                            pygame.draw.polygon(window, QUESTION_BUTTON_COLOR, [(467, 280), (457, 300), (477, 300)])
                            pygame.draw.polygon(window, QUESTION_BUTTON_COLOR, [(457, 304), (467, 324), (477, 304)])
                            no_of_question_text = no_of_question_font.render(str(no_of_question), True, INPUT_TEXT_COLOR)
                            window.blit(no_of_question_text, (409, 285))
                            pygame.display.update()

                    # if "START CREATING" button clicked
                    if start_creating_button.collidepoint(event.pos):
                        start_creating_title_clicked_text = start_creating_title_font.render(
                                             "START CREATING", True, START_BUTTON_PRESSED_COLOR)
                        window.blit(start_creating_title_clicked_text, (350, 410))
                        pygame.draw.polygon(window, START_BUTTON_PRESSED_COLOR, [(585, 395), (585, 455), (645, 425)])
                        print(file_input_text)  # final file name
                        print(no_of_question)  # final number of questions
                        pygame.display.update()
                        pygame.time.wait(500)  # 0.5 second delay
                        # todo - bottom 2 might not be part of this method
                        window.fill(WINDOW_BACKGROUND_COLOR)  # go to EDITOR page
                        pygame.display.update()

                # if text input box was clicked & user types on keyboard #
                elif event.type == pygame.KEYDOWN and active:
                    # confirms file name & stops further changes to name
                    if event.key == pygame.K_RETURN:
                        pygame.draw.rect(window, INPUT_TEXTBOX_COLOR_INACTIVE, file_input_textbox)
                        file_input_text_display = file_input_text_font.render(file_input_text, True, INPUT_TEXT_COLOR)
                        window.blit(file_input_text_display, (365, 200))
                        active = False
                        pygame.display.update()

                    # deletes some characters
                    elif event.key == pygame.K_BACKSPACE:
                        file_input_text = file_input_text[:-1]
                        pygame.draw.rect(window, INPUT_TEXTBOX_COLOR_ACTIVE, file_input_textbox)
                        file_input_text_display = file_input_text_font.render(file_input_text, True, INPUT_TEXT_COLOR)
                        window.blit(file_input_text_display, (365, 200))
                        pygame.display.update()

                    # types normal characters
                    else:
                        file_input_text += event.unicode
                        file_input_text_display = file_input_text_font.render(file_input_text, True, INPUT_TEXT_COLOR)
                        window.blit(file_input_text_display, (365, 200))
                        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    matrix_editor = MatrixEditor()
    matrix_editor.main()
