// 739. Daily Temperatures
// Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

int[] DailyTemperatures(int[] temperatures)
{
    var stack = new Stack<(int, int)>();
    stack.Push((temperatures[0], 0));
    var result = new int[temperatures.Length];

    for (int i = 1; i < temperatures.Length; i++)
    {
        var t = temperatures[i];
        while (stack.Count > 0 && stack.Peek().Item1 < t)
        {
            var item = stack.Pop();
            result[item.Item2] = i - item.Item2;
        }

        stack.Push((t, i));
    }

    return result;
}