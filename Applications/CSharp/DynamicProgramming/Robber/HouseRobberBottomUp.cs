//198. House Robber
//You are a professional robber planning to rob houses along a street. 
//Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
//Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

public class Solution
{
    public int Rob(int[] nums)
    {
        int n = nums.Length;
        int prev = 0;
        int current = 0;

        for (int i = 0; i < n; i++)
        {
            var maximum = Math.Max(prev + nums[i], current);
            prev = current;
            current = maximum;
        }

        return current;
    }
}