#JOCELYNE GONZÁLEZ HERNÁNDEZ
#SANDRA LORENA QUIJADA LEÓN

import socket
import threading
import os
from datetime import datetime

print_lock = threading.Lock()

def threaded(connectionSocket, addr):
    while True:
        opcion = connectionSocket.recv(1024) 
        op = opcion.decode()
        if op == '1':
            hora = datetime.now().strftime("[%H:%M:%S]")
            message="La hora es:" + hora
            connectionSocket.send(message.encode())

        elif op == '2':
            sentence = connectionSocket.recv(1024)
            msg = sentence.decode()
            mayuscula = msg.upper()
            count_s = mayuscula.count("S")
            message = "El número de letras 'S' en la cadena es: " + str(count_s)
            connectionSocket.send(message.encode())

        elif op == '3':
            dir_path = "/home"
            dir_list = os.listdir(dir_path)
            message = "El contenido del directorio hogar:" + str(dir_list)
            connectionSocket.send(message.encode())

        else:
            message = "Opción no válida"
            connectionSocket.send(message.encode())

    connectionSocket.close()

def main():
    serverPort = 12001
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(("192.168.127.215", serverPort))
    serverSocket.listen(5)
    print("Servidor listo para recibir TCP")

    while True:
        connectionSocket, addr = serverSocket.accept()
        print_lock.acquire()
        print("Conectado con " + addr[0] + ":" + str(addr[1]))

        client_thread = threading.Thread(target=threaded, args=(connectionSocket, addr))
        client_thread.start()

    serverSocket.close()

if __name__ == "__main__":
