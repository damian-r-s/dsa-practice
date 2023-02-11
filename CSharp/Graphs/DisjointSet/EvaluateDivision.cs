// You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
// Each Ai or Bi is a string that represents a single variable.
// You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
// Return the answers to all queries. If a single answer cannot be determined, return -1.0.
// Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

public class Solution
{
    private class Node
    {
        public Node(string key, double val)
        {
            Key = key;
            Value = val;
        }
        public string Key { get; private set; }
        public double Value { get; private set; }
    }

    public double[] CalcEquation(IList<IList<string>> equations, double[] values, IList<IList<string>> queries)
    {
        CreateGraph(equations, values);
        var result = new double[queries.Count];
        for (int i = 0; i < queries.Count; i++)
        {
            var query = queries[i];
            var from = query[0];
            var to = query[1];
            result[i] = Calculate(from, to, new HashSet<string>());
        }
        return result;
    }

    //DFS
    private double Calculate(string from, string to, HashSet<string> visited)
    {
        if (!(graph.ContainsKey(from) && graph.ContainsKey(to)))
        {
            return -1.0;
        }
        if (from == to)
        {
            return 1.0;
        }

        visited.Add(from);
        var adj = graph[from];
        foreach (var a in adj)
        {
            if (visited.Contains(a.Key))
                continue;

            double ans = Calculate(a.Key, to, visited);
            if (ans != -1.0)
            {
                return ans * a.Value;
            }
        }
        return -1.0;
    }

    private void CreateGraph(IList<IList<string>> equations, double[] values)
    {
        for (int i = 0; i < equations.Count; i++)
        {
            var equation = equations[i];
            var src = equation[0];
            var dest = equation[1];
            var val = values[i];

            Connect(src, dest, val);
            Connect(dest, src, 1 / val);
        }
    }

    private Dictionary<string, List<Node>> graph = new Dictionary<string, List<Node>>();
    void Connect(string from, string to, double value)
    {
        if (!graph.ContainsKey(from))
        {
            graph.Add(from, new List<Node>());
        }

        graph[from].Add(new Node(to, value));
    }

    List<Node> Find(string node)
    {
        if (graph.ContainsKey(node))
            return graph[node];

        return null;
    }
}