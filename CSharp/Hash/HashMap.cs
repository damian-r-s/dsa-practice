//This is too slow, it needs additonal data structure BST
public class MyHashMap
{
    private List<(int, int)>[] _array;
    public MyHashMap() => _array = new List<(int, int)>[1000000];
    private int Hash(int key) => key % 7907;
    public void Put(int key, int value)
    {
        var list = _array[Hash(key)];
        if (list == null)
        {
            list = _array[Hash(key)] = new List<(int, int)>();
            list.Add((key, value));
            return;
        }
        for (int i = 0; i < list.Count; i++)
        {
            if (list[i].Item1 == key)
            {
                list.RemoveAt(i);
                break;
            }
        }
        list.Add((key, value));
    }

    public int Get(int key)
    {
        var list = _array[Hash(key)];
        if (list == null)
            return -1;

        for (int i = 0; i < list.Count; i++)
            if (list[i].Item1 == key)
                return list[i].Item2;

        return -1;
    }

    public void Remove(int key)
    {
        var list = _array[Hash(key)];
        if (list == null)
            return;

        for (int i = 0; i < list.Count; i++)
            if (list[i].Item1 == key)
            {
                list.RemoveAt(i);
                return;
            }
    }
}