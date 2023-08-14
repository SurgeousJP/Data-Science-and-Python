class Empty(Exception):
    pass


class CircularQueue:
    """Queue implementation using circularly linked list as storage"""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        """Initializing an empty circular queue"""
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return the first value in the queue, raise Empty Exception if queue is empty"""
        if self.is_empty():
            raise Empty('Queue is empty !!!')
        else:
            return self._tail.next.element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty !!!')
        oldhead = self._tail.next
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = oldhead.next
        self._size -= 1
        return oldhead.element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest.next = newest
        else:
            newest.next = self._tail.next
            self._tail.next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotate the head to the back of the queue"""
        if self._size > 0:
            self._tail = self._tail.next


if __name__ == '__main__':
    circular_queue = CircularQueue()
    for i in range(11):
        circular_queue.enqueue(i)
    for i in range(11):
        print(circular_queue.first(), end=' ')
        circular_queue.rotate()
    print()
    for i in range(11):
        print(circular_queue.first(), end=' ')
        circular_queue.rotate()
