class Empty(Exception):
    pass


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage"""
    class _Node:
        """Lightweight, nonpublic class for stroing a singly linked node"""
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty !!!")
        else:
            return self._head.element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail.next = newest
        self._tail = newest
        self._size += 1


if __name__ == '__main__':
    q = LinkedQueue()
    for i in range(11):
        q.enqueue(i)
        print(i, end=' ')
    print()
    while not q.is_empty():
        print(q.dequeue(), end=' ')
