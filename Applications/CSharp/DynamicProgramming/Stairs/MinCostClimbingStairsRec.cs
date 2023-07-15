// 746. Min Cost Climbing Stairs
//You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
//You can either start from the step with index 0, or the step with index 1.
//Return the minimum cost to reach the top of the floor.

public class Solution
{
    public int MinCostClimbingStairs(int[] cost)
    {
        return CalculateMinCost(cost, cost.Length);
    }

    private Dictionary<int, int> dic = new Dictionary<int, int>();

    public int CalculateMinCost(int[] cost, int n)
    {
        if (n < 0)
        {
            return 0;
        }

        if (dic.ContainsKey(n))
            return dic[n];

        var curr = (n >= cost.Length) ? 0 : cost[n];
        dic[n] = curr + Math.Min(CalculateMinCost(cost, n - 1), CalculateMinCost(cost, n - 2));

        return dic[n];
    }
}