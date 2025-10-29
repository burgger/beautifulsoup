from .. import BeautifulSoup
from ..SoupReplacer import SoupReplacer

HTML1 = """
<head>
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
 </head>
 """

HTML2 = """<a class="vector-toc-link" href="#Government_and_politics">
			<div class="vector-toc-text">
				<span class="vector-toc-numb">4</span>
				<span>Government and politics</span>
			</div>
		</a>
		
			<button aria-controls="toc-Government_and_politics-sublist" class="cdx-button cdx-button--weight-quiet cdx-button--icon-only vector-toc-toggle">
				<span class="vector-icon mw-ui-icon-wikimedia-expand"></span>
				<span>Toggle Government and politics subsection</span>
			</button>
		
		<ul id="toc-Government_and_politics-sublist" class="vector-toc-list">
			<li id="toc-National_government"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#National_government">
				<div class="vector-toc-text">
					<span class="vector-toc-numb">4.1</span>
					<span>National government</span>
				</div>
			</a>
			
			<ul id="toc-National_government-sublist" class="vector-toc-list">
			</ul>
		</li>
		<li id="toc-Subdivisions"
			class="vector-toc-list-item vector-toc-level-2">
			<a class="vector-toc-link" href="#Subdivisions">
				<div class="vector-toc-text">
					<span class="vector-toc-numb">4.2</span>
					<span>Subdivisions</span>
				</div>
			</a>
			
			<ul id="toc-Subdivisions-sublist" class="vector-toc-list">
			</ul>
		</li>
		"""


class TestSoupReplacer1:
    def test_basic(self):
        rep = SoupReplacer(og_tag="meta", alt_tag="haha")
        soup = BeautifulSoup(HTML1, "lxml-xml", replacer=rep)
        print(soup)

class TestSoupReplacer2:
    def test_another(self):
        rep = SoupReplacer("div", "cia")
        soup = BeautifulSoup(HTML2, "html.parser", replacer=rep)
        print(soup)

