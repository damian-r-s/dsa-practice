int[] CountingSort(int[] lst)
{
    int maximum = lst.Max();
    int[] counts = new int[maximum + 1];
    for (int i = 0; i < lst.Length; i++)
    {
        var element = lst[i];
        counts[element] += 1;
    }

    int idx = 0;
    for (int i = 0; i < counts.Length; i++)
    {
        var count = counts[i];
        counts[i] = idx;
        idx += count;
    }

    var result = new int[lst.Length];
    for (int i = 0; i < result.Length; i++)
    {
        var element = lst[i];
        result[counts[element]] = lst[i];
        counts[element] += 1;
    }

    return result;
}