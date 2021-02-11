import socket
import os
import sys
from cipher import *
from crc import *
from _thread import *
import json

IP = '127.0.0.1'
PORT = 8888

#----------------------------------------------------------------------------------------------------------------#

class server:

    def process_request(self, received_data):

        cpr = cipher()
        cr = crc()        

        encoded_data, CRC = received_data.split("||")

        data = cpr.decrypt(encoded_data)
        recCRC = cr.generateCRC(CRC)
        if recCRC[-3:] == "000":
            print()
            print("Received Data : ", data)
            print()
            return "Data received!"
        else:
            return "Data corrupted!"

    #----------------------------------------------------------------------------------------------------------------#

    def threaded_client(self,connection):
        while True:
            data = connection.recv(2048).decode('utf-8')
            resp = self.process_request(data)
            if not data:
                break
            connection.sendall(str.encode(resp))
        connection.close()

	#----------------------------------------------------------------------------------------------------------------#

    def main(self):
        ServerSocket = socket.socket()
        ServerSocket.bind((IP, PORT))
        print('\nListening..')
        ServerSocket.listen(5)

        while True:
            Client, address = ServerSocket.accept()
            start_new_thread(self.threaded_client, (Client,))
        ServerSocket.close()

    #----------------------------------------------------------------------------------------------------------------#

s1=server()
s1.main()