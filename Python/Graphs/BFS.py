import queue
# 0 White
# 1 Gray
# 2 Black

def bfs(edges, source):
    n = len(edges)
    visited = [0 for _ in range(n)]
    distance = [0 for _ in range(n)]
        
    q = queue.Queue()    
    q.put(source)    
    distance[source] = 0
        
    while q.empty() != True:
        current = q.get()        
        
        for edge in edges[current]:
            if visited[edge] == 0:
                visited[edge] = 1
                distance[edge] = distance[current] + 1                
                q.put(edge)
        
        visited[current] = 2

    return distance
    
print(bfs([[1], [2, 4], [3], [6], [5], [], []] , 0))