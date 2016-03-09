import RandomGraph
import Graph
import random
import search


class SmallWorldGraph(RandomGraph.RandomGraph):
    def __init__(self, vs, k, p):
        RandomGraph.RandomGraph.__init__(self, vs)
        self.add_regular_edges(k)
        #self.rewire(p)
        self.customRewire(p)
    def rewire(self, p):
        edges = list(self.edges())
        vertices = self.vertices()
        for e in edges:
           if random.random() < p:
                v, temp = e
                self.remove_edge(e)
                
                w = random.choice(vertices)
                while (v == w or self.get_edge(v, w) != None):
                    w = random.choice(vertices)
                self.add_edge(Graph.Edge(v, w))
    def customRewire(self, p):
        edges = list(self.edges())
        vertices = self.vertices()
        for e in edges:
           if random.random() < p:
                self.remove_edge(e)
                w = random.choice(vertices)
                v = random.choice(vertices)
                while (v == w or self.get_edge(v, w) != None):
                    v = random.choice(vertices)
                self.add_edge(Graph.Edge(v, w))
    def clustering_coefficient(self):
        coefficientSum = 0;
        for v1 in self:
            vertices = self.out_vertices(v1)
            verticesN = len(vertices)
            if (verticesN < 2):
                coefficientSum += 1
                continue
            possibleEdges = verticesN*(verticesN - 1)/2.0
            totalEdges = 0
            for i in range(verticesN):
                for j in range(i, verticesN):
                    if(self.get_edge(vertices[i], vertices[j]) != None):
                        totalEdges += 1
            coefficientSum += totalEdges/possibleEdges
        return coefficientSum/len(self.vertices())
    def avg_path_length(self):
        vertices = self.vertices()
        verticesLen = len(vertices)
        totalPathLen = 0
        for v in vertices:
            distances = search.dijkstraSearch(self, v)
            totalPathLen += sum(distances.values())
        verticePairs = (verticesLen - 1)*verticesLen
        return totalPathLen/float(verticePairs)
