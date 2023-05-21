bool IsPalindrome(string s)
{
    var left = 0;
    var right = s.Length - 1;

    while (left < right)
    {
        while (left < right && !Char.IsLetterOrDigit(s[left]))
        {
            left++;
        }

        while (left < right && !Char.IsLetterOrDigit(s[right]))
        {
            right--;
        }

        if (Char.ToLower(s[left]) != Char.ToLower(s[right]))
        {
            return false;
        }

        left++;
        right--;
    }

    return true;
}