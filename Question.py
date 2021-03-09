from Matrix import Matrix
import random

class Question:

    def __init__(self, text, matrix1, answer, matrix2=None):

        self.__matrix1 = matrix1
        self.__matrix2 = matrix2
        self.__text = text
        self.__answer = answer

    def get_text(self):
        return self.__text

    def get_matrices(self):
        return (self.__matrix1,self.__matrix2)

    def get_answer(self):
        return self.__answer

if __name__ == "__main__":
    q = Question("test", [[1,2],[3,4]],5)
    print(q.get_matrices())