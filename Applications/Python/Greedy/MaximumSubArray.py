# 53. Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, max = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]

            if curr > curr + sum:
                sum = curr
            else:
                sum += curr
            
            if sum > max:
                max = sum

        return max
