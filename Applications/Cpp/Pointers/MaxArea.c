#define MIN(x, y) (((x) < (y)) ? (x) : (y))

int maxArea(int *height, int heightSize)
{
    int l = 0;
    int r = heightSize - 1;
    int maxW = 0;

    while (l < r)
    {
        int hl = height[l];
        int hr = height[r];

        int w = MIN(hl, hr) * (r - l);
        if (w > maxW)
        {
            maxW = w;
        }

        if (hl < hr)
        {
            l++;
        }
        else
        {
            r--;
        }
    }

    return maxW;
}

int main(void)
{
    return 0;
}