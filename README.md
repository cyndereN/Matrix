# Matrix
A teaching aid tool developed for learning matrix using pygame.

To run: `python main.py`

# Test "Load" button on MacOS device
These changes only need to be made if the program crashes when using the "Load" button.

In order to test the "Load" button on a MacOS device:
First go to practice_exercise.py, comment out lines 62, 63, 64 and 65
(as these lines involve using tkinter)
and replace 'file_name' in line 66 with the path of the file you want to import

For example,

line 66 | `self.filePath = "worksheets/test.txt"`
