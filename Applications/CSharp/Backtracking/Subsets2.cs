// 90. Subsets II
// Given an integer array nums that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution
{
    IList<IList<int>> res = new List<IList<int>>();
    public IList<IList<int>> SubsetsWithDup(int[] nums)
    {
        Sub(nums.OrderBy(x => x).ToArray(), 0, new List<int>());
        return res;
    }

    void Sub(int[] nums, int idx, List<int> lst)
    {
        if (idx == nums.Length)
        {
            res.Add(lst);
            return;
        }

        Sub(nums, idx + 1, new List<int>(lst) { nums[idx] });

        var counter = idx + 1;
        while (counter < nums.Length && nums[counter] == nums[idx])
            counter = counter + 1;

        Sub(nums, counter, new List<int>(lst));
    }
}