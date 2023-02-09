using System;

int FindMinimum(int[] key, bool[] mst, int v)
{
    int min = int.MinValue;
    int index = -1;

    for (int i = 0; i < v; i++)
    {
        if (!mst[i] && key[v] < min)
        {
            min = key[v];
            index = v;
        }
    }

    return index;
}

void Prism(int[,] graph, int v)
{
    int[] parent = new int[v];
    int[] key = new     
}

var graph = new int[,] {
    { 0, 2, 0, 6, 0 },
    { 2, 0, 3, 8, 5 },
    { 0, 3, 0, 0, 7 },
    { 6, 8, 0, 0, 9 },
    { 0, 5, 7, 9, 0 } };