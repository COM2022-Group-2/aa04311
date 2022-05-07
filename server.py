import socket
import time
from zmq import Message
from datetime import date
import threading

class Client:
    def __init__(aelf, name, bday, ip):
        self.name = name
        self.bday = bday
        self.ip = ip


Clients = {
    'Adrian': [(date(2001, 9, 20)), b"192.168.0.4"],   
    'Terry': [(date(2000, 4, 25)), b"192.168.247.1"],
    'John': [(date(1989, 10, 20)), b"192.168.0.1"],
    'alaehm': [(date(2022, 5, 5)), b"10.78.181.215"],
}


def receive():
    while True:
        for key in Clients:
            bdate = (Clients[key][0])
            
            if (bdate).strftime('%y/%m/%d') == date.today().strftime('%y/%m/%d'):
                UDP_IP = Clients[key][1]
                print(UDP_IP)
                UDP_PORT = 1001
                MESSAGE = "Happy birthday " + key
                MESSAGE = str.encode(MESSAGE)
                sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
                sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
                print("UDP target IP: %s" % UDP_IP)
                print("UDP target port: %s" % UDP_PORT)

                MESSAGE = bytes.decode(MESSAGE)

                print("message: %s" % MESSAGE)

                Clients[key][0] = date(int(str(bdate.year)) + 1, bdate.month, bdate.day)

thread = threading.Thread(target=receive)
thread.start()