import numpy as np

class Create_Exercise:

    def __init__(self,size):
        self.exercise_set_size = size
        self.exercise_set = []

    def write_to_file(self,filename):
        f = open(filename, "w")
        f.write(str(self.exercise_set_size) + "\n")
        for question in self.exercise_set:
            for element in question:
                element = str(element)
                element = element.replace("[","").replace("]","").replace(",","")
                f.write(str(element) + "\n")
        f.close()

    def add_question(self,question_type,row1,col1,matrix1,
                    row2 = None,col2 = None,matrix2 = None):
        self.exercise_set.append([question_type,[row1,col1],matrix1])
        if row2 != None:
            self.exercise_set[-1].append([row2,col2])
            self.exercise_set[-1].append(matrix2)
