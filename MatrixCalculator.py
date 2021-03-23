import numpy as np

class calculator:

    def addition(self,Matrix1,Matrix2):
        m1 = np.array(Matrix1)
        m2 = np.array(Matrix2)
        M = np.add(m1,m2).astype(float).tolist()
        return M
        
    def subtraction(self,Matrix1,Matrix2):
        m1 = np.array(Matrix1)
        m2 = np.array(Matrix2)
        M = np.subtract(m1,m2).astype(float).tolist()
        return M
        
    def multiplication(self,Matrix1,Matrix2):
        m1 = np.array(Matrix1)
        m2 = np.array(Matrix2)
        M = np.matmul(m1,m2).astype(float).tolist()
        return M
    
    def multiply(self,number,Matrix1):
        m1 = np.array(Matrix1)
        M = np.multiply(m1,number).astype(float).tolist()
        return M

    def dot(self,Matrix1,Matrix2):
        m1 = np.array(Matrix1)
        m2 = np.array(Matrix2)
        M = np.dot(m1,m2).astype(float).tolist()
        return M

    def eigenvetor(self,Matrix1):
        m1 = np.array(Matrix1)
        vectors = np.linalg.eig(m1)[-1]
        for vector in vectors:
            vector = vector.astype(float).tolist()
        return list(vectors.tolist())

    def eigenvalue(self,Matrix1):
        m1 = np.array(Matrix1)
        values = np.linalg.eigvals(m1).tolist()
        for value in values:
            value = float(value)
        return list(values)

    def inverse(self,Matrix1):
        m1 = np.array(Matrix1)
        inverse_m = np.linalg.inv(m1).astype(float).tolist()
        return list(inverse_m)

    def determinant(self,Matrix1):
        m1 = np.array(Matrix1)
        det = np.linalg.det(m1)
        det = float(det)
        return det

    def T(self,Matrix1):
        return np.transpose(Matrix1).astype(float).tolist()

    def norm_L2(self,Matrix1):
        return np.linalg.norm(Matrix1).tolist()

    def squared_magnitude(self,Matrix1):
        squared_mag = 0
        for number in Matrix1:
            squared_mag += number ** 2
        return squared_mag

if __name__ == "__main__":
    cal = calculator()
    add = (cal.addition([[1,2]],[[2,1]]))
    print(str(add) + " type: " + str(type(add)))
    print(" type: " + str(type(add[0][0])))
    minus = (cal.subtraction([[1,2]],[[2,1]]))
    print(str(minus) + " type: " + str(type(minus)))
    print(" type: " + str(type(minus[0][0])))
    multiplication = (cal.multiplication([[1],[2],[3]],[[1,2,3]]))
    print(str(multiplication) + " type: " + str(type(multiplication)))
    print(" type: " + str(type(multiplication[0][0])))
    det = (cal.determinant([[3,2],[3,4]]))
    print(str(det) + " type: " + str(type(det)))
    dot = cal.multiply(5,[[1,2],[3,4]])
    print(str(dot) + " type: " + str(type(dot)))
    print(" type: " + str(type(dot[0][0])))
    eigenvalue = (cal.eigenvalue([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]))
    print(str(eigenvalue) + " type: " + str(type(eigenvalue)))
    print(" type of eigenvalue: " + str(type(eigenvalue[0])))
    eigenvector = cal.eigenvetor([[7,5,5],[5,0,0],[5,0,3]])
    print(str(eigenvector) + " type: " + str(type(eigenvector)))
    print(" type of eigenvector: " + str(type(eigenvector[0])) + " type of element in it " + str(type(eigenvector[0][0])))
    T = cal.T([[7,5,5],[0,0,0],[0,0,0]])
    print(str(T) + " type: " + str(type(T)))
    print(" type: " + str(type(T[0][0])))
    inverse = cal.inverse(([[1,2],[2,1]]))
    print(str(inverse) + " type: " + str(type(inverse)))
    print(" type: " + str(type(inverse[1][0][0])))

