from collections import deque
from queue import Queue

# queue implementation using collections.deque
q = deque()
for i in range(11):
    q.append(i)
while len(q) != 0:
    print(q.popleft(), end=' ')
print()

# queue implementation using Queue.queue
# initializing a queue
q = Queue(maxsize=100)
# print maxsize of the queue
print(q.qsize())
# adding element to the queue
for i in range(11):
    q.put(i)
while q.empty() is False:
    print(q.get(), end=' ')
