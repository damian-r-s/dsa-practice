# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:    
    def climbStairs(self, n: int) -> int:

        if n <= 3:
            return n

        curr = 3
        prev = 2

        for i in range(4, n + 1):
            tmp = curr + prev
            prev = curr
            curr = tmp

        return curr