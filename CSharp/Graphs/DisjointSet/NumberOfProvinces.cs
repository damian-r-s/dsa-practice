// There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
// A province is a group of directly or indirectly connected cities and no other cities outside of the group.
// You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
// Return the total number of provinces.

using System;

int[] connected;

void Union(int x, int y)
{
    int xRoot = Find(x);
    int yRoot = Find(y);

    if (xRoot != yRoot)
    {
        connected[xRoot] = yRoot;
    }
}

int Find(int x)
{
    if (x == connected[x])
    {
        return x;
    }

    connected[x] = Find(connected[x]);
    return connected[x];
}

void Init(int m)
{
    connected = new int[m];
    for (int i = 0; i < m; i++)
    {
        connected[i] = i;
    }
}

int FindCircleNum(int[][] isConnected)
{
    int n = isConnected[0].Length;
    int m = isConnected.Length;

    Init(m);

    int result = m;
    for (int i = 0; i < m; i++)
    {
        for (int j = n - 1; j > i; j--)
        {
            if (isConnected[i][j] == 1)
            {
                int x = Find(i);
                int y = Find(j);

                if (x != y)
                {
                    Union(i, j);
                    result--;
                }
            }
        }
    }
    return result;
}