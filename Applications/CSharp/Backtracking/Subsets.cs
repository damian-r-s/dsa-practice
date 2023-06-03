// 78. Subsets
// Given an integer array nums of unique elements, return all possible subsets (the power set).
// The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution
{
    public IList<IList<int>> Subsets(int[] nums)
    {
        return Subsets(nums, 0);
    }

    private IList<IList<int>> Subsets(int[] nums, int idx)
    {
        IList<IList<int>> res = new List<IList<int>>();
        if (idx + 1 <= nums.Length)
        {
            var left = Subsets(nums, idx + 1);
            foreach (var l in left)
            {
                l.Add(nums[idx]);
                res.Add(l);
            }

            var right = Subsets(nums, idx + 1);
            foreach (var r in right)
            {
                res.Add(r);
            }
        }
        else
        {
            res.Add(new List<int>());
        }

        return res;
    }
}
