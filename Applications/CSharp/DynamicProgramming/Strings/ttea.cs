// 91. Decode Ways
// A message containing letters from A-Z can be encoded into numbers using the following mapping:
// To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
// "AAJF" with the grouping (1 1 10 6)
// "KJF" with the grouping (11 10 6)
// Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
// Given a string s containing only digits, return the number of ways to decode it.
// The test cases are generated so that the answer fits in a 32-bit integer.

public class Solution
{
    public int NumDecodings(string s)
    {
        var ways = Enumerable.Repeat(1, s.Length + 1).ToList();

        for (var i = s.Length - 1; i >= 0; i--)
        {
            if (s[i] == '0')
                ways[i] = 0;
            else
            {
                ways[i] = ways[i + 1];
            }

            if (i + 1 < s.Length && (s[i] == '1' || (s[i] == '2' && "0123456".Contains(s[i + 1]))))
            {
                ways[i] += ways[i + 2];
            }
        }

        return ways[0];
    }
}