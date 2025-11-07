import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "beautifulsoup")))
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

def main():
    in_path, out_path = sys.argv[1], sys.argv[2]
    og = sys.argv[3] if len(sys.argv) > 3 else "b"
    alt = sys.argv[4] if len(sys.argv) > 4 else "blockquote"

    with open(in_path, "rb") as f:
        data = f.read()

    replacer = SoupReplacer(og, alt)
    soup = BeautifulSoup(data, "html.parser", replacer=replacer)
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(soup.prettify())


if __name__ == "__main__":
    main()
