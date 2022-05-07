import socket
import time
from zmq import Message
from datetime import date
import threading
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


##############################
##############################
# please install this library to run the code
# pip install pycrypto
##############################
##############################


myPrivate = RSA.generate(128 * 8)
myPublic = myPrivate.publickey()

class Client:
    def __init__(aelf, name, bday, ip):
        self.name = name
        self.bday = bday
        self.ip = ip

key = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQClw1qhIqzgIFHoR9n4/VilSuym\nadp3LLqO9XExg1V4wUHAQuEF+gobMUHzm1Vck2djSHkIMTZ33SLy3tI8Zoqi7vVK\nQ0xWhaxQn6hvEHt98MRWAjunAokkl3iq8o19pUCxerK1Jw/R68LjTUzf+xEXH3uD\nz/FQFgQIrYoVzpB5wwIDAQAB\n-----END PUBLIC KEY-----"


Clients = {
    'Adrian': [(date(2001, 9, 20)), b"192.168.0.4"],   
    'Terry': [(date(2000, 4, 25)), b"192.168.247.1"],
    'John': [(date(1989, 10, 20)), b"192.168.0.1"],
    'alaehm': [(date(2022, 5, 5)), b"10.78.181.215", "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQClw1qhIqzgIFHoR9n4/VilSuym\nadp3LLqO9XExg1V4wUHAQuEF+gobMUHzm1Vck2djSHkIMTZ33SLy3tI8Zoqi7vVK\nQ0xWhaxQn6hvEHt98MRWAjunAokkl3iq8o19pUCxerK1Jw/R68LjTUzf+xEXH3uD\nz/FQFgQIrYoVzpB5wwIDAQAB\n-----END PUBLIC KEY-----"],
}


def encrypt(msg, clientKey):
    pub_key = RSA.import_key(clientKey.encode())
    key = PKCS1_OAEP.new(pub_key)
    return key.encrypt(msg.encode())



def receive():
    while True:
        for key in Clients:
            bdate = (Clients[key][0])
            
            if (bdate).strftime('%y/%m/%d') == date.today().strftime('%y/%m/%d'):
                UDP_IP = Clients[key][1]
                print(UDP_IP)
                UDP_PORT = 1001
                MESSAGE = "Happy birthday " + key
                # MESSAGE = str.encode(MESSAGE)
                sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

                encrypted_msg = encrypt(MESSAGE, Clients[key][2])

                sock.sendto(encrypted_msg, (UDP_IP, UDP_PORT))
                print("UDP target IP: %s" % UDP_IP)
                print("UDP target port: %s" % UDP_PORT)

                print("message: %s" % MESSAGE)

                Clients[key][0] = date(int(str(bdate.year)) + 1, bdate.month, bdate.day)

thread = threading.Thread(target=receive)
thread.start()
# key=  myPublic.exportKey().decode()
# print(key)

