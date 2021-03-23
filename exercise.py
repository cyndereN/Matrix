from random import randint
from random import choice
from Question import Question
from MatrixCalculator import calculator

ADDITION = 0
SUBTRACTION = 1
MULTIPLICATION = 2
EIGENVECTOR = 3
EIGENVALUE = 4
INVERSE = 5
DETERMINANT = 6
Text = [
    "Find the result of this calculation",
    "Find the eigenvector of this matrix",
    "Find the eigenvalue of this matrix",
    "Find the inverse of this matrix",
    "Find the determinant of this matrix"
    ]


class Exercise:

    """
    Make a instance of this method by passing the size of 
    the exercise.
    If want to import from a file, then do NOT pass any argument
    Call the import import_exercise() method
    pass the filename as argument
    """

    """
    TYPE OF QUESTION      NUMBER     ANSWER DATA TYPE
    ADDITION                0             2D-List
    SUBTRACTION             1             2D-List
    MULTIPLICATION          2             2D-List
    EIGENVECTOR             3         List of 2D-List
    EIGENVALUE              4         List of Integers
    INVERSE                 5      List, e.g.[Float,2D-List]
    DETERMINANT             6             Integer
    """

    def __init__(self):
        self.calculator = calculator()
        self.question_set_size = -1
        self.question_set = []

    # def get_exercise(self):
    #     return self.question_set

    def generate_exercise(self,size):
        self.question_set.clear()
        self.question_set_size = size
        for i in range(size):
            question_type = randint(ADDITION,INVERSE)
            self.question_set.append(self.generate_question(question_type))
        return self.question_set

    def generate_question(self,question_type,Matrix1 = None,Matrix2 = None):
        # These two use another way to generate Matrix and answer
        if question_type == EIGENVECTOR:
            return self.__eigenvector(Matrix1)
        elif question_type == EIGENVALUE:
            return self.__eigenvalue(Matrix1)

        if not Matrix1:
            Matrix1, Matrix2 = self.generate_random_matrix(question_type)

        if question_type == ADDITION:
            return self.__addition(Matrix1,Matrix2)
        elif question_type == SUBTRACTION:
            return self.__subtraction(Matrix1,Matrix2)
        elif question_type == MULTIPLICATION:
            return self.__multiplication(Matrix1,Matrix2)
        elif question_type == INVERSE:
            return self.__inverse(Matrix1)
        else:
            return self.__determinant(Matrix1)

    def generate_random_matrix(self,question_type):
        Matrix1 = self.generate_twoD_lst(question_type)
        Matrix2 = None
        if (question_type == ADDITION or
                question_type == SUBTRACTION or
                question_type == MULTIPLICATION):
            Matrix2 = self.generate_twoD_lst(question_type)
        while(question_type == INVERSE and self.calculator.determinant(Matrix1) == 0):
            Matrix1 = self.generate_twoD_lst(question_type)
        return Matrix1, Matrix2

    def __check_proper_answer_and_matrix(self,Matrix1):
        answer_in_tuple = self.calculator.eigenvalue(Matrix1)
        for answer in answer_in_tuple:
            if ((not (answer - 0.00001 <= round(answer) <= answer + 0.00001))
                or type(answer) == complex
                or -0.00001 <= round(answer) <= 0.00001):
                return False
        zero_counter = 0
        for rows in Matrix1:
            for number in rows:
                if not (number - 0.00001 <= round(number) <= number + 0.00001):
                    return False
                if (-0.00001 <= round(number) <= 0.00001):
                    zero_counter += 1
                if zero_counter >= 6:
                    return False
        return True

    def __create_matrix_for_eigen(self):
        M = []
        eigenvectors_tuple = self.__find_orthogonal_matrix()
        while([0,0,0] in eigenvectors_tuple):
            eigenvectors_tuple = self.__find_orthogonal_matrix()
        eigenvectors = [eigenvectors_tuple[i] for i in range(0,3)]
        eigenvalues = []
        for i in range(0,len(eigenvectors)):
            x = eigenvectors[i]
            square_magnitude = self.calculator.squared_magnitude(x)
            factor = choice([-3,-2,-1,1,2,3])
            value = factor * square_magnitude
            while(value in eigenvalues):
                factor = choice([-3,-2,-1,1,2,3])
                value = factor * square_magnitude
            eigenvalues.append(value)
            x_norm = self.calculator.norm_L2(x)
            x = self.calculator.dot(x,1 / x_norm)
            xt = self.calculator.T(x)
            M.append(x)
        Mt = self.calculator.T(M)
        # # initialised the diagonal vector
        D = [[0 for i in range (0,3)] for k in range (0,3)]
        # put number to the diagonal 
        for d in range(0,len(D)):
            D[d][d] = eigenvalues[d]
        A =  self.calculator.multiplication(
                self.calculator.multiplication(Mt,D),M)
        return A, eigenvalues, eigenvectors

    def __find_orthogonal_matrix(self):
        x1 = [randint(-2,2) for i in range (0,3)]
        x2 = [randint(-2,2) for i in range (0,3)]
        while (self.calculator.dot(x1,x2) != 0 or x1 == x2):
            x2 = [randint(-2,2) for i in range (0,3)]
        x3 = [randint(-2,2) for i in range (0,3)]
        while (self.calculator.dot(x1,x3) != 0 or
                self.calculator.dot(x2,x3) != 0 or x1 == x3 or
                x2 == x3):
            x3 = [randint(-2,2) for i in range (0,3)]
        return x1,x2,x3

    def generate_twoD_lst(self,question_type):
        max_range = 8
        if (question_type == ADDITION or question_type == SUBTRACTION):
            max_range = 20
        return [
                ([(randint(0,max_range) if (randint(1,4) % 4 != 0) else randint(-max_range,0))
                for k in range (0,3)])
                for i in range (0,3)
                    ]

    def __round_matrix(self,Matrix1):
        if self.__check_elements_are_integer(Matrix1):
            for i in range(0,len(Matrix1)):
                if type(Matrix1[i]) == float:
                    Matrix1[i] = round(Matrix1[i])
                else:
                    for j in range(0,len(Matrix1[i])):
                        Matrix1[i][j] = round(Matrix1[i][j])
        else:
            return Matrix1

    def __check_elements_are_integer(self,Matrix1):
        for rows in Matrix1:
            if type(rows) == float:
                if not (rows - 0.00001 <= round(rows) <= rows + 0.00001):
                    return False
            else:
                for number in rows:
                    if not (number - 0.00001 <= round(number) <= number + 0.00001):
                        return False
        return True

    def import_exercise(self,filename):
        self.question_set.clear()
        f = open(filename, "r")
        self.exercise_set_size = int(f.readline())
        #print(self.exercise_set_size)
        for i in range(0,self.exercise_set_size):
            question_type_from_file = int(f.readline())
            matrix1_from_file = self.to_matrix(f.readline(),f.readline())
            matrix2_from_file = None
            if  (question_type_from_file == ADDITION or
                question_type_from_file == SUBTRACTION or
                question_type_from_file == MULTIPLICATION):
                matrix2_from_file = self.to_matrix(f.readline(),f.readline())
            else:
                matrix2_from_file = None
            self.question_set.append(
                self.generate_question(question_type_from_file,matrix1_from_file,matrix2_from_file))
        f.close()
        return self.question_set

    def to_matrix(self,str_shape,str_matrix):
        shape = str_shape.split(" ")
        row = int(shape[0])
        col = int(shape[1])
        element = str_matrix.split(" ")
        matrix = [[] for i in range (0,col)]
        for m in range(col):
            for n in range(row):
                matrix[m].append(float(element[n + m * row]))
        return matrix

    def __addition(self,Matrix1,Matrix2):
        answer = self.calculator.addition(Matrix1,Matrix2)
        self.__round_matrix(answer)
        q = Question(ADDITION,Text[0],answer, Matrix1, Matrix2)
        return q

    def __subtraction(self,Matrix1,Matrix2):
        answer = self.calculator.subtraction(Matrix1,Matrix2)
        self.__round_matrix(answer)
        q = Question(SUBTRACTION,Text[0],answer, Matrix1, Matrix2)
        return q

    def __multiplication(self,Matrix1,Matrix2):
        answer = self.calculator.multiplication(Matrix1,Matrix2)
        self.__round_matrix(answer)
        q = Question(MULTIPLICATION,Text[0],answer, Matrix1, Matrix2)
        return q

    def __eigenvector(self,Matrix1):
        answer = []

        if Matrix1 == None:
            Matrix1, _ , answer = self.__create_matrix_for_eigen()
            self.__round_matrix(Matrix1)
            while (not self.__check_proper_answer_and_matrix(Matrix1)):
                Matrix1, _ , answer= self.__create_matrix_for_eigen()
                self.__round_matrix(Matrix1)

        else:
            temp_answer = self.calculator.eigenvetor(Matrix1)
            answer.append(self.__round_matrix(temp_answer))
        q = Question(EIGENVECTOR,Text[1],answer, Matrix1)
        return q

    def __eigenvalue(self,Matrix1):
        answer = []

        if Matrix1 == None:
            Matrix1, answer, _ = self.__create_matrix_for_eigen()
            self.__round_matrix(Matrix1)
            while (not self.__check_proper_answer_and_matrix(Matrix1)):
                Matrix1, answer, _ = self.__create_matrix_for_eigen()
                self.__round_matrix(Matrix1)
        else:
            temp_answer = self.calculator.eigenvalue(Matrix1)
            answer.append(self.__round_matrix(temp_answer))

        q = Question(EIGENVALUE,Text[2],answer, Matrix1)
        return q

    def __inverse(self,Matrix1):
        answer = []
        answer_temp = self.calculator.inverse(Matrix1)
        answer.append(round(answer_temp[0]))
        answer.append(answer_temp[1])
        self.__round_matrix(answer[1])
        q = Question(INVERSE,Text[3],answer,Matrix1)
        return q

    def __determinant(self,Matrix1):
        answer = self.calculator.determinant(Matrix1)
        answer = round(answer)
        q = Question(DETERMINANT,Text[4],answer,Matrix1)
        return q

if __name__ == "__main__":
    e = Exercise()
    q1 = e.generate_exercise(5)
    q2 = e.import_exercise("test.txt")
    print("==================== Random ======================")
    for x in q1:
        print("Text:        " + str(x.get_text()))
        print("Type:        " + str(x.get_question_type()))
        print("Matrices:    " + str(x.get_matrices()))
        print("Answer:      " + str(x.get_answer()))
        print("-----------------------------------------\n")
    print("==================== From File ======================")
    for x in q2:
        print("Text:        " + str(x.get_text()))
        print("Type:        " + str(x.get_question_type()))
        print("Matrices:    " + str(x.get_matrices()))
        print("Answer:      " + str(x.get_answer()))
        print("-----------------------------------------\n")
