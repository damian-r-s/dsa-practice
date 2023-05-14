
bool IsHappy(int n)
{
    HashSet<int> set = new HashSet<int>();
    int digits = n;
    while (digits != 1)
    {
        var sum = 0;
        foreach (var digit in digits.ToString())
        {
            var d = (digit - '0');
            sum += d * d;
        }
        if (set.Contains(sum))
        {
            return false;
        }
        digits = sum;
        set.Add(sum);
    }

    return true;
}