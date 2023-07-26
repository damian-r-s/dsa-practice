// 213. House Robber II
// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
//That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
//Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

public class Solution
{
    public int Rob(int[] nums)
    {
        int n = nums.Length;
        if (n == 1)
            return nums[0];

        int[] houses1 = new int[n - 1];
        int[] houses2 = new int[n - 1];

        Array.Copy(nums, houses1, n - 1);
        Array.Copy(nums, 1, houses2, 0, n - 1);

        return Math.Max(RobH(houses1), RobH(houses2));
    }

    public int RobH(int[] nums)
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