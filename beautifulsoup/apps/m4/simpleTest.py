import sys
import time
from bs4 import BeautifulSoup

html="""<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>bs4 &#8212; Beautiful Soup 4.13.0 documentation</title>
    <link rel="stylesheet" type="text/css" href="../_static/pygments.css?v=d1102ebc" />
    <link rel="stylesheet" type="text/css" href="../_static/alabaster.css?v=12dfc556" />
    <script src="../_static/documentation_options.js?v=ccf1db52"></script>
    <script src="../_static/doctools.js?v=888ff710"></script>
    <script src="../_static/sphinx_highlight.js?v=dc90522c"></script>
    <link rel="index" title="Index" href="../genindex.html" />
    <link rel="search" title="Search" href="../search.html" />
   
  <link rel="stylesheet" href="../_static/custom.css" type="text/css" />
  

  
  

  </head>
    </b>  <body>
  

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          

          <div class="body" role="main">
            
  <section id="bs4">
<h1>bs4<a class="headerlink" href="#bs4" title="Link to this heading">¶</a></h1>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="bs4.html">bs4 package</a><ul>
<li class="toctree-l2"><a class="reference internal" href="bs4.html#module-bs4">Module contents</a><ul>
<li class="toctree-l3"><a class="reference internal" href="bs4.html#bs4.AttributeResemblesVariableWarning"><code class="docutils literal notranslate"><span class="pre">AttributeResemblesVariableWarning</span></code></a><ul>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.AttributeResemblesVariableWarning.MESSAGE"><code class="docutils literal notranslate"><span class="pre">AttributeResemblesVariableWarning.MESSAGE</span></code></a></li>
</ul>
</li>
<li class="toctree-l3"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup</span></code></a><ul>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.ASCII_SPACES"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.ASCII_SPACES</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.DEFAULT_BUILDER_FEATURES"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.DEFAULT_BUILDER_FEATURES</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.ROOT_TAG_NAME"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.ROOT_TAG_NAME</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.contains_replacement_characters"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.contains_replacement_characters</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.copy_self"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.copy_self()</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.declared_html_encoding"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.declared_html_encoding</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.decode"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.decode()</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.insert_after"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.insert_after()</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.insert_before"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.insert_before()</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.is_xml"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.is_xml</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.new_string"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.new_string()</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.new_tag"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.new_tag()</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.original_encoding"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.original_encoding</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.reset"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.reset()</span></code></a></li>
<li class="toctree-l4"><a class="reference internal" href="bs4.html#bs4.BeautifulSoup.string_container"><code class="docutils literal notranslate"><span class="pre">BeautifulSoup.string_container()</span></code></a></li>
</ul>"""
soup = BeautifulSoup(html, 'html.parser')
for node in soup:
    print(node)