import pytest
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString, Comment,Doctype

HTML_SIMPLE = "<html><body><p>hi <b>there</b></p></body></html>"
HTML_MIXED = "<div>hello<!--c--><p>world <span>!</span></p></div>"


def test_soup_iter_single_tag():
    """
    only one Tag
    """
    soup = BeautifulSoup("<p></p>", 'html.parser')
    nodes = list(soup)

    assert len(nodes) == 1
    assert isinstance(nodes[0], Tag)
    assert nodes[0].name == "p"


def test_soup_iter_includes_text_and_comment():
    """
    Text, and comment should also be iterated
    """
    soup = BeautifulSoup(HTML_MIXED, 'html.parser')
    nodes = list(soup)

    has_tag = any(isinstance(n, Tag) for n in nodes)
    has_text = any(isinstance(n, NavigableString) and not isinstance(n, Comment)
                   for n in nodes)
    has_comment = any(isinstance(n, Comment) for n in nodes)

    assert has_tag
    assert has_text
    assert has_comment


def test_soup_iter_empty_document():
    soup = BeautifulSoup("", 'html.parser')
    assert list(soup) == []


def _manual_dfs(root):
    for child in root.contents:
        yield child
        if isinstance(child, Tag):
            for node in _manual_dfs(child):
                yield node

def test_soup_iter_matches_manual_dfs():
    """
    iter should equivalent to dfs
    """
    soup = BeautifulSoup(HTML_SIMPLE, 'html.parser')
    iter_nodes = list(soup)
    manual_nodes = list(_manual_dfs(soup))

    assert iter_nodes == manual_nodes

def test_soup_iter_with_doctype_and_top_level_comment():
    """
    doctype and comment
    """
    html = """<!DOCTYPE html>
    <!-- top comment -->
    <html><body><p>hello</p></body></html>
    """
    soup = BeautifulSoup(html, 'html.parser')
    nodes = list(soup)

    has_doctype = any(isinstance(n, Doctype) for n in nodes)
    has_comment = any(isinstance(n, Comment) for n in nodes)
    has_p = any(isinstance(n, Tag) and n.name == "p" for n in nodes)

    assert has_doctype
    assert has_comment
    assert has_p