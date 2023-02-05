# 0 White
# 1 Gray
# 2 Black

# If cycle detected then Exception thrown
def topological(edges):
    n = len(edges)
    state = [0 for _ in range(n)] # 0, 1, 2 lines: 1, 2, 3
    topology = []
    
    for vertex in range(n):
        dfsNested(vertex, edges, state, topology)
        
    return topology

def dfsNested(vertex, edges, state, topology):
    if state[vertex] != 0:
        return
    
    state[vertex] = 1
    
    for adj in edges[vertex]:
        if state[adj] == 1:
            raise Exception("Only DAG can posses topological sorted order!")
        
        dfsNested(adj, edges, state, topology)

    state[vertex] = 2
    topology.append(vertex)

def numberofSimplePaths(graph, topology, source, destination):
    n = len(graph)
    df = [0 for i in range(n)]
    df[destination] = 1
    
    for i in range(n):
        v = topology[i]
        
        for e in graph[v]:
            df[v] += df[e]
    
    return df[source]

graph = [[1, 2, 3, 4], [], [3], [4], []]
graphSorted = topological(graph)
simplePaths = numberofSimplePaths(graph, graphSorted, 0, 4)

print("Number of simple paths: " + str(simplePaths))