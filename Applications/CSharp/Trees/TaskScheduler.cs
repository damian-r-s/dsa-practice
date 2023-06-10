//621. Task Scheduler
// Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
// However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
// Return the least number of units of times that the CPU will take to finish all the given tasks.

public class Solution
{
    public int LeastInterval(char[] tasks, int n)
    {
        if (n == 0)
            return tasks.Length;

        var dic = tasks.GroupBy(c => c).Select(g => new { key = g.Key, count = g.Count() }).ToDictionary(i => i.key, i => i.count);

        var pq = new PriorityQueue<FreqClass, int>(new MaxHeap());
        foreach (var kv in dic)
            pq.Enqueue(new FreqClass(kv.Value, 0, kv.Key), kv.Value);

        var time = 0;
        while (pq.Count > 0)
        {
            var lst = new List<FreqClass>();
            var cnt = 0;
            for (var i = 0; i < n + 1; i++)
                if (pq.Count > 0)
                {
                    var item = pq.Dequeue();
                    cnt++;
                    item.Frequency--;
                    if (item.Frequency > 0)
                    {
                        lst.Add(item);
                    }
                }

            for (var i = 0; i < lst.Count; i++)
                pq.Enqueue(lst[i], lst[i].Frequency);

            time += pq.Count == 0 ? cnt : n + 1;
        }

        return time;
    }

    private class MaxHeap : IComparer<int>
    {
        public int Compare(int x, int y) => y - x;
    }

    private class FreqClass
    {
        public int Frequency { get; set; }
        public int IdleTime { get; set; }
        public char Task { get; set; }

        public FreqClass(int frequency, int idleTime, char task)
        {
            Frequency = frequency;
            IdleTime = idleTime;
            Task = task;
        }
    }
}