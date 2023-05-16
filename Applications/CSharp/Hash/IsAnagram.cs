// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

bool IsAnagram(string s, string t)
{
    if (string.IsNullOrEmpty(s) || string.IsNullOrEmpty(t))
        return false;

    if (s.Length != t.Length)
    {
        return false;
    }

    int[] counter = new int[26]; // lowercase characters 
    for (int i = 0; i < s.Length; i++)
    {
        counter[s[i] - 'a'] += 1;
        counter[t[i] - 'a'] -= 1;
    }

    for (int i = 0; i < counter.Length; i++)
    {
        if (counter[i] != 0)
        {
            return false;
        }
    }

    return true;
}