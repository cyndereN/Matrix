import numpy as np


class Matrix:

    def __init__(self, element):
        self.__element = element

    def __determinant(self):
        pass

    def __inverse(self):
        pass

    def __eigenvector(self):
        pass

    def __eigenvalue(self):
        pass

    def getDeterminant(self):
        return self.determinant()

    def getInverse(self):
        return self.inverse()

    def getEigenvector(self):
        return self.eigenvetor()

    def getEigenvalue(self):
        return self.__eigenvalue()


if __name__ == "__main__":
    m = Matrix([1, 2, 3, 4])
    print(m.element)
