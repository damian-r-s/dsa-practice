public class Solution
{
    public IList<int> FindSmallestSetOfVertices(int n, IList<IList<int>> edges)
    {
        var graph = CreateGraph(n, edges);

        var roots = new List<int>();
        var vertexes = new HashSet<int>();
        foreach (var vertex in graph)
        {
            roots.Add(vertex.Key);
            if (vertexes.Contains(vertex.Key))
                continue;

            var visited = new bool[n];
            Dfs(vertex.Key, visited, graph, vertexes);
        }

        IList<int> result = new List<int>();
        foreach (var root in roots)
        {
            if (!vertexes.Contains(root))
            {
                result.Add(root);
            }
        }

        return result;
    }

    private void Dfs(int from, bool[] visited, Dictionary<int, List<int>> graph, HashSet<int> vertexes)
    {
        if (visited[from])
            return;

        visited[from] = true;

        foreach (var vertex in graph[from])
        {
            if (!vertexes.Contains(vertex))
                vertexes.Add(vertex);

            Dfs(vertex, visited, graph, vertexes);
        }
    }

    private Dictionary<int, List<int>> CreateGraph(int n, IList<IList<int>> edges)
    {
        var graph = new Dictionary<int, List<int>>();

        for (int i = 0; i < n; i++)
            graph.Add(i, new List<int>());

        for (int i = 0; i < edges.Count; i++)
        {
            var from = edges[i][0];
            var to = edges[i][1];
            graph[from].Add(to);
        }

        return graph;
    }
}