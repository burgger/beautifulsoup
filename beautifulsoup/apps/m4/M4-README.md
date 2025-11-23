# Milestone-4
implement a ```___iter___``` in ```__init__.py``` for BeautifulSoup.

Soup is a Tag, we use descendants to implement iter
```python
    def descendants(self) -> Iterator[PageElement]:
        """Iterate over all children of this `Tag` in a
        breadth-first sequence.
        """
        if not len(self.contents):
            return
        # _last_descendant() can't return None here because
        # accept_self is True. Worst case, last_descendant will end up
        # as self.
        last_descendant = cast(PageElement, self._last_descendant(accept_self=True))
        stopNode = last_descendant.next_element
        current: _AtMostOneElement = self.contents[0]
        while current is not stopNode and current is not None:
            successor = current.next_element
            yield current
            current = successor
```
implement in line 516 ```__init__.py```