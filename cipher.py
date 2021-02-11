A = [[-3,-3,-4], [0,1,1], [4,3,4]]
A_inverse = [[1,0,1], [4,4,3], [-4,-3,-3]]

class cipher:

    def getInt(self, ch):
        if ch != " ":
            num = ord(ch) - 64
            return num
        else:
            return 27


    def convert_to_block(self, msg):
        no_of_char = len(msg)
        padd = ""
        for i in range(3-(no_of_char%3)):
            padd += " "
        msg += padd
        col = len(msg)//3
        row = 3

        matrix = [[0 for i in range(col)] for j in range(row)]

        idx = 0
        for j in range(col):
            for i in range(row):
                matrix[i][j] = self.getInt(msg[idx])
                idx+=1
        return matrix


    def dot_product(self, matrix1, matrix2):

        row = len(matrix1)
        col = len(matrix2[0])

        matrix = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):
                num = 0    
                for k in range(len(matrix1[0])):
                    num += matrix1[i][k]*matrix2[k][j]
                matrix[i][j] = num
        return matrix


    def encrypt(self, msg):
        matrix = self.convert_to_block(msg)
        res = self.dot_product(A, matrix)
        encoded_msg = str(res)
        return encoded_msg

    
    def decrypt(self, msg):

        matrix = eval(msg)
        res = self.dot_product(A_inverse, matrix)
        col = len(res[0])
        row = len(res)
        data = ""
        for j in range(col):
            for i in range(row):
                num = res[i][j]
                if num==27:
                    data += " "
                else:
                    data += chr(num + 64)
        return data