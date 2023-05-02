public class Solution
{
    public int HeightChecker(int[] heights)
    {
        var expected = new int[heights.Length];
        for (int i = 0; i < heights.Length; i++)
        {
            expected[i] = heights[i];
        }

        Array.Sort(expected);

        var inversions = 0;
        for (int i = 0; i < heights.Length; i++)
        {
            if (expected[i] != heights[i])
                inversions++;
        }
        return inversions;
    }
}