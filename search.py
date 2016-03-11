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

def floydMarshall(graph):
    dist = [[float('inf') for i in range(verticesLen)] for i in range(verticesLen)] 
    vertices = {}
    verticesLen = 0
    verticesList = graph.vertices()
    for v in verticesList:
       vertices[v] = count
       dist[count][count] = 0
       verticesLen += 1
    edges = graph.edges()
    for e in edges:
        v1, v2 = e
        i, j = vertices[v1], vertices[v2]
        dist[i][j] = 1
    for k in range(verticesLen):
        for i in range(verticesLen):
            for j in range(verticesLen):
                if (dist[i][j] > dist[i][k] + dist[k][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
          
