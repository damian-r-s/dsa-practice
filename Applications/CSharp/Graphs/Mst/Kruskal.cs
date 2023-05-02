//HackerRank Kruskal (MST): Really Special Subtree

class KruskalMST
{

    /*
     * Complete the 'kruskals' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
     */

    /*
     * For the weighted graph, <name>:
     *
     * 1. The number of nodes is <name>Nodes.
     * 2. The number of edges is <name>Edges.
     * 3. An edge exists between <name>From[i] and <name>To[i]. The weight of the edge is <name>Weight[i].
     *
     */

    private class Edge : IComparable<Edge>
    {
        public int From;
        public int To;
        public int Weight;

        public Edge(int from, int to, int weight)
        {
            From = from;
            To = to;
            Weight = weight;
        }

        public int CompareTo(Edge? other)
        {
            var result = Weight.CompareTo(other.Weight);
            if (result != 0)
                return result;

            return (From + Weight + To).CompareTo(other.From + other.Weight + other.To);
        }
    }

    private class DisjointSet
    {
        private int[] _connected;

        public DisjointSet(int size)
        {
            _connected = new int[size];
            for (int i = 0; i < size; i++)
            {
                _connected[i] = i;
            }
        }

        public void Union(int from, int to)
        {
            int fromRoot = Find(from);
            int toRoot = Find(to);

            if (fromRoot != toRoot)
            {
                _connected[fromRoot] = _connected[toRoot];
            }
        }

        public int Find(int x)
        {
            if (x == _connected[x])
                return x;

            _connected[x] = Find(_connected[x]);
            return _connected[x];
        }
    }

    private static List<Edge> Sort(List<int> gFrom, List<int> gTo, List<int> gWeight)
    {
        var result = new List<Edge>();
        for (int i = 0; i < gFrom.Count; i++)
        {
            var from = gFrom[i];
            var to = gTo[i];
            var w = gWeight[i];

            result.Add(new Edge(from, to, w));
        }

        result.Sort();
        return result;
    }

    private static int CalculateMST(int verticies, List<Edge> edges)
    {
        var ds = new DisjointSet(verticies + 1);
        var result = 0;
        foreach (var edge in edges)
        {
            var from = edge.From;
            var to = edge.To;
            var weight = edge.Weight;

            if (ds.Find(from) == ds.Find(to))
            {
                continue;
            }
            ds.Union(from, to);
            result += weight;
        }

        return result;
    }

    public static int kruskals(int gNodes, List<int> gFrom, List<int> gTo, List<int> gWeight)
    {
        return CalculateMST(gNodes, Sort(gFrom, gTo, gWeight));
    }
}
