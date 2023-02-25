int FindClosest(int[] distance, bool[] visited)
{
    int minimum = int.MaxValue;
    int index = -1;
    for (int i = 0; i < distance.Length; i++)
    {
        if (visited[i])
            continue;

        if (distance[i] < minimum)
        {
            minimum = distance[i];
            index = i;
        }
    }

    return index;
}

int[] FindShortestPaths(int[,] graph, int source)
{
    int count = graph.GetLength(0);

    int[] distance = new int[count];
    bool[] visited = new bool[count];

    for (int i = 0; i < count; i++)
    {
        distance[i] = int.MaxValue;
    }

    distance[source] = 0;

    for (int i = 0; i < count - 1; i++)
    {
        int current = FindClosest(distance, visited);
        visited[current] = true;

        for (int j = 0; j < count; j++)
        {
            var edgeWeight = graph[current, j];

            if (edgeWeight > 0 && !visited[j] && distance[current] != int.MaxValue && distance[current] + edgeWeight < distance[j])
            {
                distance[j] = distance[current] + edgeWeight;
            }
        }
    }

    return distance;
}
