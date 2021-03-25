# create_exercise GUI

import pygame, sys
from settings import *
from create_exercise import Create_Exercise


# this class handles drawing the objects on the window for COVER page & its functionality
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
        self.start_creating_title_font = pygame.font.Font(FONT_2, 18)

    def print_create_exercise_title(self):
        """ print "CREATE EXERCISE" title onto window """
        cover_page_header_font = pygame.font.Font(FONT_1, 45)
        cover_page_header_text = cover_page_header_font.render("CREATE EXERCISE", True, TITLE_TEXT_COLOR)
        self.window.blit(cover_page_header_text, (60, 90))

    def create_text_input_box_file_name(self):
        """ create text input box for file name """
        # print "name of file" title on window
        name_of_file_title_font = pygame.font.Font(FONT_2, 22)
        name_of_file_title_text = name_of_file_title_font.render("NAME OF FILE:", True, TITLE_TEXT_COLOR)
        self.window.blit(name_of_file_title_text, (60, 202))
        # draw rectangle for text box
        self.file_input_textbox = pygame.Rect(350, 190, 500, 50)  # (x , y, width, height)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.file_input_textbox)

    def create_no_of_question_number_box(self):
        """ create 'number of questions' number box & buttons """
        # print "number of questions" title on window
        no_of_question_title_font = pygame.font.Font(FONT_2, 16)
        no_of_question_title_text = no_of_question_title_font.render("NUMBER OF QUESTIONS:", True, TITLE_TEXT_COLOR)
        self.window.blit(no_of_question_title_text, (60, 290))
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
        self.window.blit(start_creating_title_clicked_text, (312, 414))
        # draw triangle for button
        pygame.draw.polygon(self.window, BUTTON_COLOR, [(585, 395), (585, 455), (645, 425)])
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
                    self.file_input_text = None
                    self.no_of_question = None
                    self.running = False
                    pygame.quit()
                    return self.file_input_text, self.no_of_question

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
                            "START CREATING", True, BUTTON_PRESSED_COLOR)
                        self.window.blit(start_creating_title_clicked_text, (312, 414))
                        pygame.draw.polygon(self.window, BUTTON_PRESSED_COLOR,
                                            [(585, 395), (585, 455), (645, 425)])
                        pygame.display.update()
                        pygame.time.wait(100)  # 0.1 second delay
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


