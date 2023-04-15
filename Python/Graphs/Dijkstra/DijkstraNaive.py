def findClosestVertex(distances, visited):
    min = 1e7
    result = -1    
    
    for idx in range(len(distances)):
        if distances[idx] < min and visited[idx] == False:
            min = distances[idx]
            result = idx
    
    return result

def dijkstraNaive(graph, s):
    n = len(graph)
    vistied = [False] * n
    distances = [1e7] * n    
    distances[s] = 0
    
    for i in range(n):
        idx = findClosestVertex(distances, vistied)        
        vistied[idx] = True
                
        for adjV in graph[idx]:
            vertex = adjV[0]
            length = adjV[1]
            
            if vistied[vertex] == False and distances[vertex] > (distances[idx] + length):
                distances[vertex] = distances[idx] + length
        
    return distances
    
# graph = [[(1, 2), (2, 3)], [(3, 1)], [(3, 4)], []]

graph = [[(1, 1)], [(2, -5)], [(3, 2)], [(1, 3)]]
print(dijkstraNaive(graph, 0))