from socket import *
import asyncio


async def client_soc_(client_sock, client_addr):
    while True:
        await asyncio.sleep(1/100000)
        c_msg = client_sock.recv(1000).decode()
        if c_msg == 'exit':
            break
        print(f"{client_addr}>>{c_msg}")
    client_sock.close()


async def create_coroutine():
    soc = socket(AF_INET, SOCK_STREAM)

    soc.bind(('localhost', 4000))
    soc.listen(1)

    while True:
        c_sock, c_add = soc.accept()
        # await asyncio.gather(*[client_soc_(*sock_add) for sock_add in soc.accept()])
        await client_soc_(c_sock, c_add)

asyncio.run(create_coroutine())

