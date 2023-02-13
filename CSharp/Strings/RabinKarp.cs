//Rabin-Karp algorithm
int[] Search(string pattern, string text, int q)
{
    int d = 256; //Number of characters
    int m = pattern.Length;
    int n = text.Length;
    int p = 0; //hash value of the pattern
    int t = 0; //hash value of the text
    int h = 1;

    for (int i = 0; i < m - 1; i++)
    {
        h = (h * d) % q;
    }

    //Calculate initial value
    for (int i = 0; i < m; i++)
    {
        p = (p * d + pattern[i]) % q;
        t = (t * d + text[i]) % q;
    }

    var results = new List<int>();
    for (int i = 0; i <= n - m; i++)
    {
        if (p == t)
        {
            for (int j = 0; j < m; j++)
            {
                if (pattern[j] != text[j + i])
                {
                    break;
                }
                if ((j + 1) == m)
                    results.Add(i);
            }
        }

        if (i < n - m)
        {
            t = (d * (t - text[i] * h) + text[i + m]) % q;
            if (t < 0)
                t = (t + q);
        }
    }

    return results.ToArray();
}