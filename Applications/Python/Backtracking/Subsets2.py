# 90. Subsets II
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(nums, idx, cur):
            if idx == len(nums):
                res.append(cur)
                return

            cur.append(nums[idx])
            dfs(nums, idx + 1, cur.copy())

            cur.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(nums, idx + 1, cur.copy())


        dfs(nums, 0, [])
        return res