import os
import sys
import time
import psutil
from bs4 import BeautifulSoup


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)


def modifiy_tags(input_path):
    output_path = f"{input_path}_modified"
    base_mem_use = get_memory_usage()
    start_time = time.time()
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
    soup = BeautifulSoup(content, "xml")
    mem_use = get_memory_usage()
    prettify_time = time.time() - start_time
    old_tag_name = 'b'
    new_tag_name = 'blockquote'
    tags_need_rename = soup.find_all(old_tag_name)
    if not tags_need_rename:
        print(f'no <{old_tag_name}> in the file')
    else:
        for tag in tags_need_rename:
            print(f'{tag} has been modified')
            tag.name = new_tag_name

    modified_file = soup.prettify()
    with open(output_path, 'w') as f:
        f.write(modified_file)
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
    modifiy_tags(input_file)
