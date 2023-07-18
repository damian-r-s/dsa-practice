//198. House Robber
//You are a professional robber planning to rob houses along a street. 
//Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
//Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

public class Solution
{
    public int Rob(int[] nums)
    {
        return Rob(nums, 0, 0);
    }

    private Dictionary<(int, int), int> _state = new Dictionary<(int, int), int>();

    private int Rob(int[] nums, int current, int lot)
    {
        if (current >= nums.Length)
            return lot;

        if (_state.ContainsKey((current, lot)))
            return _state[(current, lot)];

        var r1 = Rob(nums, current + 2, lot + nums[current]);
        var r2 = Rob(nums, current + 1, lot);

        _state[(current, lot)] = Math.Max(r1, r2);

        return _state[(current, lot)];
    }
}