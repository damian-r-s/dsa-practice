// 17. Letter Combinations of a Phone Number
// Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
// A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

public class Solution
{
    private Dictionary<int, char[]> dic = new Dictionary<int, char[]>() { };
    public Solution()
    {
        dic.Add(2, new char[] { 'a', 'b', 'c' });
        dic.Add(3, new char[] { 'd', 'e', 'f' });
        dic.Add(4, new char[] { 'g', 'h', 'i' });
        dic.Add(5, new char[] { 'j', 'k', 'l' });
        dic.Add(6, new char[] { 'm', 'n', 'o' });
        dic.Add(7, new char[] { 'p', 'q', 'r', 's' });
        dic.Add(8, new char[] { 't', 'u', 'v' });
        dic.Add(9, new char[] { 'w', 'x', 'y', 'z' });
    }

    public IList<string> LetterCombinations(string digits)
    {
        return LetterCombinations(digits, 0, null);
    }

    private IList<string> LetterCombinations(string digits, int idx, string current)
    {
        if (idx >= digits.Length)
        {
            if (string.IsNullOrEmpty(current))
                return new List<string>();

            return new List<string>() { current };
        }

        var idxI = digits[idx] - '0';
        return dic[idxI].ToList().Select(x => LetterCombinations(digits, idx + 1, current + x)).SelectMany(x => x).ToList();
    }
}