int LongestConsecutive(int[] nums)
{
    int longest = 0;
    HashSet<int> set = new HashSet<int>(nums);
    var current = 0;

    for (int i = 0; i < nums.Length; i++)
    {
        if (!set.Contains(nums[i] - 1))
        {
            int num = nums[i];
            current = 1;

            while (set.Contains(num + 1))
            {
                current++;
                num++;
            }
        }

        longest = Math.Max(longest, current);
    }

    return longest;
}