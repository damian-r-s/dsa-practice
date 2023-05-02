// 210. Course Schedule II
// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

// For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
// Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

public class Solution
{
    public int[] FindOrder(int numCourses, int[][] prerequisites)
    {
        if (prerequisites.Length == 0 && numCourses > 0)
        {
            var result = new int[numCourses];
            int idx = 0;
            for (int i = numCourses - 1; i >= 0; i--)
            {
                result[idx] = i;
                idx++;
            }

            return result;
        }

        CrateGraph(numCourses, prerequisites);
        return Order();
    }

    private int[] Order()
    {
        var visited = new HashSet<int>();
        var processed = new HashSet<int>();

        foreach (var node in graph.Keys)
        {
            if (!visited.Contains(node))
            {
                if (!Order(node, visited, processed))
                {
                    return new int[] { };
                }

                processed.Add(node);
            }
        }

        var result = processed.ToArray();
        Array.Reverse(result);
        return result;
    }

    private bool Order(int src, HashSet<int> visited, HashSet<int> processed)
    {
        visited.Add(src);

        if (graph.ContainsKey(src))
        {
            foreach (var edge in graph[src])
            {
                if (!visited.Contains(edge))
                {
                    if (!Order(edge, visited, processed))
                    {
                        return false;
                    }
                }

                if (visited.Contains(edge) && !processed.Contains(edge))
                {
                    return false;
                }
            }
        }

        processed.Add(src);

        return true;
    }

    private void CrateGraph(int vertex, int[][] edges)
    {
        for (int i = 0; i < vertex; i++)
        {
            graph.Add(i, new List<int>());
        }

        for (int i = 0; i < edges.Length; i++)
        {
            var src = edges[i][1];
            var dest = edges[i][0];
            graph[src].Add(dest);
        }
    }

    private Dictionary<int, List<int>> graph = new Dictionary<int, List<int>>();
}