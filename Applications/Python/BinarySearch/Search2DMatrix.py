# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)
        n = len(matrix[0]) - 1
        
        while l < r:
            m = (r + l) // 2            
            f = matrix[m][0]
            s = matrix[m][n]

            if f == target or s == target:
                return True
            
            if f < target and target < s:
                return self.search(matrix[m], target) != -1
            elif target < f:
                r = m
            else:
                l = m + 1

        return False
            

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while(l < r):
            m = (r + l) // 2            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m

        return -1