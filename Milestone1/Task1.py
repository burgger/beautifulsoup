# prettify and save
import os
import sys
import time

import psutil
from bs4 import BeautifulSoup


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)


def read_and_prettify(input_path):
    output_path = f"{input_path}_prettified"
    base_mem_use = get_memory_usage()
    start_time = time.time()
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
    soup = BeautifulSoup(content, "xml")
    mem_use = get_memory_usage()
    end_time = time.time()
    prettify_time = end_time - start_time
    prettified = soup.prettify()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(prettified)
    print("-" * 40)
    print(f"output file={output_path}")
    print(f'prettify time={prettify_time * 1000:.4f}ms')
    print(f'baseline mem usage={base_mem_use:.4f}MB')
    print(f'final mem usage={mem_use:.4f}MB')
    print("-" * 40)


if __name__ == "__main__":
    input_file = sys.argv[1]
    read_and_prettify(input_file)
