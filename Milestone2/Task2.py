# use SoupStrainer refactor M1/T2: print all <a>
import sys
import time
from bs4 import BeautifulSoup, SoupStrainer


def prettify_print_with_strainer(input_path):
    start_time = time.time()
    # new strainer
    strainer = SoupStrainer("a")
    with open(input_path, "rb") as f:
        content = f.read()
    # constraint
    soup = BeautifulSoup(content, "xml", parse_only=strainer)
    end_time = time.time()
    prettify_time = end_time - start_time
    hyperlinks = soup.find_all('a')
    for i, link in enumerate(hyperlinks):
        href = link.get('href', 'No Href')
        text = link.get_text(strip=True)
        print(f"{i + 1}. Href: {href}, Text: {text}")
    print("-" * 40)
    print(f'prettify time={prettify_time * 1000:.4f}ms')
    print("-" * 40)


if __name__ == "__main__":
    input_file = sys.argv[1]
    prettify_print_with_strainer(input_file)
