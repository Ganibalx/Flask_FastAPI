import random
from multiprocessing import Process, Array
import time

start_time = time.time()
thread_count = 2
arr_length = 1000000


def fillinarr(start, stop, arr):
    for i in range(start, stop+1):
        arr[i] = random.randint(1, 100)


threads = []
arr = Array('i', range(arr_length))
interval = int(arr_length/thread_count)
flag = 0

for p in range(0, thread_count):
    if (arr_length - flag) < (interval * 2):
        start = flag+1
        stop = arr_length-1
    else:
        start = flag
        stop = start + interval-1
        flag += stop
    thread = Process(target=fillinarr, args=(start, stop, arr))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print(sum(arr))
print(f'{time.time()-start_time}')

