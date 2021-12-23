from socket import *


while True:
    try:
        key = input("key: ")
        message = input("message: ")
        if message == 'quit':
            break

        soc = socket(AF_INET, SOCK_STREAM)
        soc.connect(('localhost', 4000))
        soc.send(key.encode())
        soc.close()
        soc = socket(AF_INET, SOCK_STREAM)
        soc.connect(('localhost', 4000))
        soc.send(message.encode())

        server_resp = soc.recv(1000)
        print(server_resp.decode())
    finally:
        soc.close()

