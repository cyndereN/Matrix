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
- todo - move necessary code to other classes & split into more concise methods
- todo - use methods to create 'objects' within classes
- !! only constants are all caps !!
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
RECT_BORDER_COLOR = (255, 255, 255)  # white
FPS = 60


# this class handles drawing the objects on the window for COVER page & all functionality
class CoverPage:
    def __init__(self, window):
        self.window = window
        self.running = True
        # file name input textbox
        self.file_input_textbox = None
        self.file_input_text = ""
        self.file_input_text_font = pygame.font.SysFont("courier new", 25)
        self.input_box_active = False
        # no of questions number box
        self.no_of_question = 1
        self.question_no_input_textbox = None
        self.no_of_question_font = pygame.font.SysFont("courier new", 30)
        self.increase_no_button_rect = None
        self.decrease_no_button_rect = None
        # start creating button
        self.start_creating_button = None
        self.start_creating_title_font = pygame.font.SysFont("futura", 25)  # todo - temp font, change to 'wonder-bit'

    def print_create_exercise_title(self):
        """ print "CREATE EXERCISE" title onto window """
        cover_page_header_font = pygame.font.SysFont("futura", 55)  # todo - temp font, change to 'wonder-bit'
        cover_page_header_text = cover_page_header_font.render("CREATE EXERCISE", True, TITLE_TEXT_COLOR)
        self.window.blit(cover_page_header_text, (60, 80))

    def create_text_input_box_file_name(self):
        """ create text input box for file name """
        # print "name of file" title on window
        name_of_file_title_font = pygame.font.SysFont("futura", 35)  # todo - temp font, change to 'wonder-bit'
        name_of_file_title_text = name_of_file_title_font.render("NAME OF FILE:", True, TITLE_TEXT_COLOR)
        self.window.blit(name_of_file_title_text, (60, 190))
        # draw rectangle for text box
        self.file_input_textbox = pygame.Rect(350, 190, 500, 50)  # (x , y, width, height)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.file_input_textbox)

    def create_no_of_question_number_box(self):
        """ create 'number of questions' number box & buttons """
        # print "number of questions" title on window
        no_of_question_title_font = pygame.font.SysFont("futura", 25)  # todo - temp font, change to 'wonder-bit'
        no_of_question_title_text = no_of_question_title_font.render("NUMBER OF QUESTIONS:", True, TITLE_TEXT_COLOR)
        self.window.blit(no_of_question_title_text, (60, 285))
        # draw rectangle for number box
        self.question_no_input_textbox = pygame.Rect(395, 275, 97, 53)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.question_no_input_textbox)
        # print initial number in box
        no_of_question_text = self.no_of_question_font.render(str(self.no_of_question), True, INPUT_TEXT_COLOR)
        self.window.blit(no_of_question_text, (409, 285))
        # create 'increase number of questions' triangle button
        pygame.draw.polygon(self.window, QUESTION_BUTTON_COLOR, [(457, 300), (467, 280), (477, 300)])
        self.increase_no_button_rect = pygame.Rect(455, 280, 25, 20)
        # create 'decrease number of questions' triangle button
        pygame.draw.polygon(self.window, QUESTION_BUTTON_COLOR, [(457, 304), (467, 324), (477, 304)])
        self.decrease_no_button_rect = pygame.Rect(455, 305, 25, 20)

    def create_start_creating_button(self):
        """ create "START CREATING" button """
        # print "START CREATING" title on window
        start_creating_title_clicked_text = self.start_creating_title_font.render("START CREATING", True,
                                                                                  TITLE_TEXT_COLOR)
        self.window.blit(start_creating_title_clicked_text, (350, 410))
        # draw triangle for button
        pygame.draw.polygon(self.window, START_BUTTON_COLOR, [(585, 395), (585, 455), (645, 425)])
        # create rectangle for button
        self.start_creating_button = pygame.Rect(340, 385, 320, 80)

    def go(self):
        self.window.fill(WINDOW_BACKGROUND_COLOR)

        ''' create COVER page components '''
        self.print_create_exercise_title()
        self.create_text_input_box_file_name()
        self.create_no_of_question_number_box()
        self.create_start_creating_button()

        ''' initial DISPLAY everything on window '''
        pygame.display.flip()

        while self.running:
            pygame.time.Clock().tick(FPS)

            ''' handling events '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # TODO - might move some of these into methods
                # clicking events #
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # if input box is clicked
                    if self.file_input_textbox.collidepoint(event.pos):
                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.file_input_textbox)
                        file_input_text_display = self.file_input_text_font.render(self.file_input_text, True,
                                                                                   INPUT_TEXT_COLOR)
                        self.window.blit(file_input_text_display, (365, 200))
                        self.input_box_active = True
                        pygame.display.update()

                    # if upper question button clicked
                    elif self.increase_no_button_rect.collidepoint(event.pos):
                        self.no_of_question += 1
                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.question_no_input_textbox)
                        pygame.draw.polygon(self.window, QUESTION_BUTTON_COLOR, [(467, 280), (457, 300), (477, 300)])
                        pygame.draw.polygon(self.window, QUESTION_BUTTON_COLOR, [(457, 304), (467, 324), (477, 304)])
                        no_of_question_text = self.no_of_question_font.render(
                            str(self.no_of_question), True, INPUT_TEXT_COLOR)
                        self.window.blit(no_of_question_text, (409, 285))
                        pygame.display.update()

                    # if lower question button clicked
                    elif self.decrease_no_button_rect.collidepoint(event.pos):
                        # decrease only if the number is greater than 1
                        if self.no_of_question > 1:
                            self.no_of_question -= 1
                            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.question_no_input_textbox)
                            pygame.draw.polygon(self.window, QUESTION_BUTTON_COLOR,
                                                [(467, 280), (457, 300), (477, 300)])
                            pygame.draw.polygon(self.window, QUESTION_BUTTON_COLOR,
                                                [(457, 304), (467, 324), (477, 304)])
                            no_of_question_text = self.no_of_question_font.render(
                                str(self.no_of_question), True, INPUT_TEXT_COLOR)
                            self.window.blit(no_of_question_text, (409, 285))
                            pygame.display.update()

                    # if "START CREATING" button clicked
                    elif self.start_creating_button.collidepoint(event.pos):
                        start_creating_title_clicked_text = self.start_creating_title_font.render(
                            "START CREATING", True, START_BUTTON_PRESSED_COLOR)
                        self.window.blit(start_creating_title_clicked_text, (350, 410))
                        pygame.draw.polygon(self.window, START_BUTTON_PRESSED_COLOR,
                                            [(585, 395), (585, 455), (645, 425)])
                        pygame.display.update()
                        pygame.time.wait(400)  # 0.4 second delay
                        self.running = False
                        return self.file_input_text, self.no_of_question

                # if text input box was clicked & user types on keyboard #
                elif event.type == pygame.KEYDOWN and self.input_box_active:
                    # confirms file name & stops further changes to name
                    if event.key == pygame.K_RETURN:
                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.file_input_textbox)
                        file_input_text_display = self.file_input_text_font.render(self.file_input_text, True,
                                                                                   INPUT_TEXT_COLOR)
                        self.window.blit(file_input_text_display, (365, 200))
                        self.input_box_active = False
                        pygame.display.update()

                    # deletes some characters
                    elif event.key == pygame.K_BACKSPACE:
                        self.file_input_text = self.file_input_text[:-1]
                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.file_input_textbox)
                        file_input_text_display = self.file_input_text_font.render(self.file_input_text, True,
                                                                                   INPUT_TEXT_COLOR)
                        self.window.blit(file_input_text_display, (365, 200))
                        pygame.display.update()

                    # types normal characters
                    else:
                        self.file_input_text += event.unicode
                        file_input_text_display = self.file_input_text_font.render(self.file_input_text, True,
                                                                                   INPUT_TEXT_COLOR)
                        self.window.blit(file_input_text_display, (365, 200))
                        pygame.display.update()


class EditorPage:
    def __init__(self, window, file_name, no_of_q):
        self.window = window
        self.running = True
        self.file_name = file_name
        self.no_of_q = no_of_q

    def go(self):
        self.window.fill(WINDOW_BACKGROUND_COLOR)

        # todo - refer to format of Question class & how matrix numbers are stored
        ''' initialise Question list & pointer '''
        question_set = []
        current_q = 1  # pointer

        ''' print current Q number '''
        # draw rectangle border
        question_no_rect = pygame.Rect(10, 10, 100, 50)
        pygame.draw.rect(self.window, RECT_BORDER_COLOR, question_no_rect, 1)
        # print question number text

        ''' initial DISPLAY everything on window '''
        pygame.display.flip()

        while self.running:
            pygame.time.Clock().tick(FPS)

            ''' handling events '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


class ConfirmPage:
    pass


class MatrixEditor:
    # not sure if need __init__

    # this main method should (handle user events &) moving between pages
    def main(self):
        pygame.init()

        ''' initialise GUI window '''
        window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        pygame.display.set_caption(WINDOW_TITLE)

        ''' start off the COVER page '''
        cover_page = CoverPage(window)
        file_name, no_of_q = cover_page.go()
        print("FINAL file name: ", file_name)
        print("FINAL no of q: ", no_of_q)

        ''' move onto EDITOR page '''
        editor_page = EditorPage(window, file_name, no_of_q)
        editor_page.go()


if __name__ == "__main__":
    matrix_editor = MatrixEditor()
    matrix_editor.main()
