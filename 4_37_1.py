import asyncio


dict_ = {'fibo': [], 'fact': [], 'square': [], 'cube': []}



async def fibo_nums(list_):
    num = list_[-1]
    first_ = 0
    next_ = 1
    global dict_
    for _ in range(num):
        await asyncio.sleep(1/100)
        first_, next_ = next_, next_ + first_
        dict_['fibo'].append(first_)
        print(f"fibonacci {first_}")


async def factorial(list_):

    global dict_
    for num in list_:
        factor = 1
        for i in range(1, num+1):
            await asyncio.sleep(1/100)
            factor *= i
        dict_['fact'].append(factor)
        print(f"factorial {factor}")


async def square(list_):
    global dict_
    for i in list_:
        await asyncio.sleep(1/100)
        dict_['square'].append(i ** 2)


async def cube(list_):
    global dict_
    for i in list_:
        await asyncio.sleep(1 / 100)
        dict_['cube'].append(i ** 3)


list_num = list(range(1, 11))


async def main():
    await asyncio.gather(*[
        factorial(list_num),
        fibo_nums(list_num),
        square(list_num),
        cube(list_num)
    ])


loop = asyncio.get_event_loop()
res = loop.run_until_complete(main())
print(dict_)
