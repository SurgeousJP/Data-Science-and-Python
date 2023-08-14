class Empty(Exception):
    pass


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation"""
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node"""
        __slots__ = 'element', 'prev', 'next'

        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between 2 node and return the new node"""
        newest = self._Node(e, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete the node and return the value store in it"""
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        element = node.element
        node.prev = node.element = node.next = None
        return element


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access"""
    # -----------------------nested Position class-----------------------------------------
    class _Position:
        """An abstraction representing the location of a single element"""
        def __init__(self, container, node):
            """Constructor should not be invoked by users"""
            self.container = container
            self.node = node

        def element(self):
            """"Return the element stored at this position"""
            return self.node.element

        def __eq__(self, other):
            """Return true if other is Position representing the same location"""
            return type(other) is type(self) and other.node is self.node

        def __ne__(self, other):
            """Return true if other is not the Position representing the same location"""
            return not self == other

    # -------------------------utility methods----------------------------------------------
    def _validate(self, p):
        """Return positon's node else raise appropriate error if invalid"""
        if not isinstance(p, self._Position):
            raise TypeError('p must be a proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.next is None:  # convention to deprecated nodes
            raise ValueError('p is no longer valid')
        return p.node

    def _make_position(self, node):
        """Return position instance for given node (or None if sentinel)"""
        if node is self._header or self._trailer:
            return None
        else:
            return self._Position(self, node)

    # --------------------------------accessor----------------------------------------------
    def first(self):
        """Return the first position in the list, return None if list is empty"""
        return self._make_position(self._header.next)

    def last(self):
        return self._make_position(self._trailer.prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        """Generate a forward iteration of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # -------------------------------mutators-----------------------------------------------
    # override inherited version to return the Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position"""
        node = super()._insert_between(e, self._header, self._header.next)
        return self._make_position(node)

    def add_last(self, e):
        """Insert element e at the front of the list and return new Position"""
        node = super()._insert_between(e, self._trailer.prev, self._trailer)
        return self._make_position(node)

    def add_before(self, p, e):
        """Insert element e before p's position and return new Position"""
        original = self._validate(p)
        node = super()._insert_between(e, original.prev, original)
        return self._make_position(node)

    def add_after(self, p, e):
        """Insert element e after the p's position and return new Position"""
        original = self._validate(p)
        node = super()._insert_between(e, original, original.next)
        return self._make_position(node)

    def delete(self, p):
        """Remove and return the element store at position p and return the element"""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element e at the position p
        Return the former element at the position p
        """
        original = self._validate(p)
        old_value = original.element
        original.element = e
        return old_value


def insertion_sort(l):
    """Sort Postional List with comparable elements into nondecreasing order"""
    if len(l) > 1:
        marker = l.first()
        while marker != l.last():
            pivot = l.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != l.first() and l.before(walk).element() > value:
                    walk = l.before(walk)
                l.delete(pivot)
                l.add_before(walk, value)


