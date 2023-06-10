import asyncio



# программа с конкуренцией внутри одной функции
'''
async def send_time(sec):
    while True:
        await asyncio.sleep(sec)
        print (f'прошло {sec} секунд')

async def main():
    task1 = asyncio.create_task(send_time(2))
    task2 = asyncio.create_task(send_time(5))

    await task1
    await task2

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Остановка программы')'''

# отсчитывает количество секунд
'''
async def f1():
    n = 0
    while True:
        await asyncio.sleep(1)
        n += 1
        print(f'прошло {n} секунд')

async def f2():
    while True:
        await asyncio.sleep(3)
        print(f'прошло ещё 3 секунд')


async def main():
    task1 = asyncio.create_task(f1())
    task2 = asyncio.create_task(f2())

    await task1
    await task2

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Остановка программы')
'''