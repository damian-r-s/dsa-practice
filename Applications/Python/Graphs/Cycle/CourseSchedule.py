# 207. Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def __init__(self):
        self.graph = {}
    
    def connect(self, src, dst):        
        if src not in self.graph:
            self.graph[src] = []
            
        self.graph[src].append(dst)

    def construct(self, edges: List[List[int]]):
        for i in range(len(edges)):
            self.connect(edges[i][1], edges[i][0])

    def dfs(self, src, visited, processed):
        visited.add(src)

        if src in self.graph:
            for key in self.graph[src]:
                if key not in visited:
                    if self.dfs(key, visited, processed):
                        return True

                if key in visited and key not in processed:
                    return True

        processed.add(src)
        return False

    def cycle(self):
        visited = set()
        processed = set()
        
        for key in self.graph.keys():
            if key not in visited:
                if self.dfs(key, visited, processed):
                    return True

                processed.add(key)

        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.construct(prerequisites)
        
        if self.cycle():
            return False
        return True