# Milestone-4
implement a ```___iter___``` in ```__init__.py``` for BeautifulSoup.

Soup is a Tag,Tag(name,attrs,contents)  #contents is a list stores child nodes,
child could be Tag node, Text Node, Comment Node, Document node.

Tag is a PageElement, pointer in PageElement:
```
self.parent              # Tag or soup
self.contents            # only tag have
self.next_sibling        # next sibling of same parent
self.previous_sibling    # previous sibling
self.next_element        # next element of this tree
self.previous_element    # previous_element of this tree
```

For this html
``` html
<div>
  hello <b>world</b>!
</div>
```
The structure will be:
```
Tag
    L___ NavigableString("hello ")
    L___ Tag(b)
        L___NavigableString("world")
    L___ NavigableString("!")

```

Tag has a default iterator to iterate the children, but we want soup iterator to iter 
all nodes and all children of a node--> next_element

implement a ```___iter___``` in ```__init__.py``` for BeautifulSoup(Tag).