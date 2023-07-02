# 210. Course Schedule II
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    def __init__(self):
        self.graph = {}

    def create(self, vertex: int, edges: List[List[int]]):
        for i in range(vertex):
            self.graph[i] = []

        for edge in edges:
            self.graph[edge[1]].append(edge[0])

    def order(self):
        visited = set()
        processed = set()
        lst = []

        for src in self.graph.keys():
            if src not in visited:
                if not self.dfs(src, visited, processed, lst):
                    return []
                
        return reversed(lst)        

    def dfs(self, dst, visited, processed, lst):
        visited.add(dst)

        if dst in self.graph:
            for key in self.graph[dst]:
                if key not in visited:
                    if not self.dfs(key, visited, processed, lst):
                        return False

                if key in visited and key not in processed:
                    return False
        lst.append(dst)
        processed.add(dst)
        return True

        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.create(numCourses, prerequisites)
        return self.order()

