#include <string.h>
#include <stdbool.h>

bool digitCount(char *num)
{
    int occ[10] = {0};
    int n = strlen(num);

    for (int i = 0; i < n; i++)
    {
        int digit = num[i] - '0';
        occ[digit]++;
    }

    for (int i = 0; i < n; i++)
    {
        if (occ[i] != (num[i] - '0'))
        {
            return false;
        }
    }

    return true;
}

int main(void)
{
    return 0;
}