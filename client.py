import socket

#THIS ONE IS FOR CHECKING LOCAL PC IP ADDRESS
#UDP_IP = socket.gethostbyname(socket.gethostname())
UDP_PORT = 1001

hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((host_ip, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = bytes.decode(data) #change binary to string so the 'b' before the message wont show
    print("received message: %s" % data)