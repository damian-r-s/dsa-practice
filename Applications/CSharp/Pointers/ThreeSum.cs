class Solution
{
    public IList<IList<int>> ThreeSum(int[] nums)
    {
        Array.Sort(nums);
        var result = new List<IList<int>>();

        for (int i = 0; i < nums.Length; i++)
        {
            if (i > 0 && nums[i - 1] == nums[i])
                continue;

            int l = i + 1;
            int r = nums.Length - 1;
            int a = nums[i];

            while (l < r)
            {
                var sum = a + nums[l] + nums[r];

                if (sum == 0)
                {
                    result.Add(new List<int> { a, nums[l], nums[r] });
                    l++;
                    while (l < r && nums[l] == nums[l - 1])
                    {
                        l++;
                    }
                }
                else if (sum < 0)
                {
                    l++;
                }
                else
                {
                    r--;
                }
            }
        }

        return result;
    }
}