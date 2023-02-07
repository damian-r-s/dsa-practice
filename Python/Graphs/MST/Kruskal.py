def find(parent, i):
    if parent[i] == i:
        return i    
    return find(parent, parent[i])

def addEdge(graph, u, v, w):
    graph.append([u, v, w])

def union(parent, rank, u, v):
    uRoot = find(parent, u)
    vRoot = find(parent, v)
    
    if rank[uRoot] < rank[vRoot]:
        parent[uRoot] = vRoot
    elif rank[vRoot] < rank[uRoot]:
        parent[vRoot] = uRoot
    else: # because are equal and attaching cause that root is the extra node
        parent[vRoot] = uRoot
        rank[uRoot] += 1
        
def kruskal(graph, vertexes):
    parent = [i for i in range(vertexes)]    
    rank = [0 for i in range(vertexes)]    
    graph = sorted(graph, key = lambda item: item[2])
    
    result = []
    index = 0    
    edge = 0
    while edge < vertexes - 1:
        u, v, w = graph[index]
        index += 1
        
        uRoot = find(parent, u)
        vRoot = find(parent, v)
        
        if uRoot != vRoot: # make union            
            union(parent, rank, u, v)
            result.append([u, v, w])
            edge += 1
                        
    return result


graph = []
addEdge(graph, 0, 1, 2)
addEdge(graph, 1, 0, 2)
addEdge(graph, 0, 4, 1)
addEdge(graph, 4, 0, 1)
addEdge(graph, 1, 2, 1)
addEdge(graph, 2, 1, 1)
addEdge(graph, 1, 3, 1)
addEdge(graph, 3, 1, 1)
addEdge(graph, 2, 3, 5)
addEdge(graph, 3, 2, 5)

result = kruskal(graph, 5)

for u, v, w in result:
    print ("From: %d to: %d weight: %d" % (u, v, w))