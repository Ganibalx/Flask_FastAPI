import random
import threading
import time

start_time = time.time()
thread_count = 4
arr_length = 1000000
arr = []
threads = []


def fillinarr(count):
    global arr
    for i in range(0, count):
        arr.append(random.randint(1, 100))


for p in range(0, thread_count):
    if p < thread_count-1:
        count = int(arr_length/thread_count)
        arr_length -= count
    else:
        count = arr_length
    thread = threading.Thread(target=fillinarr, args=[count])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(sum(arr))
print(f'{time.time()-start_time}')

