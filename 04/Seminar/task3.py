# Написать программу, которая считывает список из 10 URL-адресов
# и одновременно загружает данные с каждого адреса. После загрузки
# данных нужно записать их в отдельные файлы. Используйте асинхронную библиотеку.

import asyncio
import aiohttp


urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://mail.ru/'
        ]


async def download(url):
    async with aiohttp.ClientSession() as aiohttp_session:
        async with aiohttp_session.get(url) as async_with:
            filename = 'asyncio_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(f'files/{filename}', "w", encoding='utf-8') as f:
                f.write(await async_with.text())


async def main():
    task = []
    for url in urls:
        task.append(asyncio.create_task(download(url)))
    await asyncio.gather(*task)


asyncio.run(main())