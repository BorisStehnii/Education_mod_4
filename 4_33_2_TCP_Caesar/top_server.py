from socket import *

try:

    soc = socket(AF_INET, SOCK_STREAM)

    soc.bind(('localhost', 4000))
    soc.listen(1)

    while True:
        c_sock, c_addr = soc.accept()
        c_key = c_sock.recv(1000).decode()
        c_sock.close()
        c_sock, c_add = soc.accept()
        c_msg = c_sock.recv(1000).decode()

        if c_key.isdigit():
            res_msg = ""
            for i in c_msg:
                res_msg += chr(ord(i) + int(c_key))
        else:
            res_msg = "Key not type int"

        message = res_msg
        print(message)
        c_sock.send(message.encode())
        c_sock.close()

finally:
    c_sock.close()
    soc.close()

