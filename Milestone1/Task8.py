# insert a new label before a certain <>
import os
import sys
import time
import psutil
from bs4 import BeautifulSoup


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)


def find_tags_with_id_print(input_path):
    base_mem_use = get_memory_usage()
    output_path = f"{input_path}_add_before"
    start_time = time.time()
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
    soup = BeautifulSoup(content, "xml")
    mem_use = get_memory_usage()
    prettify_time = time.time() - start_time
    # insert new tag
    new_tag = soup.new_tag("span", id="inserted-by-task8")
    new_tag.string = "this is a string"
    tag = soup.find('p')
    print(f'new tag will be insert before {tag}')
    tag.insert_before(new_tag)
    print(f'{new_tag} has been inserted before first <p> tag')
    add_attr_file = soup.prettify()
    with open(output_path, 'w') as f:
        f.write(add_attr_file)
    end_time = time.time()
    final_time = end_time - start_time
    print("-" * 40)
    print(f'prettify time={prettify_time * 1000:.4f}ms')
    print(f'baseline mem usage={base_mem_use:.4f}MB')
    print(f'final mem usage={mem_use:.4f}MB')
    print(f'final time use={final_time * 1000:.2f}ms')
    print("-" * 40)


if __name__ == "__main__":
    input_file = sys.argv[1]
    find_tags_with_id_print(input_file)
