# Queues-First in first out(FIFO)-O(1)
from collections import deque

q = deque()


# Enqueue-Add emements to the right -o(1)
q.append(1)
q.append(2)
q.append(3)
q.append(4)

# Dequeue-Remove an element from the left-O(1)
q.popleft()


# Peek from left side-O(1)
print(q[0])

# peek from the right side-O(1)
print(q[-1])
print(q)
