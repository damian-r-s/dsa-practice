// In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
// If the town judge exists, then:
// The town judge trusts nobody.
// Everybody (except for the town judge) trusts the town judge.
// There is exactly one person that satisfies properties 1 and 2.
// You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
// Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


//Typical in, out degree graph problem
int FindJudge(int n, int[][] trust)
{
    if (n == 1 && trust.Length == 0)
        return 1;
    else if (n == 2 && trust.Length == 0)
        return -1;

    var inDegree = new int[n + 1];
    var outDegree = new int[n + 1];

    for (int i = 0; i < trust.Length; i++)
    {
        inDegree[trust[i][1]] += 1;
        outDegree[trust[i][0]] += 1;
    }

    for (int i = 0; i < n + 1; i++)
    {
        if (inDegree[i] == n - 1 && outDegree[i] == 0)
        {
            return i;
        }
    }

    return -1;
}