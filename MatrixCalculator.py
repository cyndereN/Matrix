import numpy as np

class calculator:

    def addition(self,Matrix1,Matrix2):
        m1 = np.array(Matrix1)
        m2 = np.array(Matrix2)
        return np.add(m1,m2).tolist()
        
    def subtraction(self,Matrix1,Matrix2):
        m1 = np.array(Matrix1)
        m2 = np.array(Matrix2)
        return np.subtract(m1,m2).tolist()
        
    def multiplication(self,Matrix1,Matrix2):
        m1 = np.array(Matrix1)
        m2 = np.array(Matrix2)
        return np.matmul(m1,m2).tolist()
    
    def eigenvetor(self,Matrix1):
        m1 = np.array(Matrix1)
        vectors = np.linalg.eig(m1)
        for vector in vectors:
            print(vector)
            vector = np.linalg.norm(vector,1)
        return vectors

    def eigenvalue(self,Matrix1):
        m1 = np.array(Matrix1)
        values = np.linalg.eigvals(m1)
        for value in values:
            np.linalg.norm(value)
        return values

    def multiplication(self,Matrix1,Matrix2):
        m1 = np.array(Matrix1)
        m2 = np.array(Matrix2)
        return np.matmul(m1,m2).tolist()            


if __name__ == "__main__":
    cal = calculator()
    print((cal.addition([1,2],[2,1])))
    print((cal.subtraction([1,2],[2,1])))
    print((cal.multiplication([2,1],[[1],[2]])))
    print(cal.eigenvetor([[1,2],[3,4]]))
    print(cal.eigenvalue([[1,2],[3,4]]))
