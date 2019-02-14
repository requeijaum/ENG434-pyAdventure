#!/bin/env python3

# rascunho do jogo de Adventure em Python3
# https://wiki.python.org.br/SocketBasico    em TCP !
# jogo do cliente

import socket

#HOST = 'requeijaum.ddns.net'
#PORT = 32100

HOST = '127.0.0.1'
PORT = 8921 #ADV0 em T9

tcp = socket.socket(
    socket.AF_INET, socket.SOCKSTREAM
)

dest = (HOST, PORT)

tcp.connect(dest)
print "Para sair use CTRL+X\n"

msg = raw_input()

while msg <> '\x18':
    tcp.send (msg)
    msg = raw_input()
tcp.close()

