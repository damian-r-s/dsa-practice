class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}

class Solution
{
    public void ReorderList(ListNode head)
    {
        if (head == null || head.next == null)
            return;

        var result = head.next;
        var list = new List<ListNode>();
        while (result != null)
        {
            list.Add(result);
            result = result.next;
        }

        var l = 0;
        var r = list.Count - 1;
        result = head;
        while (l <= r)
        {
            result.next = list[r--];
            result.next.next = list[l++];
            result = result.next.next;
        }

        if (l == r)
        {
            result.next = list[l];
        }
        result.next = null;
    }
}