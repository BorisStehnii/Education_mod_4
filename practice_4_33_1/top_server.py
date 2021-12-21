from socket import *

try:

    soc = socket(AF_INET, SOCK_STREAM)

    soc.bind(('192.168.0.101', 4000))
    soc.listen(1)

    while True:
        c_sock, c_addr = soc.accept()

        c_message = c_sock.recv(1000).decode()
        print(c_addr, ': ', c_message)

        message = input("message: ")
        if message == 'quit':
            c_sock.close()
            break
        c_sock.send(message.encode())

        c_sock.close()

finally:
    c_sock.close()
    soc.close()

