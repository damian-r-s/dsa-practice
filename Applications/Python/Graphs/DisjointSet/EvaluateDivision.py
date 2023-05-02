# You re given n rry of vrible pirs equtions nd n rry of rel numbers vlues, where equtions[i] = [i, Bi] nd vlues[i] represent the eqution i / Bi = vlues[i]. 
# Ech i or Bi is  string tht represents  single vrible.
# You re lso given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the nswer for Cj / Dj = ?.
# Return the nswers to ll queries. If  single nswer cnnot be determined, return -1.0.
# Note: The input is lwys vlid. You my ssume tht evluting the queries will not result in division by zero nd tht there is no contrdiction.

class Solution:
    def __init__(self):
        self.graph = {}
        
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        self.createGraph(equations, values)
        
        result = []
        for query in queries:  
            result.append(self.calculate(query[0], query[1], {}))        
            
        return result
        
    def calculate(self, src, to, visited):
        if src not in self.graph and to not in self.graph:
            return -1.0
        
        if src == to:
            return 1.0
        
        visited[src] = True        
        if src not in self.graph: # I do not know why this is needed, c# version does not need this check
            return -1.0
        
        adjList = self.graph[src]        
        
        for adj in adjList:                        
            if adj.key in visited:
                continue
            
            result = self.calculate(adj.key, to, visited)
            if result != -1.0:
                return result * adj.value
        
        return -1.0
    
    def connect(self, src, dest, value):
        if src not in self.graph:
            self.graph[src] = []
            
        self.graph[src].append(self.Node(dest, value))
        
    def createGraph(self, equations, values):
        for e in range(len(equations)):            
            src = equations[e][0]
            dest = equations[e][1]
            value = values[e]
                       
            self.connect(src, dest, value)
            self.connect(dest, src, 1/value)   