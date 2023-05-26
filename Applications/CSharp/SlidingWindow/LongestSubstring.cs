// 3. Longest Substring Without Repeating Characters
// Given a string s, find the length of the longest substring without repeating characters.

int LengthOfLongestSubstring(string s)
{
    var set = new HashSet<char>();
    var l = 0;
    var result = 0;

    for (var r = 0; r < s.Length; r++)
    {
        while (set.Contains(s[r]))
        {
            set.Remove(s[l]);
            l++;
        }

        set.Add(s[r]);
        result = Math.Max(result, r - l + 1);
    }

    return result;
}