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
    #gw = GraphWorld()
    coefficients = []
    x = [0.0001, 0.001, 0.01, 0.1]
    y = [1.25, 2.5, 3.75, 5, 6.25, 7.5, 8.75, 10]
    scale = [i*j for i in x for j in y]
    avgLens = []
    g0 = SmallWorldGraph.SmallWorldGraph(vs, 10, 0)
    g0Coeff = g0.clustering_coefficient()
    g0AvgLen = g0.avg_path_length()
    for p in scale:
        g = SmallWorldGraph.SmallWorldGraph(vs, 10, p)
        gCoeff = g.clustering_coefficient()
        coefficients.append(gCoeff/g0Coeff)
        gAvgLen = g.avg_path_length()
        avgLens.append(gAvgLen/g0AvgLen)
    #layout = CircleLayout(g)
    #gw.show_graph(g, layout)
    #gw.update_idletasks()
    #gw.update()
    #time.sleep(0.01)
    #gw.mainloop()
    pyplot.xlabel("Probability")
    pyplot.ylabel("Clustering Coefficient & Avg Path Length Curves")
    pyplot.title("Clustering Coefficient for Small World Theory")
    pyplot.plot(scale, coefficients)
    pyplot.plot(scale, avgLens)
    pyplot.xscale('log')
    pyplot.show()

if __name__ == '__main__':
    import sys
    main(*sys.argv)


