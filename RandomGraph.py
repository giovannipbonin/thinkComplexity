import Graph
import random


class RandomGraph(Graph.Graph):
    def add_random_edges(self, p):
        vertices = self.vertices()
        for v1 in vertices:
            for v2 in vertices:
                if v1 != v2:
                    if (random.random() < p):
                        e = Graph.Edge(v1, v2)
                        self.add_edge(e)
