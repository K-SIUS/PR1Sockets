import socket
import random
import time
#esqueleto sacado en: https://github.com/mittalmehul/socket-server
#Ander Sarrión Martón
seed= 7777
random.seed(seed)


ClientSocket = socket.socket()
print('Esperando para conectar')
try:
    ClientSocket.connect(('localhost',8080))
except socket.error as e:
    print(str(e))

while True:
    Response = ClientSocket.recv(1024)
    Recibido=Response.decode('utf-8')
    print(Recibido)
    #Con esto genero el aleatorio con el que duerme el agente
    #habrá que adaptarlo a ms probablemente.
    randomGenerated=random.randint(0,9)
    time.sleep(randomGenerated)
    RHelp= random.randint(1,3)
    
    if RHelp == 1:
    #mandamos ayuda
        ClientSocket.send(str.encode('Mando_Ayuda')) 
        print("Ayudo")
    else:
        ClientSocket.send(str.encode('no'))
        print("No ayudo")
    
ClientSocket.close()