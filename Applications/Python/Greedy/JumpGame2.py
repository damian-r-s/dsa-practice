# 45. Jump Game II
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and i + j < n 
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
 

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        count = 0
        l = r = 0
        min = n * n

        while r < n:
            far = 0
            for i in range(l, r + 1):
                far = max(far, i + nums[i])

            l = r + 1
            r = far
            count += 1            

        return count        

