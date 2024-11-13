# def dfs(G,v): G here is graph( O(v+e)) number of vertices and no.of edges
# visit(v)
'''
marked=[False] G.size()
def dfs(G,v):
visit(v)
marked[v]=True
for w in G.neighbors(v):# for each neighbour of v
if not marked[w]:
dfs(G.w)# use that as a starting node

'''

# DFS implementation 2
"""
marked=[False]*G.size()
def dfs(G,v):
stack=[v]
while len(stack)>0:
v=stack.pop()
if not marked[v]:
visit(v)
marked[v]=True

for w in G.neighbors(v):
if not marked[w]:
stack.append(w)
"""

# Preorder V/S Postorder

# Build Min Heap(Heapify)
# Time:O(n),space:O(1)

import heapq
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
heapq.heapify(A)
print(A)
# [-4, 0, 1, 3, 2, 5, 10, 8, 12, 9] not completely in ascending order

# Heap Push(insert an element)
# Time:O(logn),space:O(1)
heapq.heappush(A, 4)
print(f'heappush A:{A}')


# Heap pop(Extract min)
# Time:O(logn),space:O(1)
minn = heapq.heappop(A)
print(f'minn:{A, minn}')


# heapSort
# Time:O(nlogn),space:O(1)
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0]*n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    return new_list


heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(f'heapsort:{heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])}')
