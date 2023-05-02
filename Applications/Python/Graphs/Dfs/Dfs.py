# 0 White
# 1 Gray
# 2 Black

time = 0

def dfs(edges):
    n = len(edges)        
    global time
    
    distIn = [0 for i in range(n)]
    distOut = [0 for i in range(n)]
    colour = [0 for i in range(n)]
        
    for v in range(n):        
        dfsProcessing(v, distIn, distOut, colour, edges)
            
    return (distIn, distOut)
        
def dfsProcessing(v, distIn, distOut, colour, edges):
    if colour[v] != 0:            
        return
    
    global time    
    colour[v] = 1    
    distIn[v] = time
    time = time + 1
    
    for e in edges[v]:
        dfsProcessing(e, distIn, distOut, colour, edges)
    
    distOut[v] = time
    time = time + 1
    

print(dfs([[1], [2], [3, 1, 2], []]))