import math

from datastructures.edge import Edge
from datastructures.graph import Graph

def dijkstra(graph: Graph, source: str):
    distances: dict[str, int] = {}
    previous: dict[str, Edge] = {}
    all_vertices = graph.all_vertices()
    for key in all_vertices.keys():
        distances[key] = math.inf
        previous[key] = None
    distances[source] = 0
    current_vertex_name = source

    while len(all_vertices) > 0:
        vertex_edges = all_vertices.pop(current_vertex_name)
        unvisited_neighbors: dict[str, Edge] = {}

        for edge in vertex_edges:
            label = edge.first_label if edge.second_label == current_vertex_name else edge.second_label
            if label in all_vertices:
                unvisited_neighbors[label] = edge

        for label, edge in unvisited_neighbors.items():
            total_distance = distances[current_vertex_name] + edge.distance
            if total_distance < distances[label] and distances[current_vertex_name] < math.inf:
                distances[label] = total_distance
                previous[label] = edge

        if len(all_vertices) > 0:
            distances_without_current = {key: value for key, value in distances.items() if key in all_vertices}
            next_vertex = min(distances_without_current.items(), key=lambda x: x[1])
            current_vertex_name = next_vertex[0]

    return (distances, previous)


e1 = Edge('Curitiba', 'Chicago', 7)
e2 = Edge('Curitiba', 'Irvine', 9)
e3 = Edge('Curitiba', 'Page', 14)
e4 = Edge('Chicago', 'Evanston', 15)
e5 = Edge('Chicago', 'Irvine', 10)
e6 = Edge('Irvine', 'Page', 2)
e7 = Edge('Irvine', 'Evanston', 11)
e8 = Edge('Page', 'Toronto', 9)
e9 = Edge('Evanston', 'Toronto', 6)

g = Graph([e1, e2, e3, e4, e5, e6, e7, e8, e9])

print(dijkstra(g, 'Curitiba'))