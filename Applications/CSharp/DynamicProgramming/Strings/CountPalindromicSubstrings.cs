// 647. Palindromic Substrings
// Given a string s, return the number of palindromic substrings in it.
// A string is a palindrome when it reads the same backward as forward.
// A substring is a contiguous sequence of characters within the string.

public class Solution
{
    public int CountSubstrings(string s)
    {
        var n = s.Length;
        var result = 0;


        for (int i = 0; i < n; i++)
        {
            result += SubPalindromic(s, i, i);
            result += SubPalindromic(s, i, i + 1);
        }

        return result;
    }

    int SubPalindromic(string s, int i, int j)
    {
        var count = 0;

        while (i >= 0 && j < s.Length && s[i] == s[j])
        {
            count++;
            i--;
            j++;
        }

        return count;
    }
}