CRC_GENERATOR = "1011"
WORD_LEN = 5

class crc:

    def num_to_binary(self, num):
        binary = bin(num)[2:]
        return binary


    def string_to_binary(self, msg):
        op = ""
        for char in msg:
            if char != " ":
                num = ord(char) - 64
                op  += self.num_to_binary(num)
            else:
                op  += self.num_to_binary(27)
        return op


    def xor(self, str1, str2):
        xr = ""
        for i in range(len(str1)):
            if str1[i]==str2[i]:
                xr += "0"
            else:
                xr += "1"
        return xr


    def generateCRC(self, binary_msg):
        binary_msg += "000"
        rem = ""
        str2 = ""
        i = 0
        while i<=len(binary_msg):

            if len(str2)==0:
                start = False

            while( len(str2)<4 and i<=len(binary_msg)):
                if i<len(binary_msg):
                    if binary_msg[i] == "0" and start == False:
                        i+=1
                        continue
                    str2 += binary_msg[i]
                i+=1
                start = True
            
            if len(str2)<4:
                ze = ""
                for z in range(3-len(str2)):
                    ze+="0"
                rem = ze + str2
                break
            
            str2 = self.xor(CRC_GENERATOR, str2)
            k=0
            while (k<len(str2) and str2[k]=="0"):
                str2 = str2[1:] 
        return binary_msg[:-3] + rem