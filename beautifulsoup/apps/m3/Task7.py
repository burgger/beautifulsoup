import sys
import time
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer


# Find all the <p> tags and add (or replace) a class attribute class="test" then write the tree onto a file.
def add_attr(input_path):
    output_path = f"{input_path}_add_test"
    start_time = time.time()
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    def add_test(tag):
        if tag.name == "p":
            new_attrs = dict(tag.attrs)
            new_attrs["class"] = ["test"]
            return new_attrs
        return tag.attrs

    r = SoupReplacer(attrs_xformer=add_test)
    soup = BeautifulSoup(content, "html.parser", replacer=r)
    prettify_time = time.time() - start_time
    add_attr_file = soup.prettify()
    with open(output_path, 'w') as f:
        f.write(add_attr_file)
    end_time = time.time()
    final_time = end_time - start_time
    print("-" * 40)
    print(f'prettify time={prettify_time * 1000:.4f}ms')
    print(f'final time use={final_time * 1000:.2f}ms')
    print("-" * 40)


if __name__ == "__main__":
    input_file = sys.argv[1]
    add_attr(input_file)
