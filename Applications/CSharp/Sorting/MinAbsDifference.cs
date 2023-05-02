IList<IList<int>> MinimumAbsDifference(int[] arr)
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

    var minDist = int.MaxValue;
    IList<IList<int>> pairs = new List<IList<int>>();

    for (int i = 0; i < result.Length - 1; i++)
    {
        var item1 = result[i];
        var item2 = result[i + 1];

        var absDiff = Math.Abs(item1 - item2);
        if (absDiff == minDist)
        {
            pairs.Add(new List<int>() { item1, item2 });
        }
        else if (absDiff < minDist)
        {
            pairs.Clear();
            pairs.Add(new List<int>() { item1, item2 });
            minDist = absDiff;
        }
    }

    return pairs;
}