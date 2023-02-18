int[] ShiftedCoutingSort(int[] arr)
{
    var maximum = arr.Max();
    var minimum = arr.Min();
    var dist = maximum - minimum;
    var counts = new int[dist + 1];
    foreach (var element in arr)
    {
        counts[element - minimum] += 1;
    }

    var idx = 0;
    for (int i = 0; i < dist + 1; i++)
    {
        var count = counts[i];
        counts[i] = idx;
        idx += count;
    }

    var result = new int[arr.Length];
    for (int i = 0; i < arr.Length; i++)
    {
        var element = arr[i];
        result[counts[element - minimum]] = element;
        counts[element - minimum] += 1;
    }

    return result;
}
