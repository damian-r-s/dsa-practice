// Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
// Implement KthLargest class:
// KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
// int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

using System.Collections.Generic;

public class KthLargest
{
    private PriorityQueue<int, int> _q = new PriorityQueue<int, int>();
    private int _k;
    public KthLargest(int k, int[] nums)
    {
        _k = k;
        Init(k, nums);
        Adjust();
    }

    private void Init(int k, int[] nums)
    {
        for (int i = 0; i < nums.Length; i++)
        {
            _q.Enqueue(nums[i], nums[i]);
        }
    }

    private void Adjust()
    {
        while (_q.Count > _k)
        {
            _q.Dequeue();
        }
    }

    public int Add(int val)
    {
        _q.Enqueue(val, val);
        Adjust();
        return _q.Peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.Add(val);
 */