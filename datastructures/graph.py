from .edge import Edge

class Graph:
    def __init__(self, edges: list[Edge]):
        self.edges = set(edges)

    def all_vertices(self) -> dict[str, list[Edge]]:
        all_vertices_list = {}
        for edge in self.edges:
            if edge.first_label not in all_vertices_list:
                all_vertices_list[edge.first_label] = []
            if edge.second_label not in all_vertices_list:
                all_vertices_list[edge.second_label] = []
            
            all_vertices_list[edge.first_label].append(edge)
            all_vertices_list[edge.second_label].append(edge)

        return all_vertices_list

    def vertex_with_edges(self, vertex: str) -> list[Edge]:
        return [edge for edge in self.edges if edge.first_label == vertex or edge.second_label == vertex]

    def edge_with_shorter_distance_to_vertex(self, vertex: str) -> Edge:
        all_edges_to_origin = self.vertex_with_edges(vertex)
        return min(all_edges_to_origin, key=lambda x: x.distance)
