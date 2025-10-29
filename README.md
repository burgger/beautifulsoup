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