# this class handles drawing the objects on the window for EDITOR & CONFIRMATION page & its functionality
class EditorPage:
    def __init__(self, window, file_name, no_of_q):
        self.window = window
        self.running = True
        self.file_name = file_name
        self.no_of_q = no_of_q
        self.creator = Create_Exercise(no_of_q)  # initialise empty exercise_set
        self.current_q = 1  # pointer - current question
        self.q_type = -1  # initialise question type
        # radio buttons
        self.add_button = None; self.sub_button = None; self.mult_button = None
        self.egvec_button = None; self.egval_button = None; self.inv_button = None; self.det_button = None
        # next question button
        self.next_q_button = None
        # ONE template - matrix numbers
        self.r1c1, self.r1c2, self.r1c3 = "", "", ""
        self.r2c1, self.r2c2, self.r2c3 = "", "", ""
        self.r3c1, self.r3c2, self.r3c3 = "", "", ""
        # ONE template - matrix boxes
        self.r1c1_box, self.r1c2_box, self.r1c3_box = None, None, None
        self.r2c1_box, self.r2c2_box, self.r2c3_box = None, None, None
        self.r3c1_box, self.r3c2_box, self.r3c3_box = None, None, None
        # ONE template - number for storing which box is active
        self.ONE_active = 0  # i.e. if mat1_r1c3_box active then ONE_active = 13
        # TWO template - matrix_1 numbers
        self.mat1_r1c1, self.mat1_r1c2, self.mat1_r1c3 = "", "", ""
        self.mat1_r2c1, self.mat1_r2c2, self.mat1_r2c3 = "", "", ""
        self.mat1_r3c1, self.mat1_r3c2, self.mat1_r3c3 = "", "", ""
        # TWO template - matrix_1 boxes
        self.mat1_r1c1_box, self.mat1_r1c2_box, self.mat1_r1c3_box = None, None, None
        self.mat1_r2c1_box, self.mat1_r2c2_box, self.mat1_r2c3_box = None, None, None
        self.mat1_r3c1_box, self.mat1_r3c2_box, self.mat1_r3c3_box = None, None, None
        # TWO template - matrix_2 numbers
        self.mat2_r1c1, self.mat2_r1c2, self.mat2_r1c3 = "", "", ""
        self.mat2_r2c1, self.mat2_r2c2, self.mat2_r2c3 = "", "", ""
        self.mat2_r3c1, self.mat2_r3c2, self.mat2_r3c3 = "", "", ""
        # TWO template - matrix_2 boxes
        self.mat2_r1c1_box, self.mat2_r1c2_box, self.mat2_r1c3_box = None, None, None
        self.mat2_r2c1_box, self.mat2_r2c2_box, self.mat2_r2c3_box = None, None, None
        self.mat2_r3c1_box, self.mat2_r3c2_box, self.mat2_r3c3_box = None, None, None
        # TWO template - number for storing which box is active
        self.TWO_active = 0  # i.e. if mat2_r1c3_box active then TWO_active = 213
        # font for "matrix <number>" title
        self.matrix_no_title_font = pygame.font.Font(FONT_2, 20)
        # font for matrix input number
        self.ONE_matrix_input_num_font = pygame.font.SysFont("courier new", 30)
        self.TWO_matrix_input_num_font = pygame.font.SysFont("courier new", 27)
        # confirmation page button
        self.export_file_button = None

    def print_current_q_number(self):
        """ print current Q number (i.e. Q1) """
        # draw rectangle border
        question_no_rect = pygame.Rect(30, 30, WINDOW_WIDTH - 63, 70)
        pygame.draw.rect(self.window, RECT_BORDER_COLOR, question_no_rect, 3)
        # print question number text
        question_no_text = "QUESTION " + str(self.current_q) + " OF " + str(self.no_of_q)
        question_no_text_font = pygame.font.Font(FONT_2, 25)
        question_no_text_display = question_no_text_font.render(question_no_text, True, TITLE_TEXT_COLOR)
        self.window.blit(question_no_text_display, (50, 52))

    def print_choose_q_type_title(self):
        """ create "CHOOSE TYPE OF QUESTION" title """
        # draw rectangle border
        question_type_title_rect = pygame.Rect(30, 125, 350, 50)
        pygame.draw.rect(self.window, RECT_BORDER_COLOR, question_type_title_rect, 3)
        # print text
        question_type_title_font = pygame.font.Font(FONT_2, 13)
        question_type_title_text = question_type_title_font.render("CHOOSE TYPE OF QUESTION:", True, TITLE_TEXT_COLOR)
        self.window.blit(question_type_title_text, (50, 144))

    def create_q_type_radio_checklist(self):
        """ create question type radio button checklist """
        # draw rectangle border
        question_type_rect = pygame.Rect(30, 200, 350, 350)
        pygame.draw.rect(self.window, RECT_BORDER_COLOR, question_type_rect, 3)
        # create ADDITION option #
        # create radio button
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 240), 15)
        # create rectangle for button
        self.add_button = pygame.Rect(50, 225, 30, 30)  # x-15, y-15
        # print text
        question_type_font = pygame.font.Font(FONT_2, 18)  # same for all
        q_type_add_text = question_type_font.render("ADDITION", True, TITLE_TEXT_COLOR)
        self.window.blit(q_type_add_text, (95, 231))
        # create SUBTRACTION button #
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 285), 15)
        self.sub_button = pygame.Rect(50, 270, 30, 30)
        q_type_sub_text = question_type_font.render("SUBTRACTION", True, TITLE_TEXT_COLOR)
        self.window.blit(q_type_sub_text, (95, 276))
        # create MULTIPLICATION button #
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 330), 15)
        self.mult_button = pygame.Rect(50, 315, 30, 30)
        q_type_mult_text = question_type_font.render("MULTIPLICATION", True, TITLE_TEXT_COLOR)
        self.window.blit(q_type_mult_text, (95, 321))
        # create EIGENVECTOR button #
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 375), 15)
        self.egvec_button = pygame.Rect(50, 360, 30, 30)
        q_type_egvec_text = question_type_font.render("EIGENVECTOR", True, TITLE_TEXT_COLOR)
        self.window.blit(q_type_egvec_text, (95, 366))
        # create EIGENVALUE button #
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 420), 15)
        self.egval_button = pygame.Rect(50, 405, 30, 30)
        q_type_egval_text = question_type_font.render("EIGENVALUE", True, TITLE_TEXT_COLOR)
        self.window.blit(q_type_egval_text, (95, 411))
        # create INVERSE button #
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 465), 15)
        self.inv_button = pygame.Rect(50, 450, 30, 30)
        q_type_inv_text = question_type_font.render("INVERSE", True, TITLE_TEXT_COLOR)
        self.window.blit(q_type_inv_text, (95, 456))
        # create DETERMINANT button #
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 510), 15)
        self.det_button = pygame.Rect(50, 495, 30, 30)
        q_type_det_text = question_type_font.render("DETERMINANT", True, TITLE_TEXT_COLOR)
        self.window.blit(q_type_det_text, (95, 501))

    def mark_chosen_button(self):
        # first remove any previous mark
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 240), 15)
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 285), 15)
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 330), 15)
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 375), 15)
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 420), 15)
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 465), 15)
        pygame.draw.circle(self.window, BUTTON_COLOR, (65, 510), 15)
        # mark chosen button blue
        if self.q_type == 0:
            pygame.draw.circle(self.window, BUTTON_PRESSED_COLOR, (65, 240), 10)
        elif self.q_type == 1:
            pygame.draw.circle(self.window, BUTTON_PRESSED_COLOR, (65, 285), 10)
        elif self.q_type == 2:
            pygame.draw.circle(self.window, BUTTON_PRESSED_COLOR, (65, 330), 10)
        elif self.q_type == 3:
            pygame.draw.circle(self.window, BUTTON_PRESSED_COLOR, (65, 375), 10)
        elif self.q_type == 4:
            pygame.draw.circle(self.window, BUTTON_PRESSED_COLOR, (65, 420), 10)
        elif self.q_type == 5:
            pygame.draw.circle(self.window, BUTTON_PRESSED_COLOR, (65, 465), 10)
        elif self.q_type == 6:
            pygame.draw.circle(self.window, BUTTON_PRESSED_COLOR, (65, 510), 10)

    def draw_ONE_matrix_template(self):
        # remove previous matrix templates
        blank_rect = pygame.Rect(398, 119, 535, 373)
        pygame.draw.rect(self.window, WINDOW_BACKGROUND_COLOR, blank_rect)
        # remove TWO components
        self.mat1_r1c1_box, self.mat1_r1c2_box, self.mat1_r1c3_box = None, None, None
        self.mat1_r2c1_box, self.mat1_r2c2_box, self.mat1_r2c3_box = None, None, None
        self.mat1_r3c1_box, self.mat1_r3c2_box, self.mat1_r3c3_box = None, None, None
        self.mat2_r1c1_box, self.mat2_r1c2_box, self.mat2_r1c3_box = None, None, None
        self.mat2_r2c1_box, self.mat2_r2c2_box, self.mat2_r2c3_box = None, None, None
        self.mat2_r3c1_box, self.mat2_r3c2_box, self.mat2_r3c3_box = None, None, None
        self.TWO_active = 0
        # reset all ONE matrix elements
        self.r1c1, self.r1c2, self.r1c3 = "", "", ""
        self.r2c1, self.r2c2, self.r2c3 = "", "", ""
        self.r3c1, self.r3c2, self.r3c3 = "", "", ""
        # reset ONE active box
        self.ONE_active = 0
        # draw rectangle border for "MATRIX 1" title
        matrix_1_title_rect = pygame.Rect(405, 125, 520, 50)
        pygame.draw.rect(self.window, RECT_BORDER_COLOR, matrix_1_title_rect, 3)
        # print "MATRIX 1" text
        matrix_1_title_text = self.matrix_no_title_font.render("MATRIX 1", True, TITLE_TEXT_COLOR)
        self.window.blit(matrix_1_title_text, (589, 142))
        # draw rectangle border for matrix
        matrix_1_rect = pygame.Rect(405, 200, 520, 285)
        pygame.draw.rect(self.window, RECT_BORDER_COLOR, matrix_1_rect, 3)
        # create 9 input boxes that accept only numbers
        self.r1c1_box = pygame.Rect(502, 227, 90, 60)  # row 1 col 1 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r1c1_box)
        self.r1c2_box = pygame.Rect(622, 227, 90, 60)  # row 1 col 2 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r1c2_box)
        self.r1c3_box = pygame.Rect(742, 227, 90, 60)  # row 1 col 3 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r1c3_box)
        self.r2c1_box = pygame.Rect(502, 312, 90, 60)  # row 2 col 1 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r2c1_box)
        self.r2c2_box = pygame.Rect(622, 312, 90, 60)  # row 2 col 2 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r2c2_box)
        self.r2c3_box = pygame.Rect(742, 312, 90, 60)  # row 2 col 3 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r2c3_box)
        self.r3c1_box = pygame.Rect(502, 397, 90, 60)  # row 3 col 1 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r3c1_box)
        self.r3c2_box = pygame.Rect(622, 397, 90, 60)  # row 3 col 2 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r3c2_box)
        self.r3c3_box = pygame.Rect(742, 397, 90, 60)  # row 3 col 3 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r3c3_box)

    def ONE_color_active_box(self):
        # first color all boxes white
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r1c1_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r1c2_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r1c3_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r2c1_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r2c2_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r2c3_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r3c1_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r3c2_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.r3c3_box)
        # then color active box blue
        if self.ONE_active == 11:  # row 1 col 1
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r1c1_box)
        elif self.ONE_active == 12:  # row 1 col 2
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r1c2_box)
        elif self.ONE_active == 13:  # row 1 col 3
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r1c3_box)
        elif self.ONE_active == 21:  # row 2 col 1
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r2c1_box)
        elif self.ONE_active == 22:  # row 2 col 2
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r2c2_box)
        elif self.ONE_active == 23:  # row 2 col 3
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r2c3_box)
        elif self.ONE_active == 31:  # row 3 col 1
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r3c1_box)
        elif self.ONE_active == 32:  # row 3 col 2
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r3c2_box)
        elif self.ONE_active == 33:  # row 3 col 3
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r3c3_box)

    def ONE_redraw_all_box_input(self):
        matrix_input_display = self.ONE_matrix_input_num_font.render(self.r1c1, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (510, 240))
        matrix_input_display = self.ONE_matrix_input_num_font.render(self.r1c2, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (630, 240))
        matrix_input_display = self.ONE_matrix_input_num_font.render(self.r1c3, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (750, 240))
        matrix_input_display = self.ONE_matrix_input_num_font.render(self.r2c1, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (510, 325))
        matrix_input_display = self.ONE_matrix_input_num_font.render(self.r2c2, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (630, 325))
        matrix_input_display = self.ONE_matrix_input_num_font.render(self.r2c3, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (750, 325))
        matrix_input_display = self.ONE_matrix_input_num_font.render(self.r3c1, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (510, 410))
        matrix_input_display = self.ONE_matrix_input_num_font.render(self.r3c2, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (630, 410))
        matrix_input_display = self.ONE_matrix_input_num_font.render(self.r3c3, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (750, 410))

    def draw_TWO_matrix_template(self):
        # remove previous matrix templates
        blank_rect = pygame.Rect(398, 119, 535, 373)
        pygame.draw.rect(self.window, WINDOW_BACKGROUND_COLOR, blank_rect)
        # remove ONE components
        self.r1c1_box, self.r1c2_box, self.r1c3_box = None, None, None
        self.r2c1_box, self.r2c2_box, self.r2c3_box = None, None, None
        self.r3c1_box, self.r3c2_box, self.r3c3_box = None, None, None
        self.ONE_active = 0
        # reset all TWO matrix elements
        self.mat1_r1c1, self.mat1_r1c2, self.mat1_r1c3 = "", "", ""
        self.mat1_r2c1, self.mat1_r2c2, self.mat1_r2c3 = "", "", ""
        self.mat1_r3c1, self.mat1_r3c2, self.mat1_r3c3 = "", "", ""
        self.mat2_r1c1, self.mat2_r1c2, self.mat2_r1c3 = "", "", ""
        self.mat2_r2c1, self.mat2_r2c2, self.mat2_r2c3 = "", "", ""
        self.mat2_r3c1, self.mat2_r3c2, self.mat2_r3c3 = "", "", ""
        # reset TW0 active box
        self.TWO_active = 0
        # draw "MATRIX 1" title with border
        matrix_1_title_rect = pygame.Rect(405, 125, 248, 50)
        pygame.draw.rect(self.window, RECT_BORDER_COLOR, matrix_1_title_rect, 3)
        matrix_1_title_text = self.matrix_no_title_font.render("MATRIX 1", True, TITLE_TEXT_COLOR)
        self.window.blit(matrix_1_title_text, (452, 142))
        # draw "MATRIX 2" title with border
        matrix_2_title_rect = pygame.Rect(678, 125, 248, 50)
        pygame.draw.rect(self.window, RECT_BORDER_COLOR, matrix_2_title_rect, 3)
        matrix_2_title_text = self.matrix_no_title_font.render("MATRIX 2", True, TITLE_TEXT_COLOR)
        self.window.blit(matrix_2_title_text, (724, 142))
        # draw rectangle border for matrix 1
        matrix_1_rect = pygame.Rect(405, 200, 248, 285)
        pygame.draw.rect(self.window, RECT_BORDER_COLOR, matrix_1_rect, 3)
        # draw rectangle border for matrix 2
        matrix_2_rect = pygame.Rect(678, 200, 248, 285)
        pygame.draw.rect(self.window, RECT_BORDER_COLOR, matrix_2_rect, 3)
        # draw 9 input boxes for matrix 1
        self.mat1_r1c1_box = pygame.Rect(412, 227, 74, 60)  # row 1 col 1 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r1c1_box)
        self.mat1_r1c2_box = pygame.Rect(492, 227, 74, 60)  # row 1 col 2 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r1c2_box)
        self.mat1_r1c3_box = pygame.Rect(572, 227, 74, 60)  # row 1 col 3 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r1c3_box)
        self.mat1_r2c1_box = pygame.Rect(412, 312, 74, 60)  # row 2 col 1 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r2c1_box)
        self.mat1_r2c2_box = pygame.Rect(492, 312, 74, 60)  # row 2 col 2 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r2c2_box)
        self.mat1_r2c3_box = pygame.Rect(572, 312, 74, 60)  # row 2 col 3 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r2c3_box)
        self.mat1_r3c1_box = pygame.Rect(412, 397, 74, 60)  # row 3 col 1 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r3c1_box)
        self.mat1_r3c2_box = pygame.Rect(492, 397, 74, 60)  # row 3 col 2 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r3c2_box)
        self.mat1_r3c3_box = pygame.Rect(572, 397, 74, 60)  # row 3 col 3 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r3c3_box)
        # draw 9 input boxes for matrix 2
        self.mat2_r1c1_box = pygame.Rect(685, 227, 74, 60)  # row 1 col 1 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r1c1_box)
        self.mat2_r1c2_box = pygame.Rect(765, 227, 74, 60)  # row 1 col 2 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r1c2_box)
        self.mat2_r1c3_box = pygame.Rect(845, 227, 74, 60)  # row 1 col 3 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r1c3_box)
        self.mat2_r2c1_box = pygame.Rect(685, 312, 74, 60)  # row 2 col 1 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r2c1_box)
        self.mat2_r2c2_box = pygame.Rect(765, 312, 74, 60)  # row 2 col 2 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r2c2_box)
        self.mat2_r2c3_box = pygame.Rect(845, 312, 74, 60)  # row 2 col 3 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r2c3_box)
        self.mat2_r3c1_box = pygame.Rect(685, 397, 74, 60)  # row 3 col 1 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r3c1_box)
        self.mat2_r3c2_box = pygame.Rect(765, 397, 74, 60)  # row 3 col 2 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r3c2_box)
        self.mat2_r3c3_box = pygame.Rect(845, 397, 74, 60)  # row 3 col 3 #
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r3c3_box)

    def TWO_color_active_box(self):
        # matrix 1
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r1c1_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r1c2_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r1c3_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r2c1_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r2c2_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r2c3_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r3c1_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r3c2_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat1_r3c3_box)
        # matrix 2
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r1c1_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r1c2_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r1c3_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r2c1_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r2c2_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r2c3_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r3c1_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r3c2_box)
        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_INACTIVE, self.mat2_r3c3_box)
        # matrix 1
        if self.TWO_active == 111:  # row 1 col 1
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r1c1_box)
        elif self.TWO_active == 112:  # row 1 col 2
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r1c2_box)
        elif self.TWO_active == 113:  # row 1 col 3
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r1c3_box)
        elif self.TWO_active == 121:  # row 2 col 1
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r2c1_box)
        elif self.TWO_active == 122:  # row 2 col 2
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r2c2_box)
        elif self.TWO_active == 123:  # row 2 col 3
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r2c3_box)
        elif self.TWO_active == 131:  # row 3 col 1
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r3c1_box)
        elif self.TWO_active == 132:  # row 3 col 2
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r3c2_box)
        elif self.TWO_active == 133:  # row 3 col 3
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r3c3_box)
        # matrix 2
        elif self.TWO_active == 211:  # row 1 col 1
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r1c1_box)
        elif self.TWO_active == 212:  # row 1 col 2
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r1c2_box)
        elif self.TWO_active == 213:  # row 1 col 3
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r1c3_box)
        elif self.TWO_active == 221:  # row 2 col 1
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r2c1_box)
        elif self.TWO_active == 222:  # row 2 col 2
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r2c2_box)
        elif self.TWO_active == 223:  # row 2 col 3
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r2c3_box)
        elif self.TWO_active == 231:  # row 3 col 1
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r3c1_box)
        elif self.TWO_active == 232:  # row 3 col 2
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r3c2_box)
        elif self.TWO_active == 233:  # row 3 col 3
            pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r3c3_box)

    def TWO_redraw_all_box_input(self):
        # matrix 1
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat1_r1c1, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (417, 240))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat1_r1c2, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (497, 240))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat1_r1c3, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (577, 240))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat1_r2c1, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (417, 325))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat1_r2c2, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (497, 325))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat1_r2c3, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (577, 325))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat1_r3c1, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (417, 410))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat1_r3c2, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (497, 410))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat1_r3c3, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (577, 410))
        # matrix 2
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat2_r1c1, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (690, 240))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat2_r1c2, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (770, 240))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat2_r1c3, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (850, 240))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat2_r2c1, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (690, 325))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat2_r2c2, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (770, 325))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat2_r2c3, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (850, 325))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat2_r3c1, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (690, 410))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat2_r3c2, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (770, 410))
        matrix_input_display = self.TWO_matrix_input_num_font.render(self.mat2_r3c3, True, INPUT_TEXT_COLOR)
        self.window.blit(matrix_input_display, (850, 410))

    def check_if_number_entered(self, key_pressed):
        if key_pressed == pygame.K_0:
            return True
        elif key_pressed == pygame.K_1:
            return True
        elif key_pressed == pygame.K_2:
            return True
        elif key_pressed == pygame.K_3:
            return True
        elif key_pressed == pygame.K_4:
            return True
        elif key_pressed == pygame.K_5:
            return True
        elif key_pressed == pygame.K_6:
            return True
        elif key_pressed == pygame.K_7:
            return True
        elif key_pressed == pygame.K_8:
            return True
        elif key_pressed == pygame.K_9:
            return True
        elif key_pressed == pygame.K_MINUS:
            return True
        else:
            return False

    def create_next_question_button(self):
        # print "NEXT QUESTION" title
        next_q_title_font = pygame.font.Font(FONT_2, 15)
        if self.current_q == self.no_of_q:
            button_text = " COMPLETE SET"
        else:
            button_text = "NEXT QUESTION"
        next_q_title_text = next_q_title_font.render(button_text, True, TITLE_TEXT_COLOR)
        self.window.blit(next_q_title_text, (671, 530))
        # draw triangle
        pygame.draw.polygon(self.window, BUTTON_COLOR, [(881, 516), (881, 556), (924, 536)])
        # create rectangle for button
        self.next_q_button = pygame.Rect(665, 510, 268, 50)

    def go(self):
        self.window.fill(WINDOW_BACKGROUND_COLOR)

        # run confirm page
        if self.current_q > self.no_of_q:
            ''' print "CONFIRMATION PAGE" title '''
            confirmation_page_title_font = pygame.font.Font(FONT_1, 40)
            confirmation_page_title_text = confirmation_page_title_font.render("CONFIRMATION PAGE", True,
                                                                               TITLE_TEXT_COLOR)
            self.window.blit(confirmation_page_title_text, (163, 80))

            ''' create "EXPORT TO TXT FILE" button '''
            # create rectangle
            self.export_file_button = pygame.Rect(284, 290, 396, 80)
            pygame.draw.rect(self.window, BUTTON_COLOR, self.export_file_button)
            # print text
            export_button_font = pygame.font.Font(FONT_2, 20)
            export_button_text = export_button_font.render("EXPORT TO TXT FILE", True, INPUT_TEXT_COLOR)
            self.window.blit(export_button_text, (305, 320))

            ''' DISPLAY everything on window '''
            pygame.display.flip()

            while self.running:
                pygame.time.Clock().tick(FPS)

                ''' handling events '''
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # if user clicks on export button
                        if self.export_file_button.collidepoint(event.pos):
                            # export to text file
                            self.creator.write_to_file("worksheets/" + self.file_name + '.txt')
                            # quit to MatrixEditor()
                            self.running = False

        # continue run editor
        else:
            ''' create EDITOR page components '''
            self.print_current_q_number()
            self.print_choose_q_type_title()
            self.create_q_type_radio_checklist()

            ''' initial DISPLAY everything on window '''
            pygame.display.flip()

            while self.running:
                pygame.time.Clock().tick(FPS)

                ''' handling events '''
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        sys.exit()
                        pygame.quit()

                    # clicking events #
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # if user clicked on a RADIO BUTTON #
                        if self.add_button.collidepoint(event.pos):
                            self.q_type = 0
                            self.mark_chosen_button()
                            self.draw_TWO_matrix_template()
                            self.create_next_question_button()
                            pygame.display.update()

                        elif self.sub_button.collidepoint(event.pos):
                            self.q_type = 1
                            self.mark_chosen_button()
                            self.draw_TWO_matrix_template()
                            self.create_next_question_button()
                            pygame.display.update()

                        elif self.mult_button.collidepoint(event.pos):
                            self.q_type = 2
                            self.mark_chosen_button()
                            self.draw_TWO_matrix_template()
                            self.create_next_question_button()
                            pygame.display.update()

                        elif self.egvec_button.collidepoint(event.pos):
                            self.q_type = 3
                            self.mark_chosen_button()
                            self.draw_ONE_matrix_template()
                            self.create_next_question_button()
                            pygame.display.update()

                        elif self.egval_button.collidepoint(event.pos):
                            self.q_type = 4
                            self.mark_chosen_button()
                            self.draw_ONE_matrix_template()
                            self.create_next_question_button()
                            pygame.display.update()

                        elif self.inv_button.collidepoint(event.pos):
                            self.q_type = 5
                            self.mark_chosen_button()
                            self.draw_ONE_matrix_template()
                            self.create_next_question_button()
                            pygame.display.update()

                        elif self.det_button.collidepoint(event.pos):
                            self.q_type = 6
                            self.mark_chosen_button()
                            self.draw_ONE_matrix_template()
                            self.create_next_question_button()
                            pygame.display.update()

                        # ONE template - if user clicked on a matrix number input box #
                        elif self.r1c1_box is not None:
                            if self.r1c1_box.collidepoint(event.pos):
                                # set this box to input active
                                self.ONE_active = 11
                                # color this box blue
                                self.ONE_color_active_box()
                                self.ONE_redraw_all_box_input()
                                pygame.display.update()

                            elif self.r1c2_box.collidepoint(event.pos):
                                self.ONE_active = 12
                                self.ONE_color_active_box()
                                self.ONE_redraw_all_box_input()
                                pygame.display.update()

                            elif self.r1c3_box.collidepoint(event.pos):
                                self.ONE_active = 13
                                self.ONE_color_active_box()
                                self.ONE_redraw_all_box_input()
                                pygame.display.update()

                            elif self.r2c1_box.collidepoint(event.pos):
                                self.ONE_active = 21
                                self.ONE_color_active_box()
                                self.ONE_redraw_all_box_input()
                                pygame.display.update()

                            elif self.r2c2_box.collidepoint(event.pos):
                                self.ONE_active = 22
                                self.ONE_color_active_box()
                                self.ONE_redraw_all_box_input()
                                pygame.display.update()

                            elif self.r2c3_box.collidepoint(event.pos):
                                self.ONE_active = 23
                                self.ONE_color_active_box()
                                self.ONE_redraw_all_box_input()
                                pygame.display.update()

                            elif self.r3c1_box.collidepoint(event.pos):
                                self.ONE_active = 31
                                self.ONE_color_active_box()
                                self.ONE_redraw_all_box_input()
                                pygame.display.update()

                            elif self.r3c2_box.collidepoint(event.pos):
                                self.ONE_active = 32
                                self.ONE_color_active_box()
                                self.ONE_redraw_all_box_input()
                                pygame.display.update()

                            elif self.r3c3_box.collidepoint(event.pos):
                                self.ONE_active = 33
                                self.ONE_color_active_box()
                                self.ONE_redraw_all_box_input()
                                pygame.display.update()

                        # TWO template - if user clicked on a matrix number input box #
                        elif self.mat1_r1c1_box is not None:
                            if self.mat1_r1c1_box.collidepoint(event.pos):
                                # set this box to input active
                                self.TWO_active = 111
                                # color this box blue
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat1_r1c2_box.collidepoint(event.pos):
                                self.TWO_active = 112
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat1_r1c3_box.collidepoint(event.pos):
                                self.TWO_active = 113
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat1_r2c1_box.collidepoint(event.pos):
                                self.TWO_active = 121
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat1_r2c2_box.collidepoint(event.pos):
                                self.TWO_active = 122
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat1_r2c3_box.collidepoint(event.pos):
                                self.TWO_active = 123
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat1_r3c1_box.collidepoint(event.pos):
                                self.TWO_active = 131
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat1_r3c2_box.collidepoint(event.pos):
                                self.TWO_active = 132
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat1_r3c3_box.collidepoint(event.pos):
                                self.TWO_active = 133
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat2_r1c1_box.collidepoint(event.pos):
                                # set this box to input active
                                self.TWO_active = 211
                                # color this box blue
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat2_r1c2_box.collidepoint(event.pos):
                                self.TWO_active = 212
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat2_r1c3_box.collidepoint(event.pos):
                                self.TWO_active = 213
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat2_r2c1_box.collidepoint(event.pos):
                                self.TWO_active = 221
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat2_r2c2_box.collidepoint(event.pos):
                                self.TWO_active = 222
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat2_r2c3_box.collidepoint(event.pos):
                                self.TWO_active = 223
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat2_r3c1_box.collidepoint(event.pos):
                                self.TWO_active = 231
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat2_r3c2_box.collidepoint(event.pos):
                                self.TWO_active = 232
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                            elif self.mat2_r3c3_box.collidepoint(event.pos):
                                self.TWO_active = 233
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()

                        # if user clicked on NEXT QUESTION button #
                        if self.next_q_button is not None:
                            if self.next_q_button.collidepoint(event.pos):
                                # for question types requiring two matrices
                                if self.q_type == 0 or self.q_type == 1 or self.q_type == 2:
                                    # initialise empty boxes to 0
                                    # matrix 1
                                    if self.mat1_r1c1 == "":
                                        self.mat1_r1c1 = 0
                                    if self.mat1_r1c2 == "":
                                        self.mat1_r1c2 = 0
                                    if self.mat1_r1c3 == "":
                                        self.mat1_r1c3 = 0
                                    if self.mat1_r2c1 == "":
                                        self.mat1_r2c1 = 0
                                    if self.mat1_r2c2 == "":
                                        self.mat1_r2c2 = 0
                                    if self.mat1_r2c3 == "":
                                        self.mat1_r2c3 = 0
                                    if self.mat1_r3c1 == "":
                                        self.mat1_r3c1 = 0
                                    if self.mat1_r3c2 == "":
                                        self.mat1_r3c2 = 0
                                    if self.mat1_r3c3 == "":
                                        self.mat1_r3c3 = 0
                                    # matrix 2
                                    if self.mat2_r1c1 == "":
                                        self.mat2_r1c1 = 0
                                    if self.mat2_r1c2 == "":
                                        self.mat2_r1c2 = 0
                                    if self.mat2_r1c3 == "":
                                        self.mat2_r1c3 = 0
                                    if self.mat2_r2c1 == "":
                                        self.mat2_r2c1 = 0
                                    if self.mat2_r2c2 == "":
                                        self.mat2_r2c2 = 0
                                    if self.mat2_r2c3 == "":
                                        self.mat2_r2c3 = 0
                                    if self.mat2_r3c1 == "":
                                        self.mat2_r3c1 = 0
                                    if self.mat2_r3c2 == "":
                                        self.mat2_r3c2 = 0
                                    if self.mat2_r3c3 == "":
                                        self.mat2_r3c3 = 0
                                    m1_r1c1 = int(self.mat1_r1c1); m1_r1c2 = int(self.mat1_r1c2); m1_r1c3 = int(self.mat1_r1c3)
                                    m1_r2c1 = int(self.mat1_r2c1); m1_r2c2 = int(self.mat1_r2c2); m1_r2c3 = int(self.mat1_r2c3)
                                    m1_r3c1 = int(self.mat1_r3c1); m1_r3c2 = int(self.mat1_r3c2); m1_r3c3 = int(self.mat1_r3c3)
                                    m2_r1c1 = int(self.mat2_r1c1); m2_r1c2 = int(self.mat2_r1c2); m2_r1c3 = int(self.mat2_r1c3)
                                    m2_r2c1 = int(self.mat2_r2c1); m2_r2c2 = int(self.mat2_r2c2); m2_r2c3 = int(self.mat2_r2c3)
                                    m2_r3c1 = int(self.mat2_r3c1); m2_r3c2 = int(self.mat2_r3c2); m2_r3c3 = int(self.mat2_r3c3)
                                    matrix_1 = [[m1_r1c1, m1_r1c2, m1_r1c3], [m1_r2c1, m1_r2c2, m1_r2c3],
                                                [m1_r3c1, m1_r3c2, m1_r3c3]]
                                    matrix_2 = [[m2_r1c1, m2_r1c2, m2_r1c3], [m2_r2c1, m2_r2c2, m2_r2c3],
                                                [m2_r3c1, m2_r3c2, m2_r3c3]]
                                    # for simplicity, all matrices are fixed at a 3x3 dimension in this prototype
                                    self.creator.add_question(self.q_type, 3, 3, matrix_1, 3, 3, matrix_2)

                                else:
                                    if self.r1c1 == "":
                                        self.r1c1 = 0
                                    if self.r1c2 == "":
                                        self.r1c2 = 0
                                    if self.r1c3 == "":
                                        self.r1c3 = 0
                                    if self.r2c1 == "":
                                        self.r2c1 = 0
                                    if self.r2c2 == "":
                                        self.r2c2 = 0
                                    if self.r2c3 == "":
                                        self.r2c3 = 0
                                    if self.r3c1 == "":
                                        self.r3c1 = 0
                                    if self.r3c2 == "":
                                        self.r3c2 = 0
                                    if self.r3c3 == "":
                                        self.r3c3 = 0
                                    m1_r1c1 = int(self.r1c1); m1_r1c2 = int(self.r1c2); m1_r1c3 = int(self.r1c3)
                                    m1_r2c1 = int(self.r2c1); m1_r2c2 = int(self.r2c2); m1_r2c3 = int(self.r2c3)
                                    m1_r3c1 = int(self.r3c1); m1_r3c2 = int(self.r3c2); m1_r3c3 = int(self.r3c3)
                                    matrix = [[m1_r1c1, m1_r1c2, m1_r1c3], [m1_r2c1, m1_r2c2, m1_r2c3],
                                              [m1_r3c1, m1_r3c2, m1_r3c3]]
                                    self.creator.add_question(self.q_type, 3, 3, matrix)
                                # move pointer to next question
                                self.current_q += 1
                                self.go()

                    # keyboard events #
                    elif event.type == pygame.KEYDOWN:
                        # ONE template - if a box was clicked #
                        if self.ONE_active != 0:
                            # if user types a number #
                            number = self.check_if_number_entered(event.key)
                            if number:
                                # if r1c1 clicked, then draw blue rect with number r1c1 printed
                                if self.ONE_active == 11:
                                    if len(self.r1c1) < 4:
                                        self.r1c1 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r1c1_box)
                                        matrix_input_display = self.ONE_matrix_input_num_font.render(
                                            self.r1c1, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (510, 240))
                                        pygame.display.update()

                                elif self.ONE_active == 12:
                                    if len(self.r1c2) < 4:
                                        self.r1c2 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r1c2_box)
                                        matrix_input_display = self.ONE_matrix_input_num_font.render(
                                            self.r1c2, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (630, 240))
                                        pygame.display.update()

                                elif self.ONE_active == 13:
                                    if len(self.r1c3) < 4:
                                        self.r1c3 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r1c3_box)
                                        matrix_input_display = self.ONE_matrix_input_num_font.render(
                                            self.r1c3, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (750, 240))
                                        pygame.display.update()

                                elif self.ONE_active == 21:
                                    # prevent overlarge numbers entered
                                    if len(self.r2c1) < 4:
                                        self.r2c1 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r2c1_box)
                                        matrix_input_display = self.ONE_matrix_input_num_font.render(
                                            self.r2c1, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (510, 325))
                                        pygame.display.update()

                                elif self.ONE_active == 22:
                                    if len(self.r2c2) < 4:
                                        self.r2c2 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r2c2_box)
                                        matrix_input_display = self.ONE_matrix_input_num_font.render(
                                            self.r2c2, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (630, 325))
                                        pygame.display.update()

                                elif self.ONE_active == 23:
                                    if len(self.r2c3) < 4:
                                        self.r2c3 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r2c3_box)
                                        matrix_input_display = self.ONE_matrix_input_num_font.render(
                                            self.r2c3, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (750, 325))
                                        pygame.display.update()

                                elif self.ONE_active == 31:
                                    # prevent overlarge numbers entered
                                    if len(self.r3c1) < 4:
                                        self.r3c1 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r3c1_box)
                                        matrix_input_display = self.ONE_matrix_input_num_font.render(
                                            self.r3c1, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (510, 410))
                                        pygame.display.update()

                                elif self.ONE_active == 32:
                                    if len(self.r3c2) < 4:
                                        self.r3c2 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r3c2_box)
                                        matrix_input_display = self.ONE_matrix_input_num_font.render(
                                            self.r3c2, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (630, 410))
                                        pygame.display.update()

                                elif self.ONE_active == 33:
                                    if len(self.r3c3) < 4:
                                        self.r3c3 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r3c3_box)
                                        matrix_input_display = self.ONE_matrix_input_num_font.render(
                                            self.r3c3, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (750, 410))
                                        pygame.display.update()

                            # if user presses backspace #
                            elif event.key == pygame.K_BACKSPACE:
                                if self.ONE_active == 11:
                                    self.r1c1 = self.r1c1[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r1c1_box)
                                    matrix_input_display = self.ONE_matrix_input_num_font.render(
                                        self.r1c1, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (510, 240))
                                    pygame.display.update()

                                elif self.ONE_active == 12:
                                    self.r1c2 = self.r1c2[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r1c2_box)
                                    matrix_input_display = self.ONE_matrix_input_num_font.render(
                                        self.r1c2, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (630, 240))
                                    pygame.display.update()

                                elif self.ONE_active == 13:
                                    self.r1c3 = self.r1c3[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r1c3_box)
                                    matrix_input_display = self.ONE_matrix_input_num_font.render(
                                        self.r1c3, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (750, 240))
                                    pygame.display.update()

                                elif self.ONE_active == 21:
                                    self.r2c1 = self.r2c1[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r2c1_box)
                                    matrix_input_display = self.ONE_matrix_input_num_font.render(
                                        self.r2c1, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (510, 325))
                                    pygame.display.update()

                                elif self.ONE_active == 22:
                                    self.r2c2 = self.r2c2[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r2c2_box)
                                    matrix_input_display = self.ONE_matrix_input_num_font.render(
                                        self.r2c2, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (630, 325))
                                    pygame.display.update()

                                elif self.ONE_active == 23:
                                    self.r2c3 = self.r2c3[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r2c3_box)
                                    matrix_input_display = self.ONE_matrix_input_num_font.render(
                                        self.r2c3, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (750, 325))
                                    pygame.display.update()

                                elif self.ONE_active == 31:
                                    self.r3c1 = self.r3c1[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r3c1_box)
                                    matrix_input_display = self.ONE_matrix_input_num_font.render(
                                        self.r3c1, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (510, 410))
                                    pygame.display.update()

                                elif self.ONE_active == 32:
                                    self.r3c2 = self.r3c2[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r3c2_box)
                                    matrix_input_display = self.ONE_matrix_input_num_font.render(
                                        self.r3c2, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (630, 410))
                                    pygame.display.update()

                                elif self.ONE_active == 33:
                                    self.r3c3 = self.r3c3[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.r3c3_box)
                                    matrix_input_display = self.ONE_matrix_input_num_font.render(
                                        self.r3c3, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (750, 410))
                                    pygame.display.update()

                            # if user presses enter #
                            elif event.key == pygame.K_RETURN:
                                self.ONE_active = 0
                                self.ONE_color_active_box()
                                self.ONE_redraw_all_box_input()
                                pygame.display.update()

                        # TWO template - if a box was clicked #
                        elif self.TWO_active != 0:
                            # if user types a number #
                            number = self.check_if_number_entered(event.key)
                            if number:
                                # if r1c1 clicked, then draw blue rect with number r1c1 printed
                                if self.TWO_active == 111:
                                    if len(self.mat1_r1c1) < 4:
                                        self.mat1_r1c1 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r1c1_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat1_r1c1, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (417, 240))
                                        pygame.display.update()

                                elif self.TWO_active == 112:
                                    if len(self.mat1_r1c2) < 4:
                                        self.mat1_r1c2 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r1c2_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat1_r1c2, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (497, 240))
                                        pygame.display.update()

                                elif self.TWO_active == 113:
                                    if len(self.mat1_r1c3) < 4:
                                        self.mat1_r1c3 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r1c3_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat1_r1c3, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (577, 240))
                                        pygame.display.update()

                                elif self.TWO_active == 121:
                                    if len(self.mat1_r2c1) < 4:
                                        self.mat1_r2c1 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r2c1_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat1_r2c1, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (417, 325))
                                        pygame.display.update()

                                elif self.TWO_active == 122:
                                    if len(self.mat1_r2c2) < 4:
                                        self.mat1_r2c2 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r2c2_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat1_r2c2, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (497, 325))
                                        pygame.display.update()

                                elif self.TWO_active == 123:
                                    if len(self.mat1_r2c3) < 4:
                                        self.mat1_r2c3 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r2c3_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat1_r2c3, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (577, 325))
                                        pygame.display.update()

                                elif self.TWO_active == 131:
                                    if len(self.mat1_r3c1) < 4:
                                        self.mat1_r3c1 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r3c1_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat1_r3c1, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (417, 410))
                                        pygame.display.update()

                                elif self.TWO_active == 132:
                                    if len(self.mat1_r3c2) < 4:
                                        self.mat1_r3c2 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r3c2_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat1_r3c2, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (497, 410))
                                        pygame.display.update()

                                elif self.TWO_active == 133:
                                    if len(self.mat1_r3c3) < 4:
                                        self.mat1_r3c3 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r3c3_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat1_r3c3, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (577, 410))
                                        pygame.display.update()

                                elif self.TWO_active == 211:
                                    if len(self.mat2_r1c1) < 4:
                                        self.mat2_r1c1 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r1c1_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat2_r1c1, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (690, 240))
                                        pygame.display.update()

                                elif self.TWO_active == 212:
                                    if len(self.mat2_r1c2) < 4:
                                        self.mat2_r1c2 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r1c2_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat2_r1c2, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (770, 240))
                                        pygame.display.update()

                                elif self.TWO_active == 213:
                                    if len(self.mat2_r1c3) < 4:
                                        self.mat2_r1c3 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r1c3_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat2_r1c3, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (850, 240))
                                        pygame.display.update()

                                elif self.TWO_active == 221:
                                    if len(self.mat2_r2c1) < 4:
                                        self.mat2_r2c1 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r2c1_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat2_r2c1, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (690, 325))
                                        pygame.display.update()

                                elif self.TWO_active == 222:
                                    if len(self.mat2_r2c2) < 4:
                                        self.mat2_r2c2 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r2c2_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat2_r2c2, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (770, 325))
                                        pygame.display.update()

                                elif self.TWO_active == 223:
                                    if len(self.mat2_r2c3) < 4:
                                        self.mat2_r2c3 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r2c3_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat2_r2c3, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (850, 325))
                                        pygame.display.update()

                                elif self.TWO_active == 231:
                                    if len(self.mat2_r3c1) < 4:
                                        self.mat2_r3c1 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r3c1_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat2_r3c1, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (690, 410))
                                        pygame.display.update()

                                elif self.TWO_active == 232:
                                    if len(self.mat2_r3c2) < 4:
                                        self.mat2_r3c2 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r3c2_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat2_r3c2, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (770, 410))
                                        pygame.display.update()

                                elif self.TWO_active == 233:
                                    if len(self.mat2_r3c3) < 4:
                                        self.mat2_r3c3 += event.unicode
                                        pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r3c3_box)
                                        matrix_input_display = self.TWO_matrix_input_num_font.render(
                                            self.mat2_r3c3, True, INPUT_TEXT_COLOR)
                                        self.window.blit(matrix_input_display, (850, 410))
                                        pygame.display.update()

                            # if user presses backspace #
                            elif event.key == pygame.K_BACKSPACE:
                                if self.TWO_active == 111:
                                    self.mat1_r1c1 = self.mat1_r1c1[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r1c1_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat1_r1c1, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (417, 240))
                                    pygame.display.update()

                                elif self.TWO_active == 112:
                                    self.mat1_r1c2 = self.mat1_r1c2[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r1c2_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat1_r1c2, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (497, 240))
                                    pygame.display.update()

                                elif self.TWO_active == 113:
                                    self.mat1_r1c3 = self.mat1_r1c3[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r1c3_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat1_r1c3, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (577, 240))
                                    pygame.display.update()

                                elif self.TWO_active == 121:
                                    self.mat1_r2c1 = self.mat1_r2c1[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r2c1_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat1_r2c1, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (417, 325))
                                    pygame.display.update()

                                elif self.TWO_active == 122:
                                    self.mat1_r2c2 = self.mat1_r2c2[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r2c2_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat1_r2c2, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (497, 325))
                                    pygame.display.update()

                                elif self.TWO_active == 123:
                                    self.mat1_r2c3 = self.mat1_r2c3[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r2c3_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat1_r2c3, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (577, 325))
                                    pygame.display.update()

                                elif self.TWO_active == 131:
                                    self.mat1_r3c1 = self.mat1_r3c1[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r3c1_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat1_r3c1, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (417, 410))
                                    pygame.display.update()

                                elif self.TWO_active == 132:
                                    self.mat1_r3c2 = self.mat1_r3c2[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r3c2_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat1_r3c2, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (497, 410))
                                    pygame.display.update()

                                elif self.TWO_active == 133:
                                    self.mat1_r3c3 = self.mat1_r3c3[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat1_r3c3_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat1_r3c3, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (577, 410))
                                    pygame.display.update()

                                elif self.TWO_active == 211:
                                    self.mat2_r1c1 = self.mat2_r1c1[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r1c1_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat2_r1c1, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (690, 240))
                                    pygame.display.update()

                                elif self.TWO_active == 212:
                                    self.mat2_r1c2 = self.mat2_r1c2[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r1c2_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat2_r1c2, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (770, 240))
                                    pygame.display.update()

                                elif self.TWO_active == 213:
                                    self.mat2_r1c3 = self.mat2_r1c3[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r1c3_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat2_r1c3, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (850, 240))
                                    pygame.display.update()

                                elif self.TWO_active == 221:
                                    self.mat2_r2c1 = self.mat2_r2c1[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r2c1_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat2_r2c1, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (690, 325))
                                    pygame.display.update()

                                elif self.TWO_active == 222:
                                    self.mat2_r2c2 = self.mat2_r2c2[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r2c2_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat2_r2c2, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (770, 325))
                                    pygame.display.update()

                                elif self.TWO_active == 223:
                                    self.mat2_r2c3 = self.mat2_r2c3[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r2c3_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat2_r2c3, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (850, 325))
                                    pygame.display.update()

                                elif self.TWO_active == 231:
                                    self.mat2_r3c1 = self.mat2_r3c1[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r3c1_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat2_r3c1, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (690, 410))
                                    pygame.display.update()

                                elif self.TWO_active == 232:
                                    self.mat2_r3c2 = self.mat2_r3c2[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r3c2_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat2_r3c2, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (770, 410))
                                    pygame.display.update()

                                elif self.TWO_active == 233:
                                    self.mat2_r3c3 = self.mat2_r3c3[:-1]
                                    pygame.draw.rect(self.window, INPUT_TEXTBOX_COLOR_ACTIVE, self.mat2_r3c3_box)
                                    matrix_input_display = self.TWO_matrix_input_num_font.render(
                                        self.mat2_r3c3, True, INPUT_TEXT_COLOR)
                                    self.window.blit(matrix_input_display, (850, 410))
                                    pygame.display.update()

                            # if user presses enter #
                            elif event.key == pygame.K_RETURN:
                                self.TWO_active = 0
                                self.TWO_color_active_box()
                                self.TWO_redraw_all_box_input()
                                pygame.display.update()


class MatrixEditor:
    def __init__(self):
        """ initialise GUI window """
        self.window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        pygame.display.set_caption(WINDOW_TITLE)

    def main(self):
        pygame.init()

        ''' start off the COVER page '''
        cover_page = CoverPage(self.window)
        file_name, no_of_q = cover_page.go()

        # run this part only if user did not exit the program
        if file_name is not None and no_of_q is not None:
            ''' move onto EDITOR page '''
            editor_page = EditorPage(self.window, file_name, no_of_q)
            editor_page.go()


