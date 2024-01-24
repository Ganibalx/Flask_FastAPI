import random
import asyncio
import time

start_time = time.time()


async def fillinarr(count, arr):
    for i in range(0, count):
        arr.append(random.randint(1, 100))


async def main():
    thread_count = 4
    arr_length = 1000000
    arr = []
    task = []
    for p in range(0, thread_count):
        if p < thread_count - 1:
            count = int(arr_length / thread_count)
            arr_length -= count
        else:
            count = arr_length
        task.append(asyncio.create_task(fillinarr(count, arr)))
        await asyncio.gather(*task)
    print(sum(arr))
    print(f'{time.time() - start_time}')


asyncio.run(main())



