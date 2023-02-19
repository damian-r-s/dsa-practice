// There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
// You want to determine if there is a valid path that exists from vertex source to vertex destination.
// Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.


public class Solution
{

    private int[] _connected;
    public bool ValidPath(int n, int[][] edges, int source, int destination)
    {
        if (source == destination)
            return true;
        Init(n);

        for (int i = 0; i < edges.Length; i++)
        {
            var edge = edges[i];
            var x = edge[0];
            var y = edge[1];
            Union(x, y);

            if (Connected(source, destination))
            {
                return true;
            }
        }

        return false;
    }

    private void Init(int n)
    {
        _connected = new int[n];
        for (int i = 0; i < n; i++)
        {
            _connected[i] = i;
        }
    }

    private bool Connected(int x, int y)
    {
        return Find(x) == Find(y);
    }

    private int Find(int x)
    {
        if (x == _connected[x])
        {
            return x;
        }

        _connected[x] = Find(_connected[x]);
        return _connected[x];
    }

    private void Union(int x, int y)
    {
        int xRoot = Find(x);
        int yRoot = Find(y);

        if (xRoot != yRoot)
        {
            _connected[xRoot] = yRoot;
        }
    }
}

