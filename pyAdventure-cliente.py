#!/bin/env python

# USAR PYTHON3

# rascunho do jogo de Adventure em PYTHON3
# https://wiki.python.org.br/SocketBasico     em TCP !
# jogo do servidor

import socket

HOST = input("Digite o nome do host: ") #'127.0.0.1'
PORT = 50123  # ADV0 em T9

tcp = socket.socket(
    socket.AF_INET , socket.SOCK_STREAM
)

dest = (HOST, PORT)

print("HOST: " + HOST + ", PORT: " + str(PORT))


tcp.connect(dest)
print("Para sair use CTRL+X\n")

msg = input()

while msg != '\x18':
    tcp.send (msg.encode())
    msg = input()
tcp.close()
