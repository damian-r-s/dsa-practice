# 746. Min Cost Climbing Stairs
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

class Solution:    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1:
            return cost[0]

        result = [9999 for x in range(n + 1)]
        result[0] = 0
        result[1] = cost[0]
        
        for stair in range(2, n + 1, 1):                                    
            step1 = result[stair - 1]
            if (n + 1 - stair) > 1:
                step1 +=  cost[stair - 1]            

            step2 = result[stair - 2] + cost[stair - 1]            
            result[stair] = min(step1, step2)

        return result[n]



                