//  40. Combination Sum II
//  Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
//  Each number in candidates may only be used once in the combination.
//  Note: The solution set must not contain duplicate combinations.

class Solution
{
    public IList<IList<int>> CombinationSum2(int[] candidates, int target)
    {
        var result = new List<IList<int>>();

        void Dfs(int[] candidates, int idx, int sum, int target, List<int> copy)
        {
            if (sum == target)
            {
                result.Add(copy);
                return;
            }

            if (sum > target || idx >= candidates.Length)
                return;

            Dfs(candidates, idx + 1, sum + candidates[idx], target, new List<int>(copy) { candidates[idx] });

            while (idx + 1 < candidates.Length && candidates[idx] == candidates[idx + 1])
                idx += 1;

            Dfs(candidates, idx + 1, sum, target, new List<int>(copy));
        }

        Dfs(candidates.OrderBy(x => x).ToArray(), 0, 0, target, new List<int>());

        return result;
    }
}