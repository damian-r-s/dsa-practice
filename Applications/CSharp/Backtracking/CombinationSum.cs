// 39. Combination Sum
// Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
// The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
// The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution
{
    public IList<IList<int>> CombinationSum(int[] candidates, int target)
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

            Dfs(candidates, idx + 1, sum, target, new List<int>(copy));
            Dfs(candidates, idx, sum + candidates[idx], target, new List<int>(copy) { candidates[idx] });
        }

        Dfs(candidates, 0, 0, target, new List<int>());

        return result;
    }
}