import os
import sys
import time
import psutil
from bs4 import BeautifulSoup, SoupStrainer


def find_tags_with_id_print(input_path):
    start_time = time.time()
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
    data = SoupStrainer(attrs={'id': True})
    soup= BeautifulSoup(content,'xml',parse_only=data)
    # soup = BeautifulSoup(content, "xml")
    prettify_time = time.time() - start_time
    tags_with_id = soup.find_all()
    for tags in tags_with_id:
        print(tags)
    end_time = time.time()
    final_time = end_time - start_time
    print("-" * 40)
    print(f'prettify time={prettify_time * 1000:.2f}ms')
    print(f'final time use={final_time * 1000:.2f}ms')
    print("-" * 40)


if __name__ == "__main__":
    input_file = sys.argv[1]
    find_tags_with_id_print(input_file)
