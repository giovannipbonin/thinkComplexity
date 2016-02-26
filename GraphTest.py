from GraphWorld import *
from Graph import Vertex
from Graph import Edge
from Graph import Graph
import string
import random
import math

from itertools import chain

try:
    from Gui import Gui, GuiCanvas
except ImportError:
    from swampy.Gui import Gui, GuiCanvas


def main(script, n='9', *args):
    # create n Vertices
    n = int(n)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    # create a graph and a layout
    g = Graph(vs)
    g.add_regular_edges(3)
    layout = CircleLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()


if __name__ == '__main__':
    import sys
    main(*sys.argv)


