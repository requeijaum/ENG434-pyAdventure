#!/usr/bin/python           # This is server.py file                                                          


# conceitos legais em : https://www.smashingmagazine.com/2018/12/multiplayer-text-adventure-engine-node-js/

# ler atributos de uma maneira legal
# https://stackoverflow.com/questions/11975781/why-does-getattr-not-support-consecutive-attribute-retrievals
import operator


import json 
mainGame = None
with open('jogo1.json', 'r') as f :
    mainGame = json.loads(f.read())
    f.close()
    print("\n\nDEBUG: type(mainGame):" + str(type(mainGame)))
    print("DEBUG: mainGame.keys():")
    print(mainGame.keys())
    print("\nJSON carregado corretamente!\n")

#print(mainGame)
listaJogadores = []
# carregamos o objeto do jogo... falta funcoes


def getRoomMessage(locationID):
    global mainGame
    # entrar em mainGame.rooms.nomeDaSala.description.default
    #print(mainGame) #DEBUG
    #f = attrgetter("rooms." + locationID + ".description.default")
    #print(f(mainGame))
    return mainGame["rooms"][locationID]["description"]["default"]











# instanciar jogador

class Jogador:
   'Classe base para todos os jogadores'
   contaJogadores = 0
   hp = 100
   locationID = None

   def __init__(self, nome, con):
      self.id   = Jogador.contaJogadores
      self.nome = nome
      self.con  = con
      #self.addr = addr
      
      Jogador.contaJogadores += 1
   
   def quantosJogadores(self):
     print ("Jogadores totais: %d" % Jogador.contaJogadores)

   def mostraJogador(self):
      print ("Nome : ", self.nome,  ", Conexao: ", self.con) #(self.con,self.addr) )

   def changeLocation(self, graph , rosa_dos_ventos):
       print("DEBUG: local = " + self.locationID )
       # precisa ter um local anterior setado! --> "entrance"
       #listaProximosLocais = graph 
       # agora precisamos iterar na lista pra saber onde estamos e pra onde ir
       for localAtual in graph:
           if localAtual.id == self.locationID:
                self.location = getattr(graph, rosa_dos_ventos ) #acessar "north" em graph.entrance
                print("DEBUG: local = " + self.locationID )
      

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


# home.hccnet.nl/r.helderman/adventures/htpataic02.html

def getInput(clientsocket):
    #print("-->")
    
    return clientsocket.recv(1024).decode()


def parseAndExecute(recv_txt, player, mainGame):
    
    verb = recv_txt.split(" ")[0]
    noun = None

    if verb == "quit" : 
        #desconectar()
        print("DEBUG: desconectar()")

    if verb == "north" or verb == "south" or verb == "east" or verb == "west" :
        #player.changeLocation(mainGame["graph"], verb) # changeLocation(self, graph , rosa_dos_ventos):
        print("player.changeLocation(mainGame['graph'], verb)")


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

        

        nomeConfirma = False

        while nomeConfirma == False :

            msg = "Qual o seu nome?" + "\n"
            clientsocket.send(msg.encode())

            nome = clientsocket.recv(1024).decode()
            msg = "Seu nome é: '" + nome + "' ?" + "\n"
            clientsocket.send(msg.encode())

            nomeConfirmacao = clientsocket.recv(1024).decode()
            
            if nomeConfirmacao == "sim" :
                msg = "/playername " + nome + "\n"
                clientsocket.send(msg.encode())
                nomeConfirma = True

            else :
                msg = "Tente novamente!\n"
                clientsocket.send(msg.encode())
                nomeConfirma = False
            
        # talvez bugue
        # iniciar jogo aqui

        player = Jogador(nome, clientsocket)

        '''
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

        '''

        # iniciar logica do jogo
        gameOn = True
        
        while gameOn:

            
            # levar jogador à entrada

            player.locationID = "entrance"

            # imprimir mensagem
        
            msg = getRoomMessage(player.locationID)
            clientsocket.send(msg.encode())

            #player.changeLocation(mainGame.graph , comando)

            gameOn = False



        #else :
        #    msg = "Por favor, cumprimente o servidor corretamente!"
        #    clientsocket.send(msg.encode())



    print("Finalizando conexão do cliente: ", addr)
    clientsocket.close()


def player_instance(con,addr): #sock = con,addr
    on_new_client(con,addr)




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
        _thread.start_new_thread(player_instance,(con,addr))
        
        #msg = input()

        #Note it's (addr,) not (addr) because second parameter is a tuple
        #Edit: (c,addr)
        #that's how you pass arguments to functions when creating new threads using thread module.
        
    s.close()


if __name__ == '__main__': 
    Main() 
    quit