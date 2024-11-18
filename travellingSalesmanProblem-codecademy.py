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
        """
        Get all vertices this vertex is connected to.
        """
        return list(self.edges.keys())

    def get_weight(self, edge):
        """
        Get the weight of the edge to the specified connected vertex.
        """
        return self.edges.get(edge, None)  # Return the weight, or None if the edge doesn't exist
