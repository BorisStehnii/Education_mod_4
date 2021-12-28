import multiprocessing as mp
import time
import concurrent.futures as cf
import threading
from sympy import isprime


def primality_number(n):
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def dict_prim_number(dict_, n):
    # dict_[n] = primality_number(n)
    dict_[n] = isprime(n)


if __name__ == "__main__":

    # NUMBERS = [2, 4, 5, 7, 9]
    NUMBERS = [
        2,  # prime
        1099726899285419,
        1570341764013157,  # prime
        1637027521802551,  # prime
        1880450821379411,  # prime
        1893530391196711,  # prime
        2447109360961063,  # prime
        3,  # prime
        2772290760589219,  # prime
        3033700317376073,  # prime
        4350190374376723,
        4350190491008389,  # prime
        4350190491008390,
        4350222956688319,
        2447120421950803,
        5,  # prime
    ]

    manager = mp.Manager()
    dict_1 = manager.dict()
    start_time = time.time()
    with mp.Pool() as pool:
        for num in NUMBERS:
            pool.apply(dict_prim_number, args=(dict_1, num))
    print(time.time() - start_time)
    print(dict_1)


    start_time = time.time()
    dict_2 = dict()
    with cf.ThreadPoolExecutor(max_workers=4) as thread_pool:
        # Нужен ли лок???
        futures = []
        for num in NUMBERS:
            futures.append(thread_pool.submit(dict_prim_number, dict_=dict_2, n=num))

        for future in cf.as_completed(futures):
            pass
            # future.result()

    # thread_pool.shutdown()
    print(time.time() - start_time)
    print(dict_2)

