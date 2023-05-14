// You are given a 0-indexed string num of length n consisting of digits.
// Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

bool DigitCount(string num)
{
    int[] occurences = new int[10];

    for (int i = 0; i < num.Length; i++)
    {
        int digit = num[i] - '0';
        occurences[digit]++;
    }

    for (int i = 0; i < num.Length; i++)
    {
        if (occurences[i] != num[i] - '0')
            return false;
    }

    return true;
}