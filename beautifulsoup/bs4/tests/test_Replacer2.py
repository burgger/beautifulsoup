import pytest
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer


def test2():
    html = """<meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>bs4 &#8212; Beautiful Soup 4.13.0 documentation</title>
    <link rel="stylesheet" type="text/css" href="../_static/pygments.css?v=d1102ebc" />
    <link rel="stylesheet" type="text/css" href="../_static/alabaster.css?v=12dfc556" />
    <script src="../_static/documentation_options.js?v=ccf1db52"></script>
    <script src="../_static/doctools.js?v=888ff710"></script>
    <script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />"""
    soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("title", "t"))
    assert len(soup.find_all("t")) ==1
