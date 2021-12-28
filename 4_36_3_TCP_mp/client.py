from socket import *


soc = socket(AF_INET, SOCK_STREAM)
soc.connect(('localhost', 4000))
while True:

    message = input("message: ")
    if message == 'quit':
        break
    soc.send(message.encode())
soc.close()
