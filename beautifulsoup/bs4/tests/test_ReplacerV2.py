import pytest
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

HTML = """<meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>bs4 &#8212; Beautiful Soup 4.13.0 documentation</title>
    <link rel="stylesheet" type="text/css" href="../_static/pygments.css?v=d1102ebc" />
    <link rel="stylesheet" type="text/css" href="../_static/alabaster.css?v=12dfc556" />
    <script src="../_static/documentation_options.js?v=ccf1db52"></script>
    <script src="../_static/doctools.js?v=888ff710"></script>
    <script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />"""
parser = "html.parser"


def test1():
    soup = BeautifulSoup(HTML, parser, replacer=SoupReplacer("meta", "maga"))
    assert soup.find("meta") is None
    assert len(soup.find_all("maga")) == 3

def test2():
    r = SoupReplacer(name_xformer=lambda tag: "s" if tag.name == "script" else None)
    soup = BeautifulSoup(HTML, parser, replacer=r)
    assert soup.find("script") is None
    assert len(soup.find_all("s")) == 3

def test3():
    # all <link rel> -> ss
    def set_preload(tag):
        if tag.name == "link":
            new_attrs = dict(tag.attrs)
            new_attrs["rel"] = ["ss"]
            return new_attrs
        return tag.attrs

    r = SoupReplacer(attrs_xformer=set_preload)
    soup = BeautifulSoup(HTML, parser, replacer=r)
    links = soup.find_all("link")
    assert len(links) == 4
    for lk in links:
        rel = lk.get("rel")
        assert isinstance(rel, list) and rel == ["ss"]

def test4():
    # remove type of <link>
    def drop_type(tag):
        if tag.name == "link" and "type" in tag.attrs:
            del tag.attrs["type"]

    r = SoupReplacer(xformer=drop_type)
    soup = BeautifulSoup(HTML, parser, replacer=r)
    for lk in soup.find_all("link"):
        assert "type" not in lk.attrs

def test5():
    # attrs_xf return illegal
    html = "<p class='a'>x</p>"
    r = SoupReplacer(attrs_xformer=lambda tag: "NOT_A_MAPPING" if tag.name == "p" else tag.attrs)
    soup = BeautifulSoup(html, parser, replacer=r)
    p = soup.p
    assert p.get("class") == ["a"]

def test6():
    """
    （pair → name_xformer → attrs_xformer → xformer）：
      1) pair：       <meta> → <maga>
      2) name_xf：    <link> → <lnk>
      3) attrs_xf：    tag = <lnk> ->data-x="1"
      4) xformer：     tag = <lnk> ->role="asset"
    """
    replacer = SoupReplacer("meta", "maga")

    def name_xf(tag):
        return "lnk" if tag.name == "link" else None

    def attrs_xf(tag):
        if tag.name == "lnk":
            na = dict(tag.attrs)
            na["data-x"] = "1"
            return na
        return tag.attrs

    def xf(tag):
        if tag.name == "lnk":
            tag["role"] = "asset"

    replacer._name = name_xf
    replacer._attrs = attrs_xf
    replacer._xf = xf

    soup = BeautifulSoup(HTML, parser, replacer=replacer)
    assert soup.find("meta") is None and len(soup.find_all("maga")) == 3
    lnks = soup.find_all("lnk")
    assert len(lnks) == 4
    for t in lnks:
        assert t.get("data-x") == "1"
        assert t.get("role") == "asset"