# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

 

# Constraints:

#     2 <= nums.length <= 105
#     -30 <= nums[i] <= 30
#     The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

from ast import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        zero_idx = -1 
        product = 1        
        result = []

        for idx, i in enumerate(nums):
            if i == 0:
                zero += 1
                zero_idx = idx

                if zero > 1:
                    return [0] * len(nums)
            else:
                product *= i

            

        if zero_idx != -1:
            result = [0] * len(nums)
            result[zero_idx] = product
            return result

        for i in nums:            
            result.append((product // i))

        return result       
