import asyncio
from pprint import pprint


async def fibo_nums(list_, dict_):
    for num in list_:
        first_ = 0
        next_ = 1

        for _ in range(num):
            await asyncio.sleep(1 / 10000)
            first_, next_ = next_, next_ + first_

        dict_['fibo'].append(first_)
        # print(f"fibonacci {first_}")


async def factorial(list_, dict_):

    for num in list_:
        factor = 1
        for i in range(1, num+1):
            await asyncio.sleep(1 / 10000)
            factor *= i
        dict_['fact'].append(factor)
        # print(f"factorial {factor}")


async def square(list_, dict_):

    for i in list_:
        await asyncio.sleep(1 / 10000)
        dict_['square'].append(i ** 2)
        # print(f"square {i ** 2}")


async def cube(list_, dict_):

    for i in list_:
        await asyncio.sleep(1 / 10000)
        dict_['cube'].append(i ** 3)
        # print(f"cube {i ** 3}")


async def main(list_num_, dict_num):
    await asyncio.gather(*[
        factorial(list_num_, dict_num),
        fibo_nums(list_num_, dict_num),
        square(list_num_, dict_num),
        cube(list_num_, dict_num)
    ])

if __name__ == "__main__":
    dict_new = {'fibo': [], 'fact': [], 'square': [], 'cube': []}
    list_num = list(range(1, 11))
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(main(list_num, dict_new))
    pprint(dict_new)
