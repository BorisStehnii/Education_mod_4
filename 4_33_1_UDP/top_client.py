from socket import *


while True:
    try:
        message = input("message: ")

        client = socket(AF_INET, SOCK_DGRAM)

        if message == 'quit':
            client.close()
            break

        addr = ('192.168.0.101', 4000)
        client.sendto(message.encode(), addr)

        server_resp = client.recvfrom(1024)
        print(server_resp.decode())
    finally:
        client.close()

