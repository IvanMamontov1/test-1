class ArrayIterator:
    def __init__(self, items):
        self._items = items
        self._pos = 0

    def has_next(self) -> bool:
        return self._pos < len(self._items)

    def next(self):
        if not self.has_next():
            raise StopIteration("No more items")
        item = self._items[self._pos]
        self._pos += 1
        return item


class MyCollection:
    def __init__(self, items):
        self._items = items

    def iterator(self) -> ArrayIterator:
        return ArrayIterator(self._items)


if __name__ == "__main__":
    col = MyCollection([1, 2, 3, 4])
    it = col.iterator()
    while it.has_next():
        print(it.next())
