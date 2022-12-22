import socket
from _thread import *
import time
import random
#esqueleto sacado en: https://github.com/mittalmehul/socket-server
#Ander Sarrión Martín
clients = []
iteracion= 0
helps = 0
agentes = 0
def broadcast(message):
    for client in clients:
        client.send(message)

def handle(conexion):
    global helps
    global iteracion
    ready = False
    print("Esperando a los tres agentes para continuar...")
    while True:
        #inicialmente hay que bloquear el intercambio de mensajes hasta que los tres
        #clientes se hayan conectado
        while ready == False:
            if agentes <=3:
                ready = False
            else:
                ready = True
        iteracion = iteracion+1
        try:
            #mandamos mensaje de ayuda
            conexion.sendall(str.encode("necesito ayuda%i"%iteracion))
            #a mimir
            time.sleep(random.randint(0,9))
            message = conexion.recv(1024)
            message.decode('utf-8')
            print(message)
            if message == 'no':
                pass
            elif message == 'Helped':
                helps= helps+1
                print("ayudas: ", helps)
        except:
            print("timeout")
            pass
    
        if (helps == 3):
            conexion.sendall(str.encode("servidor ayudado"))
            conexion.close()
    
def aceptar_conexion(server):
    global agentes
    agentes = agentes +1
    conexion, direccion = server.accept()
    print('Conectado a', direccion)
    start_new_thread(handle, (conexion, ))

#creamos socket vía TCP con SOCK_STREAM
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#presenta la ip y el número de puerto
serverAddr = ('localhost',8080)
#bindeamos el host y el puerto
print("Habilitando socket  en {} con puerto {}".format(*serverAddr))
server.bind(serverAddr)

#ahora se supone que el servidor debe esperar a recibir conexiones
#pongo un 3 suponiendo que ha de entablar 3 conexiones TCP 
server.listen(3)

while True: 
    aceptar_conexion(server)



print("Server is listening... ")



'''
#Aquí empieza el bucle infinito
while True:

#esto acepta las conexiones que lleguen. sockConnection corresponde 
#a la conexión con el socket, y newIp con la nueva Ip
#no tengo muy claro como va esto
    print('Esperando a las conexiones')
    sockConnection, newIp = server.accept()
    print('Conectado a', newIp)
    peticion= 'Necesito Ayuda'
    bytes= str.encode(peticion)
    HelpNeeded= True
    while HelpNeeded:
        #reiniciamos Contador de ayuda
        helpCount=0
        #mandamos petición de ayuda
        sockConnection.sendall(bytes)
        print(bytes)
        if helpCount >= 2:
            print('Ayuda recibida con éxito\n')
            HelpNeeded= False
        print("Espero a recibir ayudas.\n")
    #hace falta try catch al parecer
        try:

        #Duda seria ¿como distingo entre agentes? 
        # ¿la concurrencia de esto?
            mensj= sockConnection.recv(1024)
            print(mensj)
            print('Ayuda recibida por parte de Agente')
            helpCount += 1
    #como último paso se cerrará la conexión de los sockets
        finally:
            sockConnection.close


'''