// 763. Partition Labels
// You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
// Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
// Return a list of integers representing the size of these parts.

class Solution
{
    IList<int> PartitionLabels(string s)
    {
        var set = new Dictionary<char, int>();
        for (var i = 0; i < s.Length; i++)
        {
            if (set.ContainsKey(s[i]))
            {
                set[s[i]] = i;
                continue;
            }
            set.Add(s[i], i);
        }

        var result = new List<int>();
        var separator = 0;
        var count = 0;
        for (var i = 0; i < s.Length; i++)
        {
            count++;
            if (separator < set[s[i]])
                separator = set[s[i]];

            if (separator == i)
            {
                result.Add(count);
                count = 0;
            }
        }

        return result;
    }
}