import numpy as np

with open("D:\Workspace\Algorithms\Python\Graphs\Dijkstra\data.txt") as f:
    lines = [[j for j in i.split('\t') if j != '\n'] for i in f.readlines() if i != ""]

graph = [[[int(z) for z in j.split(',')] for j in i[1:] ] for i in lines if i != ""]    
graph.insert(0, [])

def findClosestVertex(distances, visited):
    min = 1e7
    result = -1    
    
    for idx in range(len(distances)):
        if distances[idx] < min and visited[idx] == False:
            min = distances[idx]
            result = idx
    
    return result

def dijkstraNaive(graph, s):
    n = len(graph) + 1
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
    
distances = dijkstraNaive(graph, 1)
for i in range(len(distances)):
    print(f"{i} value: {distances[i]}")