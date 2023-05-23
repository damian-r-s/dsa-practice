int MaxArea(int[] height)
{
    var l = 0;
    var r = height.Length - 1;
    var maxW = 0;

    while (l < r)
    {
        var hL = height[l];
        var hR = height[r];

        var ab = Math.Min(hL, hR) * (r - l);
        if (ab > maxW)
        {
            maxW = ab;
        }

        if (hL < hR)
        {
            l++;
        }
        else
            r--;
    }

    return maxW;
}