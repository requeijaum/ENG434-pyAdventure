#!/usr/bin/python           # This is server.py file                                                          

class Jogador:
   'Classe base para todos os jogadores'
   contaJogadores = 0

   def __init__(self, nome, itemInicial):
      self.nome = nome
      self.itemInicial = itemInicial
      Jogador.contaJogadores += 1
   
   def quantosJogadores(self):
     print ("Jogadores totais: %d" % Jogador.contaJogadores)

   def mostraJogador(self):
      print ("Nome : ", self.nome,  ", Item inicial: ", self.itemInicial)



# terminou classe Jogador

from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
#with Listener(
#        on_press=on_press,
#        on_release=on_release
#) as listener:   listener.join()

    

import socket               # Import socket module
import _thread


def on_new_client(clientsocket,addr):
    while True:
        data_received = clientsocket.recv(1024)
        if not data_received: break        
        #do some checks and if msg == someWeirdSignal: break:
        print("Cliente: ", addr, ' >> ', data_received.decode())
        #msg = input('SERVER >> ')
        
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.

        # iniciar novo objeto da classe Jogador

        #firstMsg = clientsocket.recv(1024).decode()
        #if firstMsg == "Olá!" :

        msg = "Qual o seu nome?" + "\n"
        clientsocket.send(msg.encode())

        nomeConfirma = False

        while nomeConfirma == False :
            nome = clientsocket.recv(1024).decode()
            msg = "Seu nome é: '" + nome + "' ?" + "\n"
            clientsocket.send(msg.encode())

            nomeConfirmacao = clientsocket.recv(1024).decode()
            
            if (nomeConfirmacao == "sim") :
                msg = "/playername " + nome + "\n"
                clientsocket.send(msg.encode())
                nomeConfirma = True
            
        # talvez bugue

        msg = "Escolha sua arma:\n    1 - pistola\n    2 - marreta\n    3 - chave inglesa\n    > Escolheu: "
        clientsocket.send(msg.encode())
        arma = clientsocket.recv(1024).decode()

        if (arma=="1") or (arma=="2") or (arma=="3"):
            #criar comando pra vincular arma ao jogador
            msg = "/playerweapon " + arma + "\n"
            clientsocket.send(msg.encode())
            
            msg = "Você escolheu " + arma + " ! Muito bem. Agora vamos..." + "\n"
            clientsocket.send(msg.encode())

            msg = "/kick " + nome + "\n"
            clientsocket.send(msg.encode())

            break        

        else:
            msg = "Tente novamente!"
            clientsocket.send(msg.encode())
            break


        #else :
        #    msg = "Por favor, cumprimente o servidor corretamente!"
        #    clientsocket.send(msg.encode())

    print("Finalizando conexão do cliente: ", addr)
    clientsocket.close()


def Main():

    
    s = socket.socket()         # Create a socket object
    host = '127.0.0.1'            #socket.gethostname() # Get local machine name
    port = 50777                # Reserve a port for your service.

    print('Server started!')
    print("HOST: ", host, ":", str(port))
    print('Waiting for clients...')

    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.

    #print('Got connection from', addr)

    print("Para sair use CTRL+X\n")
    #msg = ""

    while True: #msg != '\x18':
        con, addr = s.accept()     # Establish connection with client.
        _thread.start_new_thread(on_new_client,(con,addr))
        
        #msg = input()

        #Note it's (addr,) not (addr) because second parameter is a tuple
        #Edit: (c,addr)
        #that's how you pass arguments to functions when creating new threads using thread module.
        
    s.close()


if __name__ == '__main__': 
    Main() 
    quit