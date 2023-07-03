# 70. Climbing Stairs
# 

class Solution:    
    def __init__(self):
        self.results = {}

    def climbStairs(self, n: int) -> int:
        if n in self.results:
            return self.results[n]

        if n == 0:
            return 1
        
        if n < 0:
            return 0

        self.results[n - 1] = self.climbStairs(n - 1)
        self.results[n - 2] = self.climbStairs(n - 2)

        return self.results[n - 1] + self.results[n - 2]

