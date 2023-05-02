using System.Collections.Generic;

PriorityQueue<(int, int), int> _q = new PriorityQueue<(int, int), int>();
Dictionary<int, List<(int, int)>> graph = new Dictionary<int, List<(int, int)>>();

int Prims(int n, List<List<int>> edges, int start)
{
    CreateGraph(edges);
    return Mst(start, n);
}

int Mst(int start, int v)
{
    var visited = new HashSet<int>();
    var result = 0;
    var src = start;

    while (--v > 0)
    {
        visited.Add(src);
        foreach (var edge in graph[src])
        {
            var dest = edge.Item1;
            if (visited.Contains(dest))
                continue;

            var weight = edge.Item2;
            _q.Enqueue((dest, weight), weight);
        }

        var next = FindMin(visited);
        src = next.Item1;
        result += next.Item2;
    }
    return result;
}

(int, int) FindMin(HashSet<int> visited)
{
    (int, int) next = _q.Dequeue();
    while (visited.Contains(next.Item1))
    {
        next = _q.Dequeue();
    }
    return next;
}

void CreateGraph(List<List<int>> edges)
{
    for (int i = 0; i < edges.Count; i++)
    {
        var src = edges[i][0];
        var dest = edges[i][1];
        var weight = edges[i][2];

        Connect(src, dest, weight);
    }
}

void Connect(int src, int dest, int weight)
{
    if (!graph.ContainsKey(src))
    {
        graph.Add(src, new List<(int, int)>());
    }
    graph[src].Add((dest, weight));

    if (!graph.ContainsKey(dest))
    {
        graph.Add(dest, new List<(int, int)>());
    }
    graph[dest].Add((src, weight));
}
