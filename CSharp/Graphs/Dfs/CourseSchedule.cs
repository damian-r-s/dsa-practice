//207. Course Schedule
// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

// For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
// Return true if you can finish all courses. Otherwise, return false.

public class Solution
{
    public bool CanFinish(int numCourses, int[][] prerequisites)
    {
        CreateGraph(prerequisites);
        if (IsCycle())
            return false;

        return true;
    }

    private bool IsCycle()
    {
        var visited = new HashSet<int>();
        var processed = new HashSet<int>();

        foreach (var key in graph.Keys)
        {
            if (!visited.Contains(key))
            {
                if (Cycle(key, visited, processed))
                {
                    return true;
                }

                processed.Add(key);
            }
        }

        return false;
    }

    private bool Cycle(int from, HashSet<int> visited, HashSet<int> processed)
    {
        visited.Add(from);
        if (graph.ContainsKey(from))
        {
            foreach (var dest in graph[from])
            {
                if (!visited.Contains(dest))
                {
                    if (Cycle(dest, visited, processed))
                    {
                        return true;
                    }
                }

                if (visited.Contains(dest) && !processed.Contains(dest))
                    return true;
            }
        }

        processed.Add(from);

        return false;
    }

    private void CreateGraph(int[][] edges)
    {
        for (int i = 0; i < edges.Length; i++)
        {
            var src = edges[i][1];
            var to = edges[i][0];
            Connect(src, to);
        }
    }

    private Dictionary<int, List<int>> graph = new Dictionary<int, List<int>>();

    private void Connect(int from, int to)
    {
        if (!graph.ContainsKey(from))
        {
            graph.Add(from, new List<int>());
        }

        graph[from].Add(to);
    }
}