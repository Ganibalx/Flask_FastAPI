# Cоздать программу, которая будет производить подсчет количества
# слов в каждом файле в указанной директории и выводить результаты
# в консоль. Используйте процессы.

import multiprocessing
import pathlib

def wordcount(file, dir):
    with open(f'{dir}/{file.name}', "r", encoding='utf-8') as f:
        file_read = f.read()
    print(len(file_read.split()))


threads = []
path = pathlib.Path(f'{pathlib.Path().cwd()}/files')
for file in path.iterdir():
    thread = multiprocessing.Process(target=wordcount, args=(file, path))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
