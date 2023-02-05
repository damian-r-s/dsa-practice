import queue

# 0 White
# 1 Gray
# 2 Black

# It does not check if DAG
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
        dfsNested(adj, edges, state, topology)

    state[vertex] = 2
    topology.append(vertex)

def printResult(topology):
    for i in range(len(topology) - 1, -1, -1):
        print(topology[i], sep='', end=' ', flush=True)

graphSorted = topological([[1, 2, 3], [], [3], [4], []])

printResult(graphSorted)

