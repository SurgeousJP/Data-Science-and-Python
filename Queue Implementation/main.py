class Empty(Exception):
    pass


class ArrayQueue:
    """FIFO queue implementation using Python list as the underlying storage"""
    DEFAULT_CAPACITY = 10  # moderate the size for new queues

    def __init__(self):
        # initialize an empty queue
        self._queue = [0] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        # Return the number of elements in queue
        return self._size

    def get_maximum_size(self):
        return len(self._queue)

    def is_empty(self):
        # Return True if the queue is empty, return False otherwise
        return self._size == 0

    def first(self):
        """Return the first value in queue but not remove it
        , raise Empty Exception if the queue is empty"""
        if self.is_empty():
            raise Empty('The queue is empty !!!')
        else:
            return self._queue[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (FIFO)
        Raise Empty Exception if the queue is empty"""
        if self.is_empty():
            raise Empty('The queue is empty!!!')
        else:
            return_val = self._queue[self._front]
            self._queue[self._front] = None
            self._front = (self._front + 1) % len(self._queue)
            self._size -= 1
            if 0 < self._size < len(self._queue) // 4:
                self._resize(len(self._queue) // 2)
            return return_val

    def enqueue(self, data):
        """Add the data into the back of the queue"""
        if self._size == len(self._queue):
            self._resize(2 * len(self._queue))
        else:
            avail = (self._front + self._size) % len(self._queue)
            self._queue[avail] = data
            self._size += 1

    def _resize(self, cap):  # assuming the cap >= len(self._queue)
        old = self._queue  # keeps track of the existing list
        self._queue = [None] * cap  # create a new list with cap size
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._queue[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def print_queue(self):
        temp = self._front


if __name__ == '__main__':
    q = ArrayQueue()
    n = int(input())
    for i in range(n):
        q.enqueue(int(input()))
    q.print_queue()
    # return the first value of the queue
    print("First value of the queue:", q.first())
    # Enter a value and erase it
    add = input("Adding value into the queue: ")
    q.enqueue(add)
    print("Print queue after having added the value: ")
    q.print_queue()
    # Remove the first value
    q.dequeue()
    print("Print queue after having removed the first value: ")
    q.print_queue()

