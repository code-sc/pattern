class matrix:
    """class matrix
        usage: c = matrix(dim,num)
        
            -dim = A tuple (r,c) 
                => r for number of rows
                => c for number of columns
            -num = float to fill matix with (default 1.0)
            
        attributes:
        
            -row
            -col
            -M
        
        modules:
            #-shape()
    """
    #CONSTRUCTOR
    def __init__(self,dim,num=1.0):
        self.row = dim[0]
        self.col = dim[1]
        self.M = [[num] * self.col for i in range(self.row)]
    
    #FOR DISPLAY OF MATRIX
    def __str__(self):
        mtxStr = "------------- output -------------\n"
        for i in range(self.row):
            mtxStr += ('|' + ', '.join(map(lambda x:'{0:8.3f}'.format(x),self.M[i])) + '| \n')
        mtxStr += '----------------------------------'
        return mtxStr
    
    #MATRIX ADDITION WITH ANOTHER MATRIX AND A SCALAR
    def __add__(self,other):
        #matrix to be added into
        ans = matrix(dim = (self.row,self.col),num = 0.0)
        
        #check if scalar
        if isinstance (other,(int,float)):
            for i in range(self.row):
                for j in range(self.col):
                    ans.M[i][j] = self.M[i][j] + other
        
        #check if matrix and of correct dimensions
        elif isinstance(other,matrix):
            if self.row==other.row and self.col==other.col:
                for i in range(self.row):
                    for j in range(self.col):
                        ans.M[i][j] = self.M[i][j] + other.M[i][j]
            else:
                raise TypeError("Size of matrix doesn't match")
        else:
            raise TypeError("Matrix ,int or float required for addition")
        return ans
    
    #RIGHT ADDITION (PRESERVING COMMUTATIVITY)
    def __radd__(self,other):
        return self.__add__(other)
    
    #MATRIX SUBTRACTION WITH ANOTHER MATRIX AND A SCALAR
    def __sub__(self,other):
        #matrix to be subtracted into
        ans = matrix(dim = (self.row,self.col),num=0.0)
        
        #check for scalar
        if isinstance (other,(int,float)):
            for i in range(self.row):
                for j in range(self.col):
                    ans.M[i][j] = self.M[i][j] - other
        
        #check for matrix and correct dimensions
        elif isinstance (other,matrix):
            if self.row==other.row and self.col==other.col:
                for i in range(self.row):
                    for j in range(self.col):
                        ans.M[i][j] = self.M[i][j] - other.M[i][j]
            else:
                raise TypeError("Size of matrix doesn't match")
        else:
            raise TypeError("Matrix ,int or float required for subtraction")
        return ans

    #RIGHT SUBTRACTION (SCALAR - MATRIX)
    def __rsub__(self,other):
        #matrix to be subtracted into
        ans = matrix(dim = (self.row,self.col),num=0.0)
        
        #check if other is scalar
        if isinstance(other,(int,float)):
            for i in range(self.row):
                for j in range(self.col):
                    ans.M[i][j] = other - self.M[i][j]
        else:
            raise TypeError("Matrix ,int or float required for subtraction")
        return ans

    #POINTWISE MULTIPLICATION OF MATRIX AND SCALAR
    def __mul__(self,other):
        #matrix for answer
        ans = matrix(dim=(self.row,self.col),num = 0)
        
        if isinstance(other,(int,float)):
            for i in range(self.row):
                for j in range(self.col):
                    ans.M[i][j] = other * self.M[i][j]
        elif isinstance(other,matrix):
            if self.row==other.row and self.col==other.col:
                for i in range(self.row):
                    for j in range(self.col):
                        ans.M[i][j] = self.M[i][j] * other.M[i][j]
            else:
                raise TypeError("Size of matrix doesn't match")
        else:
            raise TypeError("Matrix ,int or float required for pointwise multiplication")
        return ans
    
    #REVERSE POINTWISE MULTIPLICATION (PRESERVING COMMUTATIVITY)
    def __rmul__(self,other):
        return self.__mul__(other)
    
    #MATRIX MULTIPLICATION
    def __matmul__(self,other):
        #check if other is matrix
        if isinstance(other,matrix):
            if self.col==other.row:
                ans = matrix(dim=(self.row,other.col),num=0.0)
                for i in range(self.row):
                    for j in range(other.col):
                        for k in range(self.col):
                            ans.M[i][j] += self.M[i][k] * other.M[k][j]
                return ans
            else:
                raise TypeError("Size mismatch for matrix multiplication")
        else:
            raise TypeError("Matrix is required for matrix multiplication")

    #GET ITEM USING INDEX
    def __getitem__(self,key):
        if isinstance(key,tuple):
            i = key[0]
            j = key[1]
            return self.M[i][j]
        else:
            raise ValueError("Invalid index for matrix")
    
    #SET ITEM VALUE USING INDEX
    def __setitem__(self,key,value):
        if isinstance(key,tuple) and isinstance(value,(int,float)):
            i = key[0]
            j = key[1]
            self.M[i][j] = value

    #RETURN DIMENSION OF MATRIX
    def shape(self):
        """ Returns the shape of matrix as a tuple (row,column)"""
        return (self.row,self.col)
            
