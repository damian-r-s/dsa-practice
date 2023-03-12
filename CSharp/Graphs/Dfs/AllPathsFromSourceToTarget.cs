// Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

// The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

public class Solution
{
    public IList<IList<int>> AllPathsSourceTarget(int[][] graph)
    {
        CreateGraph(graph);
        var (state, paths) = Dfs(0, graph.Length - 1);
        return paths;
    }

    private (bool, IList<IList<int>>) Dfs(int start, int dest)
    {
        if (start == dest)
        {
            return (true, new List<IList<int>>() { new List<int>() { dest } });
        }

        var nodes = _graph[start];
        if (nodes.Count == 0)
        {
            return (false, new List<IList<int>>());
        }

        List<IList<int>> result = new List<IList<int>>();
        foreach (var node in nodes)
        {
            var (state, paths) = Dfs(node, dest);
            if (state)
            {
                foreach (var path in paths)
                {
                    path.Insert(0, start);
                    result.Add(path);
                }
            }
        }

        return (true, result);
    }

    private void CreateGraph(int[][] graph)
    {
        for (int i = 0; i < graph.Length; i++)
        {
            _graph.Add(i, new List<int>());
        }

        for (int i = 0; i < graph.Length; i++)
        {
            var edges = graph[i];
            for (int j = 0; j < edges.Length; j++)
            {
                var from = i;
                var to = edges[j];
                _graph[from].Add(to);
            }
        }
    }

    private Dictionary<int, List<int>> _graph = new Dictionary<int, List<int>>();
}