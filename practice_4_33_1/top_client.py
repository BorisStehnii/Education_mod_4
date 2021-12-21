from socket import *


while True:
    try:
        message = input("message: ")

        soc = socket(AF_INET, SOCK_STREAM)

        if message == 'quit':
            soc.close()
            break

        soc.connect(('192.168.0.101', 4000))
        soc.send(message.encode())

        server_resp = soc.recv(1000)
        print(server_resp.decode())
    finally:
        soc.close()

