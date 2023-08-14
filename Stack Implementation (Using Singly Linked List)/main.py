class Empty(Exception):
    pass


class LinkedStack:
    """LIFO Stack Implementation using a singly linked list for storage"""
    # --------------------------nested _Node class--------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        __slots__ = 'element', 'next'  # streamline memory usage

        def __init__(self, element, next):
            self.element = element
            self.next = next

    # ---------------------------stack methods-------------------------------
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head.element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        else:
            answer = self._head.element
            self._head = self._head.next
            self._size -= 1
            return answer


if __name__ == '__main__':
    s = LinkedStack()
    for i in range(10):
        s.push(i)
        print(i, end=' ')
    print()
    while not s.is_empty():
        print(s.pop(), end=' ')



