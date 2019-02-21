#!/bin/env python

# USAR PYTHON3

# rascunho do jogo de Adventure em PYTHON3
# https://wiki.python.org.br/SocketBasico     em TCP !
# jogo do servidor

import socket

HOST = input("Digite o nome do host: ") #'127.0.0.1'
PORT = 50777  # ADV0 em T9

tcp = socket.socket(
    socket.AF_INET , socket.SOCK_STREAM
)

dest = (HOST, PORT)

print("HOST: " + HOST + ", PORT: " + str(PORT))


tcp.connect(dest)
print("Para sair use CTRL+X\n")

#msg = input() # estado inicial
msg = "Olá!"

print("Você disse '" + msg + "' para o servidor...")

nomeJogador     = ""
armaJogador     = ""


while (msg != '\x18') or (msg != "/kick " + nomeJogador) :            # respeitar ordem correta de operações para não dar merda
    # envia qualquer coisa
    tcp.send(msg.encode())

    data_received = tcp.recv(1024)
    print(data_received.decode())

    # transformar comandos em tuples/array com comando e argumento(s)

    if "/playername "               in data_received.decode() :
        nomeJogador = data_received.decode().replace("/playername ", "")

    if "/playerweapon "             in data_received.decode() :
        armaJogador = data_received.decode().replace("/playerweapon ", "")
        
    if "/kick " + nomeJogador       in data_received.decode() :
        nomeJogador = data_received.decode().replace("/kick ", "")
        print("Ah, não! Você foi kickado pelo servidor! :^)")
        

    #tcp.send (msg.encode())
    msg = input()
    

tcp.close()
quit
