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


from itertools import chain

try:
    from Gui import Gui, GuiCanvas
except ImportError:
    from swampy.Gui import Gui, GuiCanvas


def main(script, *args):
    # create n Vertices
    n = 7

    # create a graph and a layout
    g = scaleFreeGraph.ScaleFreeGraph(5)
    layout = RandomLayout(g)
    # draw the graph and iterate adding more nodes
    gw = GraphWorld()
    while (n < 1000):
        gw.update_idletasks()
        gw.show_graph(g, layout)
        gw.update()
        newV = g.add_node()
        layout.add_vertex(newV)
        n += 1
        time.sleep(0.1)
    gw.mainloop()

if __name__ == '__main__':
    import sys
    main(*sys.argv)


