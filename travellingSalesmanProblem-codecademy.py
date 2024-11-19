import random
from random import randrange


class Vertex:
    def __init__(self, value):
        self.value = value  # The value or label of the vertex
        self.edges = {}     # Dictionary to store edges and their weights

    def add_edge(self, vertex, weight=0):
        """
        Add an edge to this vertex, connecting it to another vertex with a given weight.
        """
        self.edges[vertex] = weight

    def get_edges(self):
        # Get all vertices this vertex is connected to.
        return list(self.edges.keys())

    def get_weight(self, edge):
        # Get the weight of the edge to the specified connected vertex.
        # Return the weight, or None if the edge doesn't exist
        return self.edges.get(edge, None)


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        # Add a vertex to the graph
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        # Add a directed edge from one vertex to another with a given weight
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(
                from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = set()
        while start:
            current_vertex = start.pop()
            if current_vertex in seen:
                continue
            seen.add(current_vertex)
            if current_vertex == end_vertex:
                return True
            neighbors = self.graph_dict[current_vertex].get_edges()
            start.extend(neighbors)
        return False


def print_graph(graph):
    for vertex in graph.graph_dict:
        print(f"{vertex} connected to:")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if not vertex_neighbors:
            print("  No Edges")
        else:
            for adjacent_vertex, weight in vertex_neighbors.items():
                print(f"  => {adjacent_vertex} (Weight: {weight})")


def build_tsp_graph(directed):
    g = Graph(directed)
    vertices = []
    for val in ["a", "b", "c", "d"]:
        vertex = Vertex(val)
        vertices.append(vertex)
        g.add_vertex(vertex)

    g.add_edge(vertices[0], vertices[1], 3)
    g.add_edge(vertices[0], vertices[2], 4)
    g.add_edge(vertices[0], vertices[3], 5)
    g.add_edge(vertices[1], vertices[2], 2)
    g.add_edge(vertices[1], vertices[3], 6)
    g.add_edge(vertices[2], vertices[3], 1)
    return g


# Build the graph and print it
tsp_graph = build_tsp_graph(directed=False)
print_graph(tsp_graph)
