## This file contains the implementation of a Graph

import Queue

class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """create a new graph. (vs) is a list of vertices;
        (es) is a list of edges."""
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """add (v) to the graph"""
        self[v] = {}
    
    def add_edge(self, e):
        """add (e) to the graph by adding an entry in both directions.
        If there is already an edge connecting these Vertices, the new
        edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v1, v2):
        return self.get(v1).get(v2) 

    def remove_edge(self, e):
        v1, v2 = e
        del self[v1][v2]
        del self[v2][v1]
        
    def vertices(self):
        return self.keys()

    def edges(self):
        edgeSet = set()
        for v in self.keys():
            edgeSet.update(self[v].values())
        return edgeSet

    def out_vertices(self, v):
            return self[v].keys() 

    def out_edges(self, v):
            return self[v].values()

    def add_all_edges(self):
        vertices = self.vertices()
        verticesNumber = len(vertices)
        for i in range(verticesNumber):
            for j in range(i + 1, verticesNumber):
                e = Edge(vertices[i], vertices[j])
                self.add_edge(e)
    def add_regular_edges(self, n):
        vertices = self.vertices()
        verticesNumber = len(vertices)
        if (n > verticesNumber - 1): return
        if (n % 2 == 1 and verticesNumber % 2 == 1): return
        for i in range(verticesNumber):
            for j in range(n/2):
                e1 = Edge(vertices[i], vertices[(i + j + 1)%verticesNumber])
                e2 = Edge(vertices[i], vertices[i - j - 1])
                self.add_edge(e1)
                self.add_edge(e2)
            if (n % 2 == 1): 
                e1 = Edge(vertices[i], vertices[(i + verticesNumber/2)%verticesNumber])
                self.add_edge(e1)
    def is_connected(self):
       vertices = self.vertices()
       verticesLen = len(vertices)
       if (verticesLen == 0): return True
       q = Queue.Queue()
       s = set()
       q.put(vertices[0])
       while (not q.empty()):
            v = q.get()
            s.add(v)
            for v2 in self[v]:
                if v2 not in s:
                    q.put(v2)
       return len(s) == len(vertices)


                

class Vertex(object):
    def __init__(self, label=''):
        self.label = label
    
    def __repr__(self):
        return 'Vertex(%s)' %repr(self.label)
    __str__ = __repr__


class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__



