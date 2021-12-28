from socket import *
import multiprocessing as mp


def client_soc_(client_sock, client_addr):
    while True:
        c_msg = client_sock.recv(1000).decode()
        if c_msg == 'exit':
            break
        print(f"{client_addr}>>{c_msg}")
    client_sock.close()


if __name__ == "__main__":
    soc = socket(AF_INET, SOCK_STREAM)

    soc.bind(('localhost', 4000))
    soc.listen(1)

    with mp.Pool() as pool:
        c_sock, c_add = soc.accept()
        while True:
            pool.apply(client_soc_, args=(c_sock, c_add))
