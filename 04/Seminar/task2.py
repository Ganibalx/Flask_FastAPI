# Написать программу, которая считывает список из 10 URL-адресов
# и одновременно загружает данные с каждого адреса. После загрузки
# данных нужно записать их в отдельные файлы. Используйте процессы.

import requests
import multiprocessing


urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://mail.ru/'
        ]


def download(url):
    response = requests.get(url)
    filename = 'process_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(f'files/{filename}', "w", encoding='utf-8') as f:
        f.write(response.text)


mult = []
for url in urls:
    thread = multiprocessing.Process(target=download, args=(url,))
    mult.append(thread)
    thread.start()

for thread in mult:
    thread.join()
