import Graph
import string
import random


class RandomGraph(Graph.Graph):
    def add_random_edges(self, p):
        vertices = self.vertices()
        verticesLen = len(vertices)
        for i in range(verticesLen):
            for j in range(i + 1, verticesLen):
                    if (random.random() < p):
                        e = Graph.Edge(vertices[i], vertices[j])
                        self.add_edge(e)


def generateRandomGraphs(nList, pList):
    total = 100
    nListLen = len(nList)
    labels = string.lowercase + string.uppercase + string.punctuation
    for i in range(nListLen):
        count = 0
        for j in range(total):
            if nList[i] > len(labels): return 
            vs = [Graph.Vertex(c) for c in labels[:nList[i]]]
            g = RandomGraph(vs)
            g.add_random_edges(pList[i])
            if (g.is_connected()): count += 1
        print("For n = " + str(nList[i]) + " and p = " + str(pList[i]) + 
        " probability it is connected is: " + str(float(count)/total))

