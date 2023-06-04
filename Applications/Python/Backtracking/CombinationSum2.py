# 40. Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(candidates, idx, target, sum, curLst):
            if sum == target:
                res.append(curLst)
                return            
            
            if sum > target or idx >= len(candidates):
                return
                        
            dfs(candidates, idx + 1, target, sum + candidates[idx], curLst.copy() + [candidates[idx]])
            
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1

            dfs(candidates, idx + 1, target, sum, curLst.copy())
            
            
        dfs(candidates, 0, target, 0, [])
        return res