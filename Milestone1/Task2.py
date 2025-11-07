import os
import sys
import time

import psutil
from bs4 import BeautifulSoup


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)


def prettify_print(input_path):
    base_mem_use = get_memory_usage()
    start_time = time.time()
    with open(input_path, "rb") as f:
        content = f.read()
    soup = BeautifulSoup(content, "xml")
    mem_use = get_memory_usage()
    end_time = time.time()
    prettify_time = end_time - start_time
    hyperlinks = soup.find_all('a')
    for i, link in enumerate(hyperlinks):
        href = link.get('href', 'No Href')
        text = link.get_text(strip=True)
        print(f"{i + 1}. Href: {href}, Text: {text}")
    print("-" * 40)
    print(f'prettify time={prettify_time * 1000:.4f}ms')
    print(f'baseline mem usage={base_mem_use:.4f}MB')
    print(f'final mem usage={mem_use:.4f}MB')
    print("-" * 40)


if __name__ == "__main__":
    input_file = sys.argv[1]
    prettify_print(input_file)
