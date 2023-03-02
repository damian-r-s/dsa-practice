//Hanckerrank EvenTree
// You are given a tree (a simple connected graph with no cycles).
// Find the maximum number of edges you can remove from the tree to get a forest such that each connected component of the forest contains an even number of nodes.


using System.Collections.Generic;
using System.Collections;
using System.IO;
using System.Linq;
using System;

int cut = 0;
// Complete the evenForest function below.
int evenForest(int t_nodes, int t_edges, List<int> t_from, List<int> t_to)
{
    var nodes = new Dictionary<int, List<int>>();

    for (int i = 1; i <= t_nodes; i++)
    {
        nodes.Add(i, new List<int>());
    }

    for (int i = 0; i < t_edges; i++)
    {
        var from = t_from[i];
        var to = t_to[i];

        nodes[from].Add(to);
        nodes[to].Add(from);
    }

    var visited = new bool[t_nodes + 1];
    Dfs(1, nodes, visited);
    return cut;
}

int Dfs(int start, Dictionary<int, List<int>> nodes, bool[] visited)
{
    visited[start] = true;
    int number = 0;

    foreach (var node in nodes[start])
    {
        if (visited[node])
        {
            continue;
        }

        var n = Dfs(node, nodes, visited);

        if (n % 2 == 0)
        {
            cut++;
        }
        else
        {
            number += n;
        }
    }

    return number + 1;
}