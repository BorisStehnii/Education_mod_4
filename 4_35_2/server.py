from socket import *
import threading


def client_soc_(client_sock, client_addr):
    while True:
        c_msg = client_sock.recv(1000).decode()
        if c_msg == 'exit':
            break
        print(f"{client_addr}>>{c_msg}")
    client_sock.close()


soc = socket(AF_INET, SOCK_STREAM)

soc.bind(('localhost', 4000))
soc.listen(1)

while True:

    c_sock, c_add = soc.accept()
    thrd = threading.Thread(target=client_soc_, args=(c_sock, c_add))
    thrd.start()
