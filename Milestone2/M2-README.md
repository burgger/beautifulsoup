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
```python Milestone2/Task6.py [input path] [output path]```

