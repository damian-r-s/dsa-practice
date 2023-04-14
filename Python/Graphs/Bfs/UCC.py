#Undirected Connected components on BFS
import queue

def UCC(graph):    
    q = queue.Queue()    
    length = len(graph)
    visited = [0 for i in range(length)]
    componetns = [0 for i in range(length)]
    ucc = 0    
    
    for vertex in range(length):
        if visited[vertex] == 1:
            continue        
        ucc += 1
        q.put(vertex)        
        while q.empty() == False:
            s = q.get()
            if visited[s] == 1:
                continue
            visited[s] = 1
            componetns[s] = ucc            
            for v in graph[s]:
                q.put(v)        
        
    return componetns

print(UCC([[1], [0, 2], [3, 1], [2]]))