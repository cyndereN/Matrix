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
        M = np.matmul(m1,m2).tolist()
        return M
    
    def multiply(self,number,Matrix1):
        m1 = np.array(Matrix1)
        M = np.multiply(Matrix1,number).tolist()
        return M

    def dot(self,Matrix1,Matrix2):
        m1 = np.array(Matrix1)
        m2 = np.array(Matrix2)
        return np.dot(m1,m2).tolist()

    def eigenvetor(self,Matrix1):
        m1 = np.array(Matrix1)
        vectors = np.linalg.eig(m1)[-1]
        for vector in vectors:
            vector = vector.tolist()
        return tuple(vectors.tolist())

    def eigenvalue(self,Matrix1):
        m1 = np.array(Matrix1)
        values = np.linalg.eigvals(m1)
        return tuple(values)

    def inverse(self,Matrix1):
        r = len(Matrix1)
        m1 = np.array(Matrix1)
        det_m1 = self.determinant(m1)
        m2 = det_m1 * np.eye(r,r)
        inverse_m = np.linalg.solve(m1,m2)
        for row in inverse_m:
            for element in row:
                element = (element)
        return det_m1, inverse_m.tolist()        

    def determinant(self,Matrix1):
        m1 = np.array(Matrix1)
        return (np.linalg.det(m1))

    def T(self,Matrix1):
        return np.transpose(Matrix1).tolist()

    def norm_L2(self,Matrix1):
        return np.linalg.norm(Matrix1).tolist()

    def squared_magnitude(self,Matrix1):
        squared_mag = 0
        for number in Matrix1:
            squared_mag += number ** 2
        return squared_mag

if __name__ == "__main__":
    cal = calculator()
    # print((cal.addition([1,2],[2,1])))
    # print((cal.subtraction([1,2],[2,1])))
    print((cal.multiplication([[1],[2],[3]],[[1,2,3]])))
    # print(cal.determinant([[3,2],[3,4]]))
    print((cal.eigenvalue([[1,2,3],[2,2,2],[3,2,1]])))
    # print(cal.eigenvetor([[7,5,5],[5,0,0],[5,0,3]]))
    # print(cal.T([[7,5,5],[0,0,0],[0,0,0]]))
    # print(cal.inverse(([1,2],[2,1])))

