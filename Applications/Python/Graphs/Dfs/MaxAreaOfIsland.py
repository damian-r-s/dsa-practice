# 695. Max Area of Island
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        n = len(grid)
        m = len(grid[0])        
        maxi = 0
        v = set()

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 or (i, j) in v:
                return 0

            v.add((i, j))         
            l = dfs(i - 1, j)
            r = dfs(i + 1, j)
            t = dfs(i, j + 1)
            d = dfs(i, j - 1)

            return l + r + t + d + 1

        for i in range(n):
            for j in range(m):                                
                candidate = dfs(i, j)
                if candidate > maxi:
                    maxi = candidate                    

        return maxi
