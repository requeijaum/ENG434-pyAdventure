#!/usr/bin/python           # This is server.py file                                                          

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
        print(addr, ' >> ', data_received)
        #msg = input('SERVER >> ')
        
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        
        #clientsocket.send(msg)

    clientsocket.close()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 50123                # Reserve a port for your service.

print('Server started!')
print("HOST: ", host, ":", str(port))
print('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

#print('Got connection from', addr)

print("Para sair use CTRL+X\n")
msg = ""

while msg != '\x18':
   c, addr = s.accept()     # Establish connection with client.
   _thread.start_new_thread(on_new_client,(c,addr))
   
   msg = input()

   #Note it's (addr,) not (addr) because second parameter is a tuple
   #Edit: (c,addr)
   #that's how you pass arguments to functions when creating new threads using thread module.
   
s.close()