import socket
from cipher import *
from crc import *
import sys

#------------------------------------------- GLOBAL VARIABLES ---------------------------------------------------#

host = '127.0.0.1'
port = 8888

class client:

    def encode(self, cmd):
        cpr = cipher()
        cr = crc()
        encoded_msg = cpr.encrypt(cmd)
        binary_msg = cr.string_to_binary(cmd)
        CRC = cr.generateCRC(binary_msg)
        return encoded_msg + "||" + CRC

    #----------------------------------------------------------------------------------------------------------------#

    def send(self,ClientSocket, cmd):
        ClientSocket.send(str.encode(cmd))
        Response = ClientSocket.recv(1024).decode('utf-8')
        return ("Server :\> " + Response)

    #----------------------------------------------------------------------------------------------------------------#

    def main(self):
        print()
        print("----------------------> CLIENT <--------------------\n")

        ClientSocket = socket.socket()
        ClientSocket.connect((host, port))

        while True:
            cmd = input("Enter Your Mesage: ")
            cmd = self.encode(cmd)
            resp = self.send(ClientSocket, cmd)
            print(resp)
            print()
        ClientSocket.close()

    #----------------------------------------------------------------------------------------------------------------#

c1=client()
c1.main()