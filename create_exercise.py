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
                f.write(str(element) + "\n")
        f.close()

    def add_question(self,question_type,row1,col1,matrix1,
                    row2 = None,col2 = None,matrix2 = None):
        self.exercise_set.append([question_type,row1,col1,matrix1])
        if row2 != None:
            self.exercise_set[-1].append(row2)
            self.exercise_set[-1].append(col2)
            self.exercise_set[-1].append(matrix2)

if __name__ == "__main__":
    ce = Create_Exercise(1)
    ce.add_question(1,3,3,[[1,2,3],[4,5,6],[7,8,9]],3,3,[[1,2,3],[4,5,6],[7,8,9]])
    ce.write_to_file("test.txt")