from collections.abc import MutableMapping


class MapBase(MutableMapping):
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key


class UnsortedTableMap(MapBase):
    """Map implementation using an unsorted list"""
    def __init__(self):
        """Initialize an empty map"""
        self._map = []

    def __getitem__(self, k):
        """Return value associated with key k, raise KeyError if not found"""
        for item in self._map:
            if k == item._key:
                return item._value
        raise KeyError('Key Error:' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwrite existing value if present"""
        for item in self._map:
            if k == item._key:
                item._value = v
                return
        # did not find match for key
        self._map.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k, raise KeyError if not found"""
        for j in range(len(self._map)):
            if k == self._map[j]._key:
                self._map.pop(j)
                return
        # did not find the key
        raise KeyError('Key Error:', repr(k))

    def __iter__(self):
        """Generate iteration of map's key"""
        for item in self._map:
            yield item._key

