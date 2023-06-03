# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(candidates, idx, target, sum, curLst):
            if sum == target:
                res.append(curLst)
                return
            
            if sum > target or idx >= len(candidates):
                return

            dfs(candidates, idx + 1, target, sum, curLst.copy())
            dfs(candidates, idx, target, sum + candidates[idx], curLst.copy() + [candidates[idx]])
            
        dfs(candidates, 0, target, 0, [])
        return res