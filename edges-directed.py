# Array of Edges-Directed [ start, End]
from collections import defaultdict
n = 8
A = [
    [0, 1],
    [1, 2],
    [0, 3],
    [3, 4],
    [3, 6],
    [3, 7],
    [4, 2],
    [4, 5],
    [5, 2],
]
# convert Array of Edges ->Adjency Matrix
M = []
for i in range(n):

    M.append([0]*n)
for u, v in A:
    M[u][v] = 1
    # M[v][u]=1 # uncomment if undirected
# print(M)


# Convert Array of Edges->Adjency List
D = defaultdict(list)
for u, v in A:
    D[u].append(v)
print(M[3])
print(D[3])


#DFS with Recursion-O(v+E)
def dfs_recursive(node)