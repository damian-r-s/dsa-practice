// You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
// You can swap the characters at any pair of indices in the given pairs any number of times.
// Return the lexicographically smallest string that s can be changed to after using the swaps.


int[] Init(int size)
{
    var _v = new int[size];
    for (int i = 0; i < size; i++)
    {
        _v[i] = i;
    }
    return _v;
}

void Union(int x, int y, int[] _v)
{
    int xRoot = Find(x, _v);
    int yRoot = Find(y, _v);

    if (xRoot != yRoot)
    {
        _v[xRoot] = yRoot;
    }
}

int Find(int x, int[] _v)
{
    if (x == _v[x])
    {
        return x;
    }
    _v[x] = Find(_v[x], _v);
    return _v[x];
}

string Sort(string s, int[] v)
{
    var groups = new Dictionary<int, List<char>>();
    for (int i = 0; i < v.Length; i++)
    {
        var idx = Find(i, v);
        if (!groups.ContainsKey(idx))
        {
            groups.Add(idx, new List<char>());
        }

        groups[idx].Add(s[i]);
    }

    foreach (int key in groups.Keys)
    {
        groups[key] = groups[key].OrderBy(x => x).ToList();
    }

    var result = new char[s.Length];
    for (int i = 0; i < v.Length; i++)
    {
        var lst = groups[v[i]];
        result[i] = lst[0];
        lst.RemoveAt(0);
    }

    return new string(result);
}

string SmallestStringWithSwaps(string s, IList<IList<int>> pairs)
{
    var _v = Init(s.Length);

    for (int i = 0; i < pairs.Count; i++)
    {
        var x = pairs[i][0];
        var y = pairs[i][1];

        Union(x, y, _v);
    }

    return Sort(s, _v);
}