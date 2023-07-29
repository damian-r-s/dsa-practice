// 152. Maximum Product Subarray
// Given an integer array nums, find a subarray that has the largest product, and return the product.
// The test cases are generated so that the answer will fit in a 32-bit integer.

public class Solution
{
    public int MaxProduct(int[] nums)
    {
        var n = nums.Length;

        var maxProduct = nums.Max();
        (int curMin, int curMax) = (1, 1);

        foreach (var l in nums)
        {
            var tmp = curMax * l;

            curMax = new int[] { l, l * curMin, l * curMax }.Max();
            curMin = new int[] { l, l * curMin, tmp }.Min();

            maxProduct = Math.Max(maxProduct, curMax);
        }

        return maxProduct;
    }
}