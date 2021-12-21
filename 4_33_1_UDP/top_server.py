from socket import *

try:

    server = socket(AF_INET, SOCK_DGRAM)
    addr = ('192.168.0.101', 4000)
    server.bind(addr)

    while True:
        # c_sock, c_addr = soc.accept()
        #
        # c_message = c_sock.recv(1000).decode()
        c_message, c_addr = server.recvfrom(1024)

        print(c_addr, ': ', c_message.decode())

        message = input("message: ")
        if message == 'quit':
            server.close()
            break
        server.sendto(message.encode(), c_addr)


finally:
    server.close()

