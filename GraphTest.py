from GraphWorld import *
from Graph import Vertex
from Graph import Edge
from Graph import Graph
import time
import string
import SmallWorldGraph
import random
import math
import generator
import matplotlib.pyplot as pyplot


from itertools import chain

try:
    from Gui import Gui, GuiCanvas
except ImportError:
    from swampy.Gui import Gui, GuiCanvas


def main(script, n='1000', *args):
    # create n Vertices
    n = int(n)
    gen = generator.alphaNum_generator() 
    vs = [Vertex(gen.next()) for i in range(n)]

    # create a graph and a layout
  #  g = Graph(vs)
#j    g.add_regular_edges(3)

    # draw the graph
    gw = GraphWorld()
    coefficients = []
    x = [i/float(100) for i in range(100)]
    g0 = SmallWorldGraph.SmallWorldGraph(vs, 10, 0)
    g0Coeff = g0.clustering_coefficient()
    for p in x:
        g = SmallWorldGraph.SmallWorldGraph(vs, 10, p)
        gCoeff = g.clustering_coefficient()
        coefficients.append(gCoeff/g0Coeff)
        layout = CircleLayout(g)
        gw.show_graph(g, layout)
        gw.update_idletasks()
        gw.update()
        time.sleep(0.01)
    gw.mainloop()
    #gbase = SmallWorldGraph.SmallWorldGraph(v1, 
    pyplot.xlabel("Probability")
    pyplot.ylabel("Clustering Coefficient")
    pyplot.title("Clustering Coefficient for Small World Theory")
    pyplot.plot(x, coefficients)
    pyplot.xscale('log')
    #pyplot.show()

if __name__ == '__main__':
    import sys
    main(*sys.argv)


