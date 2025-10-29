# Milestone1

---

## Task1
```pip install beautifulsoup4```

```pip install psutil``` to monitor the resources usage

```pip install lxml``` to process xml/html better

cd into ```Milestone1``` and run in the terminal with ```python Task1.py [path of the xml/html]```

Performance on running 3.19GB xml:
```
(.venv) bohuang@Bos-MacBook-Air PythonProject % python Milestone1/Task1.py Milestone1/HTMLfiles/giga_wikidatawiki.xml
--------------------
output file=Milestone1/HTMLfiles/giga_wikidatawiki.xml_prettified
prettify time=367746.5091ms
baseline mem usage=20.0781MB
final mem usage=3052.4062MB
--------------------
```
However, the final mem usage is not precise when handling large files, when the ```mem_use = get_memory_usage()```
has been called, python already start the memory recycle. By checking the system monitor,
python takes up to 30GB on running prettify. We can use ```memory_profiler``` to get the accuracy
highest memory use. But it creates more files and need to run other commands to check the details. So we won't use that.

## Task2
run ```python Task2.py [path to the html/xml file]```

## Task3
run ```python Task3.py [path to the html/xml file]```

## Task4
run ```python Task4.py [path to the html/xml file]```


performance on 3.19GB xml:
```
prettify time=366403.8250ms
baseline mem usage=20.0625MB
final mem usage=2592.6406MB
final time use=373086.01ms
```
Like task1 the memory use is not precise, the python process takes up more than 30GB RAM when running.

## Task5 
find the parent of ```div id="simpleSearch"``` in
and print the parent tree
```html
<span>Search</span>
	</a>
	<div class="vector-typeahead-search-container">
		<div class="cdx-typeahead-search cdx-typeahead-search--show-thumbnail cdx-typeahead-search--auto-expand-width">
			<form action="/w/index.php" id="searchform" class="cdx-search-input cdx-search-input--has-end-button">
				<div id="simpleSearch" class="cdx-search-input__input-wrapper"  data-search-loc="header-moved">
					<div class="cdx-text-input cdx-text-input--has-start-icon">
						<input
							class="cdx-text-input__input mw-searchInput" autocomplete="off"
							 type="search" name="search" placeholder="Search Wikipedia" aria-label="Search Wikipedia" autocapitalize="sentences" spellcheck="false" title="Search Wikipedia [f]" accesskey="f" id="searchInput"
							>
						<span class="cdx-text-input__icon cdx-text-input__start-icon"></span>
					</div>
					<input type="hidden" name="title" value="Special:Search">
				</div>
				<button class="cdx-button cdx-search-input__end-button">Search</button>
			</form>
		</div>
	</div>
</div>
```
result:
```
(.venv) bohuang@Bos-MacBook-Air PythonProject % python Milestone1/Task5.py Milestone1/HTMLfiles/big_US.html
<form action="/w/index.php" class="cdx-search-input cdx-search-input--has-end-button" id="searchform">
<div class="cdx-search-input__input-wrapper" data-search-loc="header-moved" id="simpleSearch">
<div class="cdx-text-input cdx-text-input--has-start-icon">
<input accesskey="f" aria-label="Search Wikipedia" autocapitalize="sentences" autocomplete="off" class="cdx-text-input__input mw-searchInput" id="searchInput" name="search" placeholder="Search Wikipedia" spellcheck="false" title="Search Wikipedia [f]" type="search">
<span class="cdx-text-input__icon cdx-text-input__start-icon"/>
</input>
<input name="title" type="hidden" value="Special:Search">
</input>
<button class="cdx-button cdx-search-input__end-button">Search</button>
</div>
</div>
</form>
----------------------------------------
prettify time=199.8580ms
baseline mem usage=20.1406MB
final mem usage=56.5938MB
final time use=200.16ms
----------------------------------------
```

## Task6
run ```python Task6.py [path to the html/xml file]```

It will print the tags which has been modified and generate a new file name's [original file]_modified

## Task7
run ```python Task7.py [path to the html/xml file]```
It will print the tags which has been modified and generate a new file name's [original file]_add_test

## Task8
run ```python Task8.py [path to the html/xml file]```

It will add an 
```html
<span id="inserted-by-task8">
                                              this is a string
                                             </span>
```
before the first <p>

Performance on 4MB html file
```
new tag will be insert before <p class="mw-empty-elt">
</p>
<span id="inserted-by-task8">this is a string</span> has been inserted before first <p> tag
----------------------------------------
prettify time=199.2400ms
baseline mem usage=20.1562MB
final mem usage=56.6875MB
final time use=339.57ms
----------------------------------------
```

# Milestone2 

---
## Part I
In this part, we use SoupStrainer to refactor codes in Milestone1, to simplify the test
we only use the 343MB HTML file for test.
### Task2
```commandline
python Milestone2/Task2.py [path to the html/xml file] 
```
In Task2 we add a SoupStrainer When working on a more than 300MB html
Milestone1 Task2 cost 131s and Milestone2 Task2 cost only 32s. **About 4times quicker** See in the Commandline output

```commandline
(.venv) bohuang@Bos-MacBook-Air Milestone % python Milestone2/Task2.py HTMLfiles/huge_wikidatawiki.xml
----------------------------------------
prettify time=32108.8481ms
----------------------------------------
(.venv) bohuang@Bos-MacBook-Air Milestone % python Milestone1/Task2.py HTMLfiles/huge_wikidatawiki.xml
----------------------------------------
prettify time=131835.1839ms
baseline mem usage=20.0625MB
final mem usage=1454.7812MB
```

### Task3
run```python Milestone2/Task3.py HTMLfiles/huge_wikidatawiki.xml```
In Milestone2/task3 comparing with Milestone1/task3, because all tags have been parsed,SoupStrainer
only ignored the pure text in the html file. So the refactor doesn't show it's much higher performance.

Milestone1 takes 137s and Milestone2 takes 110s.
```
Milestone1: without SoupStrainer
prettify time=137742.93ms
final time use=372288.91ms

Milestone2: with SoupStrainer
prettify time use=110675.41ms
final time use=333763.99ms
```


### Task4
run`python Milestone2/Task4.py HTMLfiles/huge_wikidatawiki.xml`

Performance compare to Milestone1
```
Milestone1
prettify time=125713.7599ms
final time use=149368.52ms

Milestone2
prettify time=38476.07ms
final time use=43310.53ms
```

## Part II
All func we used in Milestone1 and Milestone2:
1.  **BeautifulSoup()**
    * File Path:`beautifulsoup/bs4/__init__.py`
    * Lines: 133~1144
2. **prettify()**
    * File Path:`beautifulsoup/bs4/element.py`
    * Lines: 2601~2618
3. **find_all()**
    * File Path:`beautifulsoup/bs4/element.py`
    * Lines: 2715~2746
4. **find()**
    * File Path:`beautifulsoup/bs4/element.py`
    * Lines: 2684~2712
5.  **find_parent()**
    * File Path:`beautifulsoup/bs4/element.py`
    * Lines: 992~1019
6. **.name** elements of soup
    * File Path:`beautifulsoup/bs4/element.py`
    * Lines: 1817
7. **new_tag()**
    * File Path:`beautifulsoup/bs4/__init__.py`
    * Lines: 682~731
8. **insert_before()**
    * File Path:`beautifulsoup/bs4/__init__.py`
    * Lines: 772~779
9. **SoupStrainer()**
    * File Path:`beautifulsoup/bs4/filter.py`
    * Lines: 313~683

## Part III
