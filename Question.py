class Question:

    def __init__(self, question_type, text, answer, matrix1, matrix2=None):

        self.__question_type = question_type
        self.__matrix1 = matrix1
        self.__matrix2 = matrix2
        self.__text = text
        self.__answer = answer

    def get_question_type(self):
        return self.__question_type

    def get_text(self):
        return self.__text

    def get_matrices(self):
        return (self.__matrix1,self.__matrix2)

    def get_answer(self):
        return self.__answer