class Trie
{
    class Node
    {
        public Node[] _nodes;
        public bool end;
        public Node()
        {
            _nodes = new Node[26];
        }
    }
    private Node _root;

    public Trie()
    {
        _root = new Node();
    }

    private int ConvertToInt(char c) => (int)(c - 'a');

    public void Insert(string word)
    {
        var current = _root;
        foreach (var c in word)
        {
            int pointer = ConvertToInt(c);
            if (current._nodes[pointer] == null)
                current._nodes[pointer] = new Node();

            current = current._nodes[pointer];
        }

        current.end = true;
    }

    public bool Search(string word)
    {
        var current = _root;
        foreach (var c in word)
        {
            int pointer = ConvertToInt(c);
            if (current._nodes[pointer] == null)
            {
                return false;
            }
            current = current._nodes[pointer];
        }

        return current.end;
    }

    public bool StartsWith(string prefix)
    {
        var current = _root;
        foreach (var c in prefix)
        {
            int pointer = ConvertToInt(c);
            if (current._nodes[pointer] == null)
            {
                return false;
            }
            current = current._nodes[pointer];
        }

        return true;
    }
}