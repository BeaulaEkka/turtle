# breath-borad/wide-O(v+e) vertices and edges
# first in first out
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E', 'F'],
#     'C': ['G'],
#     'D': [],
#     'E': [],
#     'F': ['H'],
#     'G': ['I'],
#     'H': [],
#     'I': [],
# }


# def bfs(graph, node):
#     visited = []
#     queue = []

#     visited.append(node)
#     queue.append(node)

#     while queue:
#         s = queue.pop(0)
#         print(s, end="")

#         for n in graph[s]:
#             if n not in visited:
#                 visited.append(n)
#                 queue.append(n)

# Global /class scope variables
# n=number of nodes in the graph
# g=adjacency list representing unweighted graph

# s=start node, e=end_node, and 0<=e,s<n
# function bfs(s,e)

# Return reconstructed path from s->e
# return reconstructPath(s,e,prev)

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': [],
}

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end='')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

#Driver Code
print("following is the breath-first Search")
bfs(visited, graph, '4')  # Output: 5 3 7