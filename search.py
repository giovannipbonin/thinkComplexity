import Queue

def dijkstraSearch(graph, start):
    queue = Queue.Queue() 
    queue.put(start)
    distances = {}
    vertices = graph.vertices()
    for v in vertices:
       distances[v] = float('inf') 
    distances[start] = 0
        
    while (not queue.empty()):
        vertex = queue.get()
        d = distances[vertex]
        for v in graph.out_vertices(vertex):
            if (distances[v] == float('inf')):
                distances[v] = d + 1
                queue.put(v)
    return distances
