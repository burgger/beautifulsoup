# Test1 for Replacer
import pytest
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer


def test1():
    html = """<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <title>
   bs4 — Beautiful Soup 4.13.0 documentation
  </title>
  <link href="../_static/pygments.css?v=d1102ebc" rel="stylesheet" type="text/css"/>
  <link href="../_static/alabaster.css?v=12dfc556" rel="stylesheet" type="text/css"/>
  <script src="../_static/documentation_options.js?v=ccf1db52"/>
  <script src="../_static/doctools.js?v=888ff710"/>
  <script src="../_static/sphinx_highlight.js?v=dc90522c"/>
  <link href="../genindex.html" rel="index" title="Index"/>
  <link href="../search.html" rel="search" title="Search"/>
  <link href="../_static/custom.css" rel="stylesheet" type="text/css"/>
 </head>"""
    soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("meta", "maga"))
    assert soup.find("meta") is None
    assert soup.find("maga") is not None
