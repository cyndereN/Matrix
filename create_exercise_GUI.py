# create_exercise GUI

"""
BASIC STRUCTURE OF GUI:
- make a basic frame window - WIDTH: 960 ; HEIGHT: 580
- important components:
    - COVER PAGE
        - "CREATE EXERCISE" title
        - todo | textbox for user input of file name
        - todo | get number input from user for number of questions
        - todo | "START CREATING" button - go to EDITOR page
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
RECT_COLOR_INACTIVE = (255, 255, 255)  # white
RECT_COLOR_ACTIVE = (137, 209, 254)  # light blue
INPUT_TEXT_COLOR = (0, 0, 0)  # black


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
        file_input_textbox = pygame.Rect(350, 190, 500, 50)
        pygame.draw.rect(window, RECT_COLOR_INACTIVE, file_input_textbox)
        # format text
        file_input_text = ""
        file_input_text_font = pygame.font.SysFont("courier new", 25)
        active = False

        ''' initial display everything on window '''
        pygame.display.flip()

        running = True
        while running:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # if input box is clicked
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if file_input_textbox.colliderect(file_input_textbox):
                        pygame.draw.rect(window, RECT_COLOR_ACTIVE, file_input_textbox)
                        file_input_text_display = file_input_text_font.render(file_input_text, True, INPUT_TEXT_COLOR)
                        window.blit(file_input_text_display, (365, 200))
                        active = True
                        pygame.display.update()

                # if input box was clicked & user types on keyboard
                elif event.type == pygame.KEYDOWN and active:
                    # confirms file name
                    if event.key == pygame.K_RETURN:
                        pygame.draw.rect(window, RECT_COLOR_INACTIVE, file_input_textbox)
                        file_input_text_display = file_input_text_font.render(file_input_text, True, INPUT_TEXT_COLOR)
                        window.blit(file_input_text_display, (365, 200))
                        active = False
                        print(file_input_text)
                        pygame.display.update()

                    # deletes some characters
                    elif event.key == pygame.K_BACKSPACE:
                        file_input_text = file_input_text[:-1]
                        pygame.draw.rect(window, RECT_COLOR_ACTIVE, file_input_textbox)
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
