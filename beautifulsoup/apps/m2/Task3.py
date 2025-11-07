# use SoupStrainer refactor M1/T3: print all tags
import sys
import time
from bs4 import BeautifulSoup, SoupStrainer


def find_tags_print(input_path):
    start_time = time.time()
    with open(input_path, "rb") as f:
        content = f.read()
    tags = SoupStrainer(True)
    soup = BeautifulSoup(content, "xml", parse_only=tags)
    # soup = BeautifulSoup(content, "xml")
    prettify_time = time.time() - start_time
    all_tags = soup.find_all(True)
    for tags in all_tags:
        print(tags)
    end_time = time.time()
    final_time = end_time - start_time
    print("-" * 40)
    print(f'prettify time use={prettify_time * 1000:.2f}ms')
    print(f'final time use={final_time * 1000:.2f}ms')
    print("-" * 40)


if __name__ == "__main__":
    input_file = sys.argv[1]
    find_tags_print(input_file)
