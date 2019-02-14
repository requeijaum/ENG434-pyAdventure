#!/bin/env python3

# rascunho do jogo de Adventure em Python3
# https://wiki.python.org.br/SocketBasico    em TCP !
# jogo do servidor

import socket

HOST = ''
PORT = 8921 #ADV0 em T9

tcp = socket.socket(
    socket.AF_INET, socket.SOCKSTREAM
)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    print 'Conectado por: ', cliente   
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
    print 'Finalizando conexao do cliente ', cliente
    con.close()


