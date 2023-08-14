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
            self._next = next

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


class LinkedDeque(_DoublyLinkedBase):
    """Double end queue implementation based on a doubly linked list"""

    def first(self):
        """Return the front element of the deque (but not remove it)"""
        if self.is_empty():
            raise Empty('The deque is empty !!!')
        else:
            return self._header.next.element

    def last(self):
        """Return the back element of the deque (but not remove it)"""
        if self.is_empty():
            raise Empty('The deque is empty !!!')
        else:
            return self._trailer.prev.element

    def insert_first(self, e):
        """Add an element to the front of the queue"""
        self._insert_between(e, self._header, self._header.next)

    def insert_last(self, e):
        """Add an element to the back of the queue"""
        self._insert_between(e, self._trailer.prev, self._trailer)

    def remove_first(self):
        """Remove the first element in deque, return its value, raise Empty Exception if the deque is empty"""
        if self.is_empty():
            raise Empty('The deque is empty')
        else:
            answer = self._delete_node(self._header.next)
            return answer

    def remove_last(self):
        """Remove the last element in deque, return its value, raise Empty Exception if the deque is empty"""
        if self.is_empty():
            raise Empty('The deque is empty')
        else:
            answer = self._delete_node(self._trailer.prev)
            return answer


