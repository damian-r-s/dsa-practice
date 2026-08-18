# 42. Trapping Rain Water
# Solved
# Hard
# Topics
# premium lock iconCompanies

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft   = [0] * len(height)
        maxRight = [0] * len(height)

        maxLeft[0]   =  height[0]
        maxRight[len(height) - 1] =  height[len(height) - 1]

        result = 0
        
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])

        for i in range(len(height)):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            result = result + max(0, water)

        return result