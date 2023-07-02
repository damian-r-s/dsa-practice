# 684. Redundant Connection
# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

class Solution:
    def __init__(self):
        self.graph = {}
        
    def findParent(self, x):
        if self.graph[x] == -1:
            return x

        return self.findParent(self.graph[x])

    def union(self, x, y):
        self.graph[x] = y

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for edge in edges:
            x = edge[0]
            y = edge[1]

            if x not in self.graph:
                self.graph[x] = -1

            if y not in self.graph:
                self.graph[y] = -1

            parentX = self.findParent(x)
            parentY = self.findParent(y)

            if parentX == parentY:
                return (x, y)

            self.union(parentX, parentY)

        return (0, 0)