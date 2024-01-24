from multiprocessing import Process, Value, Array

def f(a):
    for i in range(len(a)):
        a[i] = i


arr = Array('i', range(10))

p = Process(target=f, args=(arr,))
p.start()
p.join()

print(*arr)