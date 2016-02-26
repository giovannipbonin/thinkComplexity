## This file contains the implementation of a Graph


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



