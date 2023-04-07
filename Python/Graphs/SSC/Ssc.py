# n - number of verticies
time = 0
def DfsFindTheOrder(edges):
    global time
    n = len(edges)
    order = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]        
    
    for v in range(n):
        DfsProcessing(v, edges, order, visited)                                 

    return order

def DfsProcessing(v, edges, order, visited):
    if (visited[v] == 1):
        return
    
    global time    
    visited[v] = 1    

    for edge in edges[v]:
        DfsProcessing(edge, edges, order, visited)     
                   
    order[v] = time
    time = time + 1
    
def RevertGraph(edges):
    n = len(edges)
    result = [[] for _ in range(n)]    
    
    for idx in range(n):        
        adj = edges[idx]        
        
        for a in adj:
            result[a].append(idx)
                
    return result      


def SSC(edges):    
    reverted = RevertGraph(edges)
    order = DfsFindTheOrder(reverted)
    sort = sorted(enumerate(order), key=lambda x: x[1], reverse=True)
    
    n = len(edges)
    visited = [0] * n
    stack = []
    classes = [i for i in range(n)]
    group = 0
    
    for v in sort:                
        if visited[v[0]] == 1:
            continue
        
        stack.append(v[0])        
        while (len(stack) > 0):
            current = stack.pop()                                                
            
            if visited[current] == 1:
                continue       
                 
            classes[current] = group            
            visited[current] = 1
            for edge in edges[current]:
                stack.append(edge)
                        
        group += 1
    return classes


print(SSC([[2], [0], [1], [1, 4], [5], [3], [5, 7], [6]]))