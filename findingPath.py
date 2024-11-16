class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())

    def __str__(self):
        return f"Vertex({self.value})"


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(
                from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex.value]  # Use the value (string) for the search
        visited = set()

        while start:
            current_vertex_value = start.pop(0)
            print(f"Visiting {current_vertex_value}")

            if current_vertex_value == end_vertex.value:
                return True

            if current_vertex_value not in visited:
                visited.add(current_vertex_value)
                vertex = self.graph_dict[current_vertex_value]
                next_vertices = vertex.get_edges()
                start.extend(next_vertices)

        return False


# Create a directed graph and vertices
directed_railway = Graph(True)
rotterdam = Vertex('Rotterdam')
den_haag = Vertex("Den Haag")
amsterdam = Vertex("Amsterdam")
zuid_beijerland = Vertex('Zuid Beijerland')

directed_railway.add_vertex(rotterdam)
directed_railway.add_vertex(den_haag)
directed_railway.add_vertex(amsterdam)
directed_railway.add_vertex(zuid_beijerland)

directed_railway.add_edge(rotterdam, den_haag, 26)
directed_railway.add_edge(den_haag, amsterdam, 25)
directed_railway.add_edge(amsterdam, zuid_beijerland, 30)
directed_railway.add_edge(zuid_beijerland, rotterdam, 35)

# Find the path and print results
find_path_rotterdam = directed_railway.find_path(rotterdam, zuid_beijerland)

print(f"Path exists from Rotterdam to Zuid Beijerland: {find_path_rotterdam}")
# print(rotterdam.value)
# print(den_haag.value)
