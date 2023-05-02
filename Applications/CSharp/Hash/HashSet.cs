
//This is too slow, it needs additonal data structure BST
public class MyHashSet
{
    private List<int>[] _array;
    public MyHashSet() => _array = new List<int>[1000000];
    private int Hash(int key) => key % 7907;
    public void Add(int key)
    {
        var list = _array[Hash(key)];
        if (list == null)
        {
            list = _array[Hash(key)] = new List<int>();
            list.Add(key);
            return;
        }

        for (int i = 0; i < list.Count; i++)
        {
            if (list[i] == key)
                return;
        }
        list.Add(key);
    }

    public void Remove(int key)
    {
        var list = _array[Hash(key)];
        if (list == null)
            return;
        list.Remove(key);
    }

    public bool Contains(int key)
    {
        var list = _array[Hash(key)];
        if (list == null)
            return false;

        for (int i = 0; i < list.Count; i++)
            if (list[i] == key)
                return true;

        return false;
    }
}