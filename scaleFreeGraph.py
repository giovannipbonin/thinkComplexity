import generator
import Graph
import random
import RandomGraph


class ScaleFreeGraph(Graph.Graph):
    def __init__(self, m0):
        self.gen = generator.alphaNum_generator()
        vertices = []
        for i in range(m0):
            vertices.append(Graph.Vertex(self.gen.next()))
        Graph.Graph.__init__(self, vertices)
        self.add_regular_edges(m0 - 1)
        self.edgeCount = (m0 - 1)*m0
    def add_node(self):
        vertices = self.vertices()
        newNode = Graph.Vertex(self.gen.next())
        for v in vertices:
            v_edgesNumber = len(self.out_vertices(v))
            p = v_edgesNumber/float(self.edgeCount)
            if (random.random() < p):
                newEdge = Graph.Edge(v, newNode)
                self.add_vertex(newNode)
                self.add_edge(newEdge)
                self.edgeCount += 2







