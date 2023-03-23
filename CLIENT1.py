#JOCELYNE GONZÁLEZ HERNÁNDEZ
#SANDRA LORENA QUIJADA LEÓN

import socket
import threading

serverName = "192.168.127.215"
serverPort = 12001
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def main():
    while True:
        print("Elige una opcion")
        print("1. Mostrar la hora del servidor")
        print("2. Contar el número de 'S' en una cadena")
        print("3. Contenido del directorio hogar")

        opcion = input("Escoge una opción: ")
        clientSocket.send(opcion.encode())

        if opcion == '1':
            modifiedSentence = clientSocket.recv(1024)
            print(modifiedSentence.decode())

        elif opcion == '2':
            sentence = input("Input lower sentence:")
            clientSocket.send(sentence.encode())
            modifiedSentence = clientSocket.recv(1024)
            print(modifiedSentence.decode())

        elif opcion == '3':
            modifiedSentence = clientSocket.recv(1024)
            print(modifiedSentence.decode())
        else:
            print("\nOpción no válida")

        opcion = input("\n ¿Desea continuar? S / N: ")
        if opcion == 'S':
            continue

        elif opcion == "N":
            break
    print("BYE")

if _name_ == "_main_":
    main()
