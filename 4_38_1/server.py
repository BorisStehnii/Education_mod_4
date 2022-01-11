from socket import *
import threading
import concurrent.futures as cf


class ClientTread(threading.Thread):

    client_threads = []

    def __init__(self, c_sock, ip, port):
        super().__init__()
        self.c_sock = c_sock
        self.ip = ip
        self.port = port
        self.client_name = f"({self.ip}, {self.port})"

        self.__class__.client_threads.append(self)

    def run(self):
        try:
            while True:
                c_msg = self.c_sock.recv(1000).decode()

                if "command:quit" in c_msg:
                    self.__class__.client_threads.remove(self)
                    self.c_sock.send(f"Client: {self.client_name} disconnected.".encode())
                    print(f"Client: {self.client_name} disconnected.")
                    break
                elif "command:change_name:" in c_msg:
                    old_name = self.client_name
                    self.client_name = c_msg.split(':')[2]
                    self.c_sock.send(f">>> Your name was successfully changed to: {self.client_name}".encode())
                    print(f'Client`s name: {old_name} was changed to: {self.client_name}: {c_msg}')

                else:
                    print(f'>>> {self.client_name}: {c_msg}')
                    # self.c_sock.send(f">>> {self.client_name}: {c_msg}".encode())
                    futures = []
                    with cf.ThreadPoolExecutor() as executor:

                        for c_thd in self.__class__.client_threads:
                            futures.append(executor.submit(c_thd.c_sock.send,
                                                           f">>> {self.client_name}: {c_msg}".encode()))

                        for _ in cf.as_completed(futures):
                            pass

        finally:
            self.c_sock.close()


if __name__ == "__main__":
    soc = socket(AF_INET, SOCK_STREAM)
    try:
        soc.bind(('localhost', 4000))
        soc.listen(3)
        print(">>> Server started <<<")

        while True:

            c_sock, c_addr = soc.accept()
            print("> New connection <")

            thr = ClientTread(c_sock, *c_addr)
            thr.start()

    finally:
        soc.close()
