from socket import *
from threading import Thread


def send_message(sock_):
    while True:
        message = input("message: ")
        sock_.send(message.encode())


def reception_message(sock_):
    while True:
        server_resp = sock_.recv(1000)
        rec_msg = server_resp.decode()
        print(rec_msg + '\n')
        if 'disconnected' in rec_msg:
                sock_.close()
                break


if __name__ == '__main__':
    soc = socket(AF_INET, SOCK_STREAM)
    soc.connect(('localhost', 4000))

    print(">>> New connection established <<<")


    thd_send_msg = Thread(target=send_message, args=(soc,))
    thd_send_msg.start()
    thd_reception_msg = Thread(target=reception_message, args=(soc,))
    thd_reception_msg.start()


