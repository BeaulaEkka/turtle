# Graphs
# nodes=pairs

class Graph:
    def __init__(self, nodes, edges):
        self.edges = edges


# tuples can be used but the data structure need to transform to d
routes = [
    ("Mumbai", "Paris"),
    ('Mumbai', 'Dubai'),
    ('Paris', 'Dubai'),
    ('Paris', 'New York'),
    ('Dubai', 'New York'),
    ('New York', 'Toronto'),
]
route_graph = Graph(routes)

d = {
    "Mumbai": ["Paris", "New York"],
    "Paris": ["Dubai", "New York"],
    "Dubai": ["New York"],
    "New York": ["Toronto"],
    
}
