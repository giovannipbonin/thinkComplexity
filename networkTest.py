from GraphWorld import *
from Graph import Vertex
from Graph import Edge
from Graph import Graph
import time
import string
import scaleFreeGraph
import random
import math
import generator
import matplotlib.pyplot as pyplot
import Pmf


from itertools import chain

try:
    from Gui import Gui, GuiCanvas
except ImportError:
    from swampy.Gui import Gui, GuiCanvas


def main(script, *args):
    # create a graph 
    n = 5
    g = scaleFreeGraph.ScaleFreeGraph(n)

    # draw the graph and iterate adding more nodes
    #layout = CircleLayout(g)
    #gw = GraphWorld()
    # while (n < 1000):
    #    gw.update_idletasks()
   #     gw.show_graph(g, layout)
   #     gw.update()
   #     newV = g.add_node()
   #     layout.add_vertex(newV)
   #     n += 1
   # gw.mainloop()
    for i in range(10000):
        g.add_node()  
    values = []
    for v in g.keys():
        values.append(len(g.out_vertices(v)))
    hist = Pmf.MakeHistFromList(values)
    k, frequency = hist.Render()
    frequency = [f/15010.0 for f in frequency]
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.plot(k, frequency)
    pyplot.show()
if __name__ == '__main__':
    import sys
    main(*sys.argv)


