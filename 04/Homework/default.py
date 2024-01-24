import time
import random


arr_length = 1000000
start_time = time.time()
arr = []
for i in range(0, arr_length):
    arr.append(random.randint(1, 100))

print(sum(arr))
print(f'{time.time()-start_time}')
