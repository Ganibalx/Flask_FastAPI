# Cоздать программу, которая будет производить подсчет количества
# слов в каждом файле в указанной директории и выводить результаты
# в консоль. Используйте асинхронность.

import asyncio
import pathlib


async def wordcount(file, dir):
    with open(f'{dir}/{file.name}', "r", encoding='utf-8') as f:
        file_read = f.read()
    print(len(file_read.split()))


async def main():
    threads = []
    path = pathlib.Path(f'{pathlib.Path().cwd()}/files')
    for file in path.iterdir():
        threads.append(asyncio.create_task(wordcount(file, path)))
    await asyncio.gather(*threads)


asyncio.run(main())
